from __future__ import print_function

import torch
import pickle
import numpy as np
import math
import cv2
from PIL import Image, JpegImagePlugin
from scipy import ndimage
import hashlib
import sys, os
from zipfile import ZipFile
from .imgproc import loadImage

if sys.version_info[0] == 2:
    from six.moves.urllib.request import urlretrieve
else:
    from urllib.request import urlretrieve

import os

current_path = os.getcwd()
print("Current working directory:", current_path)
current_path = os.path.abspath(__file__)

def consecutive(data, mode ='first', stepsize=1):
    group = np.split(data, np.where(np.diff(data) != stepsize)[0]+1)
    group = [item for item in group if len(item)>0]

    if mode == 'first': result = [l[0] for l in group]
    elif mode == 'last': result = [l[-1] for l in group]
    return result

def word_segmentation(mat, separator_idx =  {'th': [1,2],'en': [3,4]}, separator_idx_list = [1,2,3,4]):
    result = []
    sep_list = []
    start_idx = 0
    sep_lang = ''
    for sep_idx in separator_idx_list:
        if sep_idx % 2 == 0: mode ='first'
        else: mode ='last'
        a = consecutive( np.argwhere(mat == sep_idx).flatten(), mode)
        new_sep = [ [item, sep_idx] for item in a]
        sep_list += new_sep
    sep_list = sorted(sep_list, key=lambda x: x[0])

    for sep in sep_list:
        for lang in separator_idx.keys():
            if sep[1] == separator_idx[lang][0]: # start lang
                sep_lang = lang
                sep_start_idx = sep[0]
            elif sep[1] == separator_idx[lang][1]: # end lang
                if sep_lang == lang: # check if last entry if the same start lang
                    new_sep_pair = [lang, [sep_start_idx+1, sep[0]-1]]
                    if sep_start_idx > start_idx:
                        result.append( ['', [start_idx, sep_start_idx-1] ] )
                    start_idx = sep[0]+1
                    result.append(new_sep_pair)
                sep_lang = ''# reset

    if start_idx <= len(mat)-1:
        result.append( ['', [start_idx, len(mat)-1] ] )
    return result

# code is based from https://github.com/githubharald/CTCDecoder/blob/master/src/BeamSearch.py
class BeamEntry:
    "information about one single beam at specific time-step"
    def __init__(self):
        self.prTotal = 0 # blank and non-blank
        self.prNonBlank = 0 # non-blank
        self.prBlank = 0 # blank
        self.prText = 1 # LM score
        self.lmApplied = False # flag if LM was already applied to this beam
        self.labeling = () # beam-labeling
        self.simplified = True  # To run simplyfiy label

class BeamState:
    "information about the beams at specific time-step"
    def __init__(self):
        self.entries = {}

    def norm(self):
        "length-normalise LM score"
        for (k, _) in self.entries.items():
            labelingLen = len(self.entries[k].labeling)
            self.entries[k].prText = self.entries[k].prText ** (1.0 / (labelingLen if labelingLen else 1.0))

    def sort(self):
        "return beam-labelings, sorted by probability"
        beams = [v for (_, v) in self.entries.items()]
        sortedBeams = sorted(beams, reverse=True, key=lambda x: x.prTotal*x.prText)
        return [x.labeling for x in sortedBeams]

    def wordsearch(self, classes, ignore_idx, maxCandidate, dict_list):
        beams = [v for (_, v) in self.entries.items()]
        sortedBeams = sorted(beams, reverse=True, key=lambda x: x.prTotal*x.prText)
        if len(sortedBeams) >  maxCandidate: sortedBeams = sortedBeams[:maxCandidate]

        for j, candidate in enumerate(sortedBeams):
            idx_list = candidate.labeling
            text = ''
            for i,l in enumerate(idx_list):
                if l not in ignore_idx and (not (i > 0 and idx_list[i - 1] == idx_list[i])):
                    text += classes[l]

            if j == 0: best_text = text
            if text in dict_list:
                #print('found text: ', text)
                best_text = text
                break
            else:
                pass
                #print('not in dict: ', text)
        return best_text

def applyLM(parentBeam, childBeam, classes, lm):
    "calculate LM score of child beam by taking score from parent beam and bigram probability of last two chars"
    if lm and not childBeam.lmApplied:
        c1 = classes[parentBeam.labeling[-1] if parentBeam.labeling else classes.index(' ')] # first char
        c2 = classes[childBeam.labeling[-1]] # second char
        lmFactor = 0.01 # influence of language model
        bigramProb = lm.getCharBigram(c1, c2) ** lmFactor # probability of seeing first and second char next to each other
        childBeam.prText = parentBeam.prText * bigramProb # probability of char sequence
        childBeam.lmApplied = True # only apply LM once per beam entry

def simplify_label(labeling, blankIdx = 0):
    labeling = np.array(labeling)

    # collapse blank
    idx = np.where(~((np.roll(labeling,1) == labeling) & (labeling == blankIdx)))[0]
    labeling = labeling[idx]

    # get rid of blank between different characters
    idx = np.where( ~((np.roll(labeling,1) != np.roll(labeling,-1)) & (labeling == blankIdx)) )[0]

    if len(labeling) > 0:
        last_idx = len(labeling)-1
        if last_idx not in idx: idx = np.append(idx, [last_idx])
    labeling = labeling[idx]

    return tuple(labeling)

