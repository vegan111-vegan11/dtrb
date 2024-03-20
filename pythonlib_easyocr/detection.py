import torch
import torch.backends.cudnn as cudnn
from torch.autograd import Variable
from PIL import Image
from collections import OrderedDict

import cv2
import numpy as np
from .craft_utils import getDetBoxes, adjustResultCoordinates
from .imgproc import resize_aspect_ratio, normalizeMeanVariance
from .craft import CRAFT
import os

current_path = os.path.abspath(__file__)

def copyStateDict(state_dict):
    if list(state_dict.keys())[0].startswith("module"):
        start_idx = 1
    else:
        start_idx = 0
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = ".".join(k.split(".")[start_idx:])
        new_state_dict[name] = v
    return new_state_dict

def test_net(canvas_size, mag_ratio, net, image, text_threshold, link_threshold, low_text, poly, device, estimate_num_chars=False):

    print(fr'test_net canvas_size : {canvas_size} {canvas_size}')
    print(fr'test_net mag_ratio : {canvas_size} {mag_ratio}')
    print(fr'test_net net : {canvas_size} {net}')
    print(fr'test_net text_threshold : {canvas_size} {text_threshold}')
    print(fr'test_net link_threshold : {canvas_size} {link_threshold}')
    print(fr'test_net low_text : {canvas_size} {low_text}')
    print(fr'test_net poly : {canvas_size} {poly}')
    print(fr'test_net device : {canvas_size} {device}')

    if isinstance(image, np.ndarray) and len(image.shape) == 4:  # image is batch of np arrays
        image_arrs = image
    else:                                                        # image is single numpy array
        image_arrs = [image]

    #print(fr'test_net image_arrs : {canvas_size} {image_arrs}')

    img_resized_list = []
    # resize
    for img in image_arrs:
        img_resized, target_ratio, size_heatmap = resize_aspect_ratio(img, canvas_size,
                                                                      interpolation=cv2.INTER_LINEAR,
                                                                      mag_ratio=mag_ratio)

        print(fr'test_net img_resized : {canvas_size} {img_resized}')
        print(fr'test_net target_ratio : {canvas_size} {target_ratio}')
        print(fr'test_net size_heatmap : {canvas_size} {size_heatmap}')

        img_resized_list.append(img_resized)
    ratio_h = ratio_w = 1 / target_ratio

    print(fr'test_net ratio_w : {canvas_size} {ratio_w}')
    print(fr'test_net target_ratio : {canvas_size} {target_ratio}')
    print(fr'test_net ratio_h : {canvas_size} {ratio_h}')


    # preprocessing
    x = [np.transpose(normalizeMeanVariance(n_img), (2, 0, 1))
         for n_img in img_resized_list]
    #print(fr'test_net x : {canvas_size} {x}')
    x = torch.from_numpy(np.array(x))
    #print(fr'test_net x : {canvas_size} {x}')
    x = x.to(device)
    #print(fr'test_net x : {canvas_size} {x}')

    # forward pass
    with torch.no_grad():
        y, feature = net(x)
        #print(fr'test_net y : {canvas_size} {y}')
        #print(fr'test_net feature : {canvas_size} {feature}')

    boxes_list, polys_list = [], []
    for out in y:

        #print(fr'test_net y : {canvas_size} {y}')
        #print(fr'test_net out : {canvas_size} {out}')

        # make score and link map
        score_text = out[:, :, 0].cpu().data.numpy()
        score_link = out[:, :, 1].cpu().data.numpy()

        #print(fr'test_net score_text : {canvas_size} {score_text}')
        #print(fr'test_net score_link : {canvas_size} {score_link}')

        # Post-processing
        boxes, polys, mapper = getDetBoxes(
            score_text, score_link, text_threshold, link_threshold, low_text, poly, estimate_num_chars)

        print(fr'test_net boxes : {canvas_size} {boxes}')
        print(fr'test_net polys : {canvas_size} {polys}')
        print(fr'test_net mapper : {canvas_size} {mapper}')

        # coordinate adjustment
        boxes = adjustResultCoordinates(boxes, ratio_w, ratio_h)
        polys = adjustResultCoordinates(polys, ratio_w, ratio_h)

        print(fr'test_net boxes : {canvas_size} {boxes}')
        print(fr'test_net polys : {canvas_size} {polys}')
        print(fr'test_net estimate_num_chars : {canvas_size} {estimate_num_chars}')


        if estimate_num_chars:
            boxes = list(boxes)
            polys = list(polys)

            print(fr'test_net boxes : {canvas_size} {boxes}')
            print(fr'test_net polys : {canvas_size} {polys}')

        for k in range(len(polys)):

            print(fr'test_net len(polys) : {canvas_size} {len(polys)}')
            print(fr'test_net k : {canvas_size} {k}')

            print(fr'test_net estimate_num_chars : {canvas_size} {estimate_num_chars}')

            if estimate_num_chars:
                boxes[k] = (boxes[k], mapper[k])
                print(fr'test_netboxes[k] : {canvas_size} {boxes[k]}')

            print(fr'test_netboxes[k] : {canvas_size} {boxes[k]}')
            if polys[k] is None:
                polys[k] = boxes[k]

                print(fr'test_net polys[k] : {canvas_size} {polys[k]}')

        boxes_list.append(boxes)
        polys_list.append(polys)

        print(fr'test_net boxes_list : {canvas_size} {boxes_list}')
        print(fr'test_net polys_list : {canvas_size} {polys_list}')

    return boxes_list, polys_list