def fast_simplify_label(labeling, c, blankIdx=0):

    # Adding BlankIDX after Non-Blank IDX
    if labeling and c == blankIdx and labeling[-1] != blankIdx:
        newLabeling = labeling + (c,)

    # Case when a nonBlankChar is added after BlankChar |len(char) - 1
    elif labeling and c != blankIdx and labeling[-1] == blankIdx:

        # If Blank between same character do nothing | As done by Simplify label
        if labeling[-2] == c:
            newLabeling = labeling + (c,)

        # if blank between different character, remove it | As done by Simplify Label
        else:
            newLabeling = labeling[:-1] + (c,)

    # if consecutive blanks : Keep the original label
    elif labeling and c == blankIdx and labeling[-1] == blankIdx:
        newLabeling = labeling

    # if empty beam & first index is blank
    elif not labeling and c == blankIdx:
        newLabeling = labeling

    # if empty beam & first index is non-blank
    elif not labeling and c != blankIdx:
        newLabeling = labeling + (c,)

    elif labeling and c != blankIdx:
        newLabeling = labeling + (c,)

    # Cases that might still require simplyfying
    else:
        newLabeling = labeling + (c,)
        newLabeling = simplify_label(newLabeling, blankIdx)

    return newLabeling

def addBeam(beamState, labeling):
    "add beam if it does not yet exist"
    if labeling not in beamState.entries:
        beamState.entries[labeling] = BeamEntry()

def ctcBeamSearch(mat, classes, ignore_idx, lm, beamWidth=25, dict_list = []):
    blankIdx = 0
    maxT, maxC = mat.shape

    # initialise beam state
    last = BeamState()
    labeling = ()
    last.entries[labeling] = BeamEntry()
    last.entries[labeling].prBlank = 1
    last.entries[labeling].prTotal = 1

    # go over all time-steps
    for t in range(maxT):
        curr = BeamState()
        # get beam-labelings of best beams
        bestLabelings = last.sort()[0:beamWidth]
        # go over best beams
        for labeling in bestLabelings:
            # probability of paths ending with a non-blank
            prNonBlank = 0
            # in case of non-empty beam
            if labeling:
                # probability of paths with repeated last char at the end
                prNonBlank = last.entries[labeling].prNonBlank * mat[t, labeling[-1]]

            # probability of paths ending with a blank
            prBlank = (last.entries[labeling].prTotal) * mat[t, blankIdx]

            # add beam at current time-step if needed
            prev_labeling = labeling
            if not last.entries[labeling].simplified:
                labeling = simplify_label(labeling, blankIdx)

            # labeling = simplify_label(labeling, blankIdx)
            addBeam(curr, labeling)

            # fill in data
            curr.entries[labeling].labeling = labeling
            curr.entries[labeling].prNonBlank += prNonBlank
            curr.entries[labeling].prBlank += prBlank
            curr.entries[labeling].prTotal += prBlank + prNonBlank
            curr.entries[labeling].prText = last.entries[prev_labeling].prText
            # beam-labeling not changed, therefore also LM score unchanged from

            #curr.entries[labeling].lmApplied = True # LM already applied at previous time-step for this beam-labeling

            # extend current beam-labeling
            # char_highscore = np.argpartition(mat[t, :], -5)[-5:] # run through 5 highest probability
            char_highscore = np.where(mat[t, :] >= 0.5/maxC)[0] # run through all probable characters
            for c in char_highscore:
            #for c in range(maxC - 1):
                # add new char to current beam-labeling
                # newLabeling = labeling + (c,)
                # newLabeling = simplify_label(newLabeling, blankIdx)
                newLabeling = fast_simplify_label(labeling, c, blankIdx)

                # if new labeling contains duplicate char at the end, only consider paths ending with a blank
                if labeling and labeling[-1] == c:
                    prNonBlank = mat[t, c] * last.entries[prev_labeling].prBlank
                else:
                    prNonBlank = mat[t, c] * last.entries[prev_labeling].prTotal

                # add beam at current time-step if needed
                addBeam(curr, newLabeling)

                # fill in data
                curr.entries[newLabeling].labeling = newLabeling
                curr.entries[newLabeling].prNonBlank += prNonBlank
                curr.entries[newLabeling].prTotal += prNonBlank

                # apply LM
                #applyLM(curr.entries[labeling], curr.entries[newLabeling], classes, lm)

        # set new beam state

        last = curr

    # normalise LM scores according to beam-labeling-length
    last.norm()

    if dict_list == []:
        bestLabeling = last.sort()[0] # get most probable labeling
        res = ''
        for i,l in enumerate(bestLabeling):
            # removing repeated characters and blank.
            if l not in ignore_idx and (not (i > 0 and bestLabeling[i - 1] == bestLabeling[i])):
                res += classes[l]
    else:
        res = last.wordsearch(classes, ignore_idx, 20, dict_list)
    return res