def get_detector(trained_model, device='cpu', quantize=True, cudnn_benchmark=False):
    net = CRAFT()

    if device == 'cpu':
        net.load_state_dict(copyStateDict(torch.load(trained_model, map_location=device)))
        if quantize:
            try:
                torch.quantization.quantize_dynamic(net, dtype=torch.qint8, inplace=True)
            except:
                pass
    else:
        net.load_state_dict(copyStateDict(torch.load(trained_model, map_location=device)))
        net = torch.nn.DataParallel(net).to(device)
        cudnn.benchmark = cudnn_benchmark

    net.eval()
    return net

def get_textbox(detector, image, canvas_size, mag_ratio, text_threshold, link_threshold, low_text, poly, device, optimal_num_chars=None, **kwargs):
    result = []
    estimate_num_chars = optimal_num_chars is not None
    bboxes_list, polys_list = test_net(canvas_size, mag_ratio, detector,
                                       image, text_threshold,
                                       link_threshold, low_text, poly,
                                       device, estimate_num_chars)

    print(fr'get_textbox bboxes_list : {current_path} {bboxes_list} ')
    print(fr'get_textbox polys_list : {current_path} {polys_list} ')

    #print(f'detection.py bboxes_list : {bboxes_list}')
    print(fr'get_textbox estimate_num_chars : {current_path} {estimate_num_chars} ')

    if estimate_num_chars:
        polys_list = [[p for p, _ in sorted(polys, key=lambda x: abs(optimal_num_chars - x[1]))]
                      for polys in polys_list]

    for polys in polys_list:

        print(fr'get_textbox polys_list : {current_path} {polys_list} ')
        print(fr'get_textbox polys : {current_path} {polys} ')

        single_img_result = []
        for i, box in enumerate(polys):

            print(fr'get_textbox polys : {current_path} {polys} ')
            print(fr'get_textbox i : {current_path} {i} ')
            print(fr'get_textbox box : {current_path} {box} ')

            poly = np.array(box).astype(np.int32).reshape((-1))
            single_img_result.append(poly)

            print(fr'get_textbox poly : {current_path} {poly} ')
            print(fr'get_textbox single_img_result : {current_path} {single_img_result} ')

        result.append(single_img_result)

        print(fr'get_textbox result : {current_path} {result} ')

    print(fr'get_textbox result : {current_path} {result} ')

    return result