class CTCLabelConverter(object):
    """ Convert between text-label and text-index """

    def __init__(self, character, separator_list = {}, dict_pathlist = {}):
        # character (str): set of the possible characters.
        dict_character = list(character)

        import os

        current_path = os.getcwd()
        print(fr"Current working directory CTCLabelConverter current_path : {current_path}, character : {character}")

        self.dict = {}
        for i, char in enumerate(dict_character):
            self.dict[char] = i + 1

        self.character = ['[blank]'] + dict_character  # dummy '[blank]' token for CTCLoss (index 0)

        self.separator_list = separator_list
        separator_char = []
        for lang, sep in separator_list.items():
            separator_char += sep
        self.ignore_idx = [0] + [i+1 for i,item in enumerate(separator_char)]

        ####### latin dict
        if len(separator_list) == 0:
            dict_list = []
            for lang, dict_path in dict_pathlist.items():
                try:
                    with open(dict_path, "r", encoding = "utf-8-sig") as input_file:
                        word_count =  input_file.read().splitlines()
                    dict_list += word_count
                except:
                    pass
        else:
            dict_list = {}
            for lang, dict_path in dict_pathlist.items():
                with open(dict_path, "r", encoding = "utf-8-sig") as input_file:
                    word_count =  input_file.read().splitlines()
                dict_list[lang] = word_count

        self.dict_list = dict_list

    def encode(self, text, batch_max_length=25):
        """convert text-label into text-index.
        input:
            text: text labels of each image. [batch_size]

        output:
            text: concatenated text index for CTCLoss.
                    [sum(text_lengths)] = [text_index_0 + text_index_1 + ... + text_index_(n - 1)]
            length: length of each text. [batch_size]
        """
        length = [len(s) for s in text]
        text = ''.join(text)
        text = [self.dict[char] for char in text]

        return (torch.IntTensor(text), torch.IntTensor(length))

    def decode_greedy(self, text_index, length):
        """ convert text-index into text-label. """
        texts = []
        index = 0
        for l in length:
            t = text_index[index:index + l]
            # Returns a boolean array where true is when the value is not repeated
            a = np.insert(~((t[1:]==t[:-1])),0,True)
            # Returns a boolean array where true is when the value is not in the ignore_idx list
            b = ~np.isin(t,np.array(self.ignore_idx))
            # Combine the two boolean array
            c = a & b
            # Gets the corresponding character according to the saved indexes
            text = ''.join(np.array(self.character)[t[c.nonzero()]])
            texts.append(text)
            index += l
        return texts

    def decode_beamsearch(self, mat, beamWidth=5):
        texts = []
        for i in range(mat.shape[0]):
            t = ctcBeamSearch(mat[i], self.character, self.ignore_idx, None, beamWidth=beamWidth)
            texts.append(t)
        return texts

    def decode_wordbeamsearch(self, mat, beamWidth=5):
        texts = []
        argmax = np.argmax(mat, axis = 2)

        for i in range(mat.shape[0]):
            string = ''
            # without separators - use space as separator
            if len(self.separator_list) == 0:
                space_idx = self.dict[' ']

                data = np.argwhere(argmax[i]!=space_idx).flatten()
                group = np.split(data, np.where(np.diff(data) != 1)[0]+1)
                group = [ list(item) for item in group if len(item)>0]

                for j, list_idx in enumerate(group):
                    matrix = mat[i, list_idx,:]
                    t = ctcBeamSearch(matrix, self.character, self.ignore_idx, None,\
                                      beamWidth=beamWidth, dict_list=self.dict_list)
                    if j == 0: string += t
                    else: string += ' '+t

            # with separators
            else:
                words = word_segmentation(argmax[i])

                for word in words:
                    matrix = mat[i, word[1][0]:word[1][1]+1,:]
                    if word[0] == '': dict_list = []
                    else: dict_list = self.dict_list[word[0]]
                    t = ctcBeamSearch(matrix, self.character, self.ignore_idx, None, beamWidth=beamWidth, dict_list=dict_list)
                    string += t
            texts.append(string)
        return texts

def merge_to_free(merge_result, free_list):
    merge_result_buf, mr_buf = [], []

    if not free_list:
        return merge_result

    free_list_buf = merge_result[-len(free_list):]
    merge_result = merge_result[:-len(free_list)]

    for idx, r in enumerate(merge_result):
        if idx == len(merge_result)-1:
            mr_buf.append(r)
            merge_result_buf.append(mr_buf)
            mr_buf=[]
            continue

        if (mr_buf == []) or (mr_buf[-1][0] < r[0]):
            mr_buf.append(r)
        else:
            merge_result_buf.append(mr_buf)
            mr_buf=[]
            mr_buf.append(r)

    for free_pos in free_list_buf:
        y_pos = len(merge_result_buf)
        x_pos = len(merge_result_buf[y_pos-1])
        for i, result_pos in enumerate(merge_result_buf[1:]):
            if free_pos[0][0][1] < result_pos[0][0][0][1]:
                y_pos = i
                break

        for i, result_pos in enumerate(merge_result_buf[y_pos]):
            if free_pos[0][0][0] < result_pos[0][0][0]:
                x_pos = i
                break
                
        merge_result_buf[y_pos].insert(x_pos, free_pos)

    merge_result = []
    [merge_result.extend(r) for r in merge_result_buf]
    return merge_result

def four_point_transform(image, rect):
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([[0, 0],[maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1],[0, maxHeight - 1]], dtype = "float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

def group_text_box(polys, slope_ths = 0.1, ycenter_ths = 0.5, height_ths = 0.5, width_ths = 1.0, add_margin = 0.05, sort_output = True):
    # poly top-left, top-right, low-right, low-left
    horizontal_list, free_list,combined_list, merged_list = [],[],[],[]



    for poly in polys:

        print(fr'group_text_box polys : {current_path} {polys}')
        print(fr'group_text_box poly : {current_path} {poly}')


        slope_up = (poly[3]-poly[1])/np.maximum(10, (poly[2]-poly[0]))
        slope_down = (poly[5]-poly[7])/np.maximum(10, (poly[4]-poly[6]))

        print(fr'group_text_box slope_up : {current_path} {slope_up}')
        print(fr'group_text_box slope_down : {current_path} {slope_down}')

        if max(abs(slope_up), abs(slope_down)) < slope_ths:
            x_max = max([poly[0],poly[2],poly[4],poly[6]])
            x_min = min([poly[0],poly[2],poly[4],poly[6]])
            y_max = max([poly[1],poly[3],poly[5],poly[7]])
            y_min = min([poly[1],poly[3],poly[5],poly[7]])
            horizontal_list.append([x_min, x_max, y_min, y_max, 0.5*(y_min+y_max), y_max-y_min])

            print(fr'group_text_box x_max : {current_path} {x_max}')
            print(fr'group_text_box x_min : {current_path} {x_min}')
            print(fr'group_text_box y_max : {current_path} {y_max}')
            print(fr'group_text_box y_min : {current_path} {y_min}')
            print(fr'group_text_box horizontal_list : {current_path} {horizontal_list}')

        else:
            height = np.linalg.norm([poly[6]-poly[0],poly[7]-poly[1]])
            width = np.linalg.norm([poly[2]-poly[0],poly[3]-poly[1]])

            print(fr'group_text_box height : {current_path} {height}')
            print(fr'group_text_box width : {current_path} {width}')


            margin = int(1.44*add_margin*min(width, height))

            theta13 = abs(np.arctan( (poly[1]-poly[5])/np.maximum(10, (poly[0]-poly[4]))))
            theta24 = abs(np.arctan( (poly[3]-poly[7])/np.maximum(10, (poly[2]-poly[6]))))

            print(fr'group_text_box margin : {current_path} {margin}')
            print(fr'group_text_box theta13 : {current_path} {theta13}')
            print(fr'group_text_box theta24 : {current_path} {theta24}')

            # do I need to clip minimum, maximum value here?
            x1 = poly[0] - np.cos(theta13)*margin
            y1 = poly[1] - np.sin(theta13)*margin
            x2 = poly[2] + np.cos(theta24)*margin
            y2 = poly[3] - np.sin(theta24)*margin
            x3 = poly[4] + np.cos(theta13)*margin
            y3 = poly[5] + np.sin(theta13)*margin
            x4 = poly[6] - np.cos(theta24)*margin
            y4 = poly[7] + np.sin(theta24)*margin

            print(fr'group_text_box x1 : {current_path} {x1}')
            print(fr'group_text_box y1 : {current_path} {y1}')
            print(fr'group_text_box x2 : {current_path} {x2}')
            print(fr'group_text_box y2 : {current_path} {y2}')
            print(fr'group_text_box x3 : {current_path} {x3}')
            print(fr'group_text_box y3 : {current_path} {y3}')
            print(fr'group_text_box x4 : {current_path} {x4}')
            print(fr'group_text_box y4 : {current_path} {y4}')

            free_list.append([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
            print(fr'group_text_box free_list : {current_path} {free_list}')

    print(fr'group_text_box sort_output : {current_path} {sort_output}')
    if sort_output:
        horizontal_list = sorted(horizontal_list, key=lambda item: item[4])
        print(fr'group_text_box horizontal_list : {current_path} {horizontal_list}')

    # combine box
    new_box = []
    for poly in horizontal_list:

        print(fr'group_text_box horizontal_list : {current_path} {horizontal_list}')
        print(fr'group_text_box poly : {current_path} {poly}')

        print(fr'group_text_box new_box : {current_path} {new_box}')
        print(fr'group_text_box len(new_box) : {current_path} {len(new_box)}')
        if len(new_box) == 0:
            b_height = [poly[5]]
            b_ycenter = [poly[4]]
            new_box.append(poly)

            print(fr'group_text_box b_height : {current_path} {b_height}')
            print(fr'group_text_box b_ycenter : {current_path} {b_ycenter}')
            print(fr'group_text_box new_box : {current_path} {new_box}')

        else:
            # comparable height and comparable y_center level up to ths*height
            if abs(np.mean(b_ycenter) - poly[4]) < ycenter_ths*np.mean(b_height):
                b_height.append(poly[5])
                b_ycenter.append(poly[4])
                new_box.append(poly)

                print(fr'group_text_box b_height len(new_box) == 0 아님 and < ycenter_ths*np.mean(b_height) : {current_path} {b_height}')
                print(fr'group_text_box b_ycenter  len(new_box) == 0 아님 and < ycenter_ths*np.mean(b_height) : {current_path} {b_ycenter}')
                print(fr'group_text_box new_box  len(new_box) == 0 아님 and < ycenter_ths*np.mean(b_height) : {current_path} {new_box}')

            else:
                b_height = [poly[5]]
                b_ycenter = [poly[4]]
                combined_list.append(new_box)
                new_box = [poly]

                print(
                    fr'group_text_box b_height len(new_box) == 0 아님 and >= ycenter_ths*np.mean(b_height) : {current_path} {b_height}')
                print(
                    fr'group_text_box b_ycenter  len(new_box) == 0 아님 and >= ycenter_ths*np.mean(b_height) : {current_path} {b_ycenter}')
                print(
                    fr'group_text_box new_box  len(new_box) == 0 아님 and >= ycenter_ths*np.mean(b_height) : {current_path} {new_box}')

    combined_list.append(new_box)

    print(fr'group_text_box new_box  combined_list : {current_path} {combined_list}')

    # merge list use sort again
    for boxes in combined_list:

        print(fr'group_text_box new_box  combined_list : {current_path} {combined_list}')
        print(fr'group_text_box new_box  boxes : {current_path} {boxes}')

        if len(boxes) == 1: # one box per line
            box = boxes[0]
            margin = int(add_margin*min(box[1]-box[0],box[5]))
            merged_list.append([box[0]-margin,box[1]+margin,box[2]-margin,box[3]+margin])

            print(fr'group_text_box new_box  len(boxes) : {current_path} {len(boxes)}')
            print(fr'group_text_box new_box  add_margin : {current_path} {add_margin}')
            print(fr'group_text_box new_box  margin : {current_path} {margin}')
            print(fr'group_text_box new_box  merged_list : {current_path} {merged_list}')

        else: # multiple boxes per line
            boxes = sorted(boxes, key=lambda item: item[0])

            print(fr'group_text_box new_box  len(boxes) : {current_path} {len(boxes)}')
            print(fr'group_text_box new_box  boxes : {current_path} {boxes}')


            merged_box, new_box = [],[]
            for box in boxes:

                print(fr'group_text_box new_box  boxes : {current_path} {boxes}')
                print(fr'group_text_box new_box  box : {current_path} {box}')

                print(fr'group_text_box new_box  len(new_box) : {current_path} {len(new_box)}')
                if len(new_box) == 0:
                    b_height = [box[5]]
                    x_max = box[1]
                    new_box.append(box)
                else:
                    if (abs(np.mean(b_height) - box[5]) < height_ths*np.mean(b_height)) and ((box[0]-x_max) < width_ths *(box[3]-box[2])): # merge boxes
                        b_height.append(box[5])
                        x_max = box[1]
                        new_box.append(box)

                        print(fr'group_text_box new_box  b_height : {current_path} {b_height}')
                        print(fr'group_text_box new_box  x_max : {current_path} {x_max}')
                        print(fr'group_text_box new_box  new_box : {current_path} {new_box}')
                    else:
                        b_height = [box[5]]
                        x_max = box[1]
                        merged_box.append(new_box)
                        new_box = [box]

                        print(fr'group_text_box new_box  b_height else : {current_path} {b_height}')
                        print(fr'group_text_box new_box  x_max else : {current_path} {x_max}')
                        print(fr'group_text_box new_box  merged_box else : {current_path} {merged_box}')
                        print(fr'group_text_box new_box  new_box else : {current_path} {new_box}')

            print(fr'group_text_box new_box  len(new_box) : {current_path} {len(new_box)}')
            if len(new_box) >0:
                merged_box.append(new_box)
                print(fr'group_text_box new_box  merged_box : {current_path} {merged_box}')

            for mbox in merged_box:

                print(fr'group_text_box new_box  merged_box : {current_path} {merged_box}')
                print(fr'group_text_box new_box  mbox : {current_path} {mbox}')

                if len(mbox) != 1: # adjacent box in same line
                    # do I need to add margin here?
                    x_min = min(mbox, key=lambda x: x[0])[0]
                    x_max = max(mbox, key=lambda x: x[1])[1]
                    y_min = min(mbox, key=lambda x: x[2])[2]
                    y_max = max(mbox, key=lambda x: x[3])[3]

                    print(fr'group_text_box new_box  x_min : {current_path} {x_min}')
                    print(fr'group_text_box new_box  x_max : {current_path} {x_max}')
                    print(fr'group_text_box new_box  y_min : {current_path} {y_min}')
                    print(fr'group_text_box new_box  y_max : {current_path} {y_max}')

                    box_width = x_max - x_min
                    box_height = y_max - y_min
                    margin = int(add_margin * (min(box_width, box_height)))

                    merged_list.append([x_min-margin, x_max+margin, y_min-margin, y_max+margin])

                    print(fr'group_text_box new_box  box_width : {current_path} {box_width}')
                    print(fr'group_text_box new_box  box_height : {current_path} {box_height}')
                    print(fr'group_text_box new_box  margin : {current_path} {margin}')
                    print(fr'group_text_box new_box  merged_list : {current_path} {merged_list}')

                else: # non adjacent box in same line
                    box = mbox[0]

                    box_width = box[1] - box[0]
                    box_height = box[3] - box[2]
                    margin = int(add_margin * (min(box_width, box_height)))

                    merged_list.append([box[0]-margin,box[1]+margin,box[2]-margin,box[3]+margin])

                    print(fr'group_text_box new_box  box non adjacent box in same line : {current_path} {box}')
                    print(fr'group_text_box new_box  box_width non adjacent box in same line : {current_path} {box_width}')
                    print(fr'group_text_box new_box  box_height non adjacent box in same line : {current_path} {box_height}')
                    print(fr'group_text_box new_box  merged_list non adjacent box in same line : {margin} {margin}')
                    print(fr'group_text_box new_box  merged_list non adjacent box in same line : {margin} {merged_list}')

    # may need to check if box is really in image

    print(fr'group_text_box new_box  merged_list may need to check if box is really in image : {current_path} {merged_list}')
    print(fr'group_text_box new_box  free_list may need to check if box is really in image : {current_path} {free_list}')

    return merged_list, free_list

def calculate_ratio(width,height):
    '''
    Calculate aspect ratio for normal use case (w>h) and vertical text (h>w)
    '''
    ratio = width/height
    if ratio<1.0:
        ratio = 1./ratio
    return ratio

def compute_ratio_and_resize(img,width,height,model_height):

    print(fr'compute_ratio_and_resize width : {current_path} {width}')
    print(fr'compute_ratio_and_resize height : {current_path} {height}')
    print(fr'compute_ratio_and_resize model_height : {current_path} {model_height}')

    '''
    Calculate ratio and resize correctly for both horizontal text
    and vertical case
    '''
    ratio = width/height

    print(fr'compute_ratio_and_resize ratio : {current_path} {ratio}')
    from PIL import Image, JpegImagePlugin
    if ratio<1.0:
        ratio = calculate_ratio(width,height)
        img = cv2.resize(img,(model_height,int(model_height*ratio)), interpolation=Image.Resampling.LANCZOS)
    else:
        img = cv2.resize(img,(int(model_height*ratio),model_height),interpolation=Image.Resampling.LANCZOS)

        #import cv2

        # 이미지 저장 경로
        save_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\th\log\crop.jpg'

        # 이미지를 저장할 변수
        crop_image = img

        # 이미지 저장
        cv2.imwrite(save_path, crop_image)


        #import cv2
        # from PIL import Image
        # from matplotlib import pyplot as plt
        #
        # # 이미지를 resize
        # resized_img = cv2.resize(img, (int(model_height * ratio), model_height), interpolation=cv2.INTER_LANCZOS4)
        #
        # # PIL 이미지로 변환
        # resized_img_pil = Image.fromarray(resized_img)
        #
        # # 이미지 표시
        # plt.imshow(resized_img_pil)
        # #plt.title('Resized Image')
        # plt.show()



    return img,ratio


def get_image_list(horizontal_list, free_list, img, model_height = 64, sort_output = True):
    image_list = []
    maximum_y,maximum_x = img.shape

    print(fr'get_image_list maximum_y : {current_path} {maximum_y}')
    print(fr'get_image_list maximum_x : {current_path} {maximum_x}')
    print(fr'get_image_list model_height : {current_path} {model_height}')

    max_ratio_hori, max_ratio_free = 1,1
    for box in free_list:
        rect = np.array(box, dtype = "float32")
        transformed_img = four_point_transform(img, rect)
        ratio = calculate_ratio(transformed_img.shape[1],transformed_img.shape[0])



        print(fr'get_image_list model_height : {current_path} {model_height}')
        print(fr'get_image_list ratio : {current_path} {ratio}')
        print(fr'get_image_list model_height : {current_path} {model_height}')
        print(fr'get_image_list ratio : {current_path} {ratio}')

        print(fr'get_image_list model_height : {current_path} {model_height}')
        print(fr'get_image_list ratio : {current_path} {ratio}')

        new_width = int(model_height*ratio)
        if new_width == 0:
            pass
        else:
            crop_img,ratio = compute_ratio_and_resize(transformed_img,transformed_img.shape[1],transformed_img.shape[0],model_height)
            image_list.append( (box,crop_img) ) # box = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
            max_ratio_free = max(ratio, max_ratio_free)


    max_ratio_free = math.ceil(max_ratio_free)

    print(fr'horizontal_list : {current_path} {horizontal_list}')

    for box in horizontal_list:

        print(fr'box : {current_path} {box}')

        x_min = max(0,box[0])
        x_max = min(box[1],maximum_x)
        y_min = max(0,box[2])
        y_max = min(box[3],maximum_y)

        print(fr'get_image_list box : {current_path} {box}')
        print(fr'get_image_list box[0] : {current_path} {box[0]}')
        print(fr'get_image_list box[1] : {current_path} {box[1]}')
        print(fr'get_image_list box[2] : {current_path} {box[2]}')
        print(fr'get_image_list box[3] : {current_path} {box[3]}')


        print(fr'x_min : {current_path} {x_min}')
        print(fr'x_max : {current_path} {x_max}')
        print(fr'y_min : {current_path} {y_min}')
        print(fr'y_max : {current_path} {y_max}')

        crop_img = img[y_min : y_max, x_min:x_max]

        import cv2
        # from PIL import Image
        # from matplotlib import pyplot as plt
        #
        # # crop_img를 PIL 이미지로 변환
        # crop_img_pil = Image.fromarray(crop_img)
        #
        # # crop_img와 원본 이미지를 matplotlib를 사용하여 함께 표시
        # fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        # ax[0].imshow(crop_img_pil)
        # ax[0].set_title('Cropped Image')
        # ax[1].imshow(crop_img)
        # ax[1].set_title('Original Image')
        # plt.show()



        width = x_max - x_min
        height = y_max - y_min
        ratio = calculate_ratio(width,height)
        new_width = int(model_height*ratio)
        #new_width = 282

        # x_min = max(0, box[0])
        # x_max = min(box[1], maximum_x)
        # y_min = max(0, box[2])
        # y_max = min(box[3], maximum_y)
        # box :      [3, 271, 0, 117]
        # maximum_y, maximum_x = img.shape
        # maximum_y: 114
        # maximum_x: 282

        print(fr'get_image_list x_max : {current_path} {x_max}')
        print(fr'get_image_list x_min : {current_path} {x_min}')
        print(fr'get_image_list y_max : {current_path} {y_max}')
        print(fr'get_image_list y_min : {current_path} {y_min}')

        print(fr'get_image_list width x_max - x_min = {x_max} - {x_min} : {current_path} {width}')
        print(fr'get_image_list height y_max - y_min = {y_max} - {y_min} : {current_path} {height}')
        print(fr'get_image_list ratio calculate_ratio(width,height)  = {calculate_ratio(width,height)} : {current_path} {ratio}')
        print(fr'get_image_list model_height = {model_height} : {current_path} {model_height}')
        print(fr'get_image_list new_width int(model_height*ratio) = int({ model_height} * {ratio}) : {current_path} {new_width}')

        if new_width == 0:
            pass
        else:
            crop_img,ratio = compute_ratio_and_resize(crop_img,width,height,model_height)
            image_list.append( ( [[x_min,y_min],[x_max,y_min],[x_max,y_max],[x_min,y_max]] ,crop_img) )
            max_ratio_hori = max(ratio, max_ratio_hori)

            print(fr'get_image_list crop_img : {current_path} {crop_img}')
            print(fr'get_image_list ratio : {current_path} {ratio}')
            print(fr'get_image_list image_list : {current_path} {image_list}')
            print(fr'get_image_list max_ratio_hori : {current_path} {max_ratio_hori}')

            # 이미지 리스트 순회하며 이미지와 바운딩 박스 정보 추출
            for bounding_box, image_data in image_list:
                # 이미지 데이터를 넘파이 배열로 변환
                image_np = np.array(image_data)

                # 바운딩 박스 정보 추출
                x_min, y_min = bounding_box[0]
                x_max, y_max = bounding_box[2]

                # 이미지 저장 경로
                #save_path = "C:/Users/TAMSystech/yjh/ipynb/deep-text-recognition-benchmark/data/th/test/0318"
                save_path = "C:/Users/TAMSystech/yjh/ipynb/deep-text-recognition-benchmark/data/th/test/0318"

                # 이미지 저장
                cv2.imwrite(f"{save_path}/image.jpg", image_np)

                print(fr' 이미지 저장 완료!!!!!!!!!!!!!! get_image_list save_path : {current_path} {save_path}')

    max_ratio_hori = math.ceil(max_ratio_hori)
    max_ratio = max(max_ratio_hori, max_ratio_free)
    max_width = math.ceil(max_ratio)*model_height

    print(fr'max_ratio_hori : {current_path} {max_ratio_hori}')
    print(fr'max_ratio : {current_path} {max_ratio}')
    print(fr'max_width : {current_path} {max_width}')

    print(fr'sort_output : {current_path} {sort_output}')

    if sort_output:
        image_list = sorted(image_list, key=lambda item: item[0][0][1]) # sort by vertical position

    print(fr'get_image_list image_list : {current_path} {image_list}')
    print(fr'get_image_listmax_width : {current_path} {max_width}')

    ##############################

    import cv2
    import os

    # 저장할 디렉토리 경로
    save_dir = "C:/Users/TAMSystech/yjh/ipynb/deep-text-recognition-benchmark/data/th/test/0319/train/img"

    # 디렉토리가 없으면 생성
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 이미지를 저장하기 전에 UMat 형식인 경우에만 NumPy 배열로 변환하여 저장
    for i, image in enumerate(image_list):
        if isinstance(image, cv2.UMat):
            print(fr'UMat 이 무야 ')
            image = image.get()
        image_path = os.path.join(save_dir, f"image_{i}.jpg")
        try:
            cv2.imwrite(image_path, image)
        except Exception as e:
            print(f"이미지 저장 중 오류 발생: {e}")

    print("이미지 저장이 완료되었습니다.")

    print("이미지 저장이 완료되었습니다.")

    ##############################

    return image_list, max_width

def download_and_unzip(url, filename, model_storage_directory, verbose=True):
    zip_path = os.path.join(model_storage_directory, 'temp.zip')
    reporthook = printProgressBar(prefix='Progress:', suffix='Complete', length=50) if verbose else None
    urlretrieve(url, zip_path, reporthook=reporthook)
    with ZipFile(zip_path, 'r') as zipObj:
        zipObj.extract(filename, model_storage_directory)
    os.remove(zip_path)

def calculate_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def diff(input_list):
    return max(input_list)-min(input_list)

def get_paragraph(raw_result, x_ths=1, y_ths=0.5, mode = 'ltr'):
    # create basic attributes
    box_group = []
    for box in raw_result:
        all_x = [int(coord[0]) for coord in box[0]]
        all_y = [int(coord[1]) for coord in box[0]]
        min_x = min(all_x)
        max_x = max(all_x)
        min_y = min(all_y)
        max_y = max(all_y)
        height = max_y - min_y
        box_group.append([box[1], min_x, max_x, min_y, max_y, height, 0.5*(min_y+max_y), 0]) # last element indicates group
    # cluster boxes into paragraph
    current_group = 1
    while len([box for box in box_group if box[7]==0]) > 0:
        box_group0 = [box for box in box_group if box[7]==0] # group0 = non-group
        # new group
        if len([box for box in box_group if box[7]==current_group]) == 0:
            box_group0[0][7] = current_group # assign first box to form new group
        # try to add group
        else:
            current_box_group = [box for box in box_group if box[7]==current_group]
            mean_height = np.mean([box[5] for box in current_box_group])
            min_gx = min([box[1] for box in current_box_group]) - x_ths*mean_height
            max_gx = max([box[2] for box in current_box_group]) + x_ths*mean_height
            min_gy = min([box[3] for box in current_box_group]) - y_ths*mean_height
            max_gy = max([box[4] for box in current_box_group]) + y_ths*mean_height
            add_box = False
            for box in box_group0:
                same_horizontal_level = (min_gx<=box[1]<=max_gx) or (min_gx<=box[2]<=max_gx)
                same_vertical_level = (min_gy<=box[3]<=max_gy) or (min_gy<=box[4]<=max_gy)
                if same_horizontal_level and same_vertical_level:
                    box[7] = current_group
                    add_box = True
                    break
            # cannot add more box, go to next group
            if add_box==False:
                current_group += 1
    # arrage order in paragraph
    result = []
    for i in set(box[7] for box in box_group):
        current_box_group = [box for box in box_group if box[7]==i]
        mean_height = np.mean([box[5] for box in current_box_group])
        min_gx = min([box[1] for box in current_box_group])
        max_gx = max([box[2] for box in current_box_group])
        min_gy = min([box[3] for box in current_box_group])
        max_gy = max([box[4] for box in current_box_group])

        text = ''
        while len(current_box_group) > 0:
            highest = min([box[6] for box in current_box_group])
            candidates = [box for box in current_box_group if box[6]<highest+0.4*mean_height]
            # get the far left
            if mode == 'ltr':
                most_left = min([box[1] for box in candidates])
                for box in candidates:
                    if box[1] == most_left: best_box = box
            elif mode == 'rtl':
                most_right = max([box[2] for box in candidates])
                for box in candidates:
                    if box[2] == most_right: best_box = box
            text += ' '+best_box[0]
            current_box_group.remove(best_box)

        result.append([ [[min_gx,min_gy],[max_gx,min_gy],[max_gx,max_gy],[min_gx,max_gy]], text[1:]])

    return result


def printProgressBar(prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    def progress_hook(count, blockSize, totalSize):
        progress = count * blockSize / totalSize
        percent = ("{0:." + str(decimals) + "f}").format(progress * 100)
        filledLength = int(length * progress)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='')

    return progress_hook

def reformat_input(image):
    if type(image) == str:
        if image.startswith('http://') or image.startswith('https://'):
            tmp, _ = urlretrieve(image , reporthook=printProgressBar(prefix = 'Progress:', suffix = 'Complete', length = 50))
            img_cv_grey = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
            os.remove(tmp)
        else:
            img_cv_grey = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            image = os.path.expanduser(image)
        img = loadImage(image)  # can accept URL
    elif type(image) == bytes:
        nparr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_cv_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    elif type(image) == np.ndarray:
        if len(image.shape) == 2: # grayscale
            img_cv_grey = image
            img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            print(fr' type(img) : {current_path} {type(img)}')

            from PIL import Image
            #import cv2

            # OpenCV 이미지를 PIL 이미지로 변환
            pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # 이미지 표시
            pil_image.show()



        elif len(image.shape) == 3 and image.shape[2] == 1:
            img_cv_grey = np.squeeze(image)
            img = cv2.cvtColor(img_cv_grey, cv2.COLOR_GRAY2BGR)
        elif len(image.shape) == 3 and image.shape[2] == 3: # BGRscale
            img = image
            img_cv_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif len(image.shape) == 3 and image.shape[2] == 4: # RGBAscale
            img = image[:,:,:3]
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img_cv_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif type(image) == JpegImagePlugin.JpegImageFile:
        image_array = np.array(image)
        img = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
        img_cv_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        raise ValueError('Invalid input type. Supporting format = string(file path or url), bytes, numpy array')

    return img, img_cv_grey


def reformat_input_batched(image, n_width=None, n_height=None):
    """
    reformats an image or list of images or a 4D numpy image array &
    returns a list of corresponding img, img_cv_grey nd.arrays
    image:
        [file path, numpy-array, byte stream object,
        list of file paths, list of numpy-array, 4D numpy array,
        list of byte stream objects]
    """
    if ((isinstance(image, np.ndarray) and len(image.shape) == 4) or isinstance(image, list)):
        # process image batches if image is list of image np arr, paths, bytes
        img, img_cv_grey = [], []
        for single_img in image:
            clr, gry = reformat_input(single_img)
            if n_width is not None and n_height is not None:
                clr = cv2.resize(clr, (n_width, n_height))
                gry = cv2.resize(gry, (n_width, n_height))
            img.append(clr)
            img_cv_grey.append(gry)
        img, img_cv_grey = np.array(img), np.array(img_cv_grey)
        # ragged tensors created when all input imgs are not of the same size
        if len(img.shape) == 1 and len(img_cv_grey.shape) == 1:
            raise ValueError("The input image array contains images of different sizes. " +
                             "Please resize all images to same shape or pass n_width, n_height to auto-resize")
    else:
        img, img_cv_grey = reformat_input(image)
    return img, img_cv_grey



def make_rotated_img_list(rotationInfo, img_list):

    result_img_list = img_list[:]

    # add rotated images to original image_list
    max_ratio=1
    
    for angle in rotationInfo:
        for img_info in img_list : 
            rotated = ndimage.rotate(img_info[1], angle, reshape=True) 
            height,width = rotated.shape
            ratio = calculate_ratio(width,height)
            max_ratio = max(max_ratio,ratio)
            result_img_list.append((img_info[0], rotated))
    return result_img_list


def set_result_with_confidence(results):
    """ Select highest confidence augmentation for TTA
    Given a list of lists of results (outer list has one list per augmentation,
    inner lists index the images being recognized), choose the best result 
    according to confidence level.
    Each "result" is of the form (box coords, text, confidence)
    A final_result is returned which contains one result for each image
    """
    final_result = []
    for col_ix in range(len(results[0])):
        # Take the row_ix associated with the max confidence
        best_row = max(
            [(row_ix, results[row_ix][col_ix][2]) for row_ix in range(len(results))],
            key=lambda x: x[1])[0]
        final_result.append(results[best_row][col_ix])

    return final_result
