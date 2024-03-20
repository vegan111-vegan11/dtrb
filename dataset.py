import os
import sys
import re
import six
import math
import lmdb
import torch

from natsort import natsorted
from PIL import Image
import numpy as np
from torch.utils.data import Dataset, ConcatDataset, Subset
from torch._utils import _accumulate
import torchvision.transforms as transforms
import datetime
import random
lan = 'pt'
lan = 'ko'
lan = 'en'
lan = 'th'
get_batch_cnt = 0
class Batch_Balanced_Dataset(object):

    def __init__(self, opt):
        """
        Modulate the data ratio in the batch.
        For example, when select_data is "MJ-ST" and batch_ratio is "0.5-0.5",
        the 50% of the batch is filled with MJ and the other 50% of the batch is filled with ST.
        """

        current_date = datetime.datetime.now().strftime("%m-%d")
        #print(f'dataset 파일 current_date {current_date}')

        # 원하는 폴더 경로 생성
        directory = f'./saved_models/{opt.exp_name}/{current_date}/'

        # 폴더가 존재하지 않으면 생성
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 파일 열기
        #log = open(f'{directory}/log_dataset.txt', 'a')
        log = open(f'{directory}/log_dataset.txt', 'a', encoding='utf-8')

        #log = open(f'./saved_models/{opt.exp_name}/{current_date}/log_dataset.txt', 'a')
        # 로그용
        print(f'dataset 파일 log : {log}')

        dashed_line = '-' * 80
        print(dashed_line)
        log.write(dashed_line + '\n')
        # 로그용

        # print(f'Batch_Balanced_Dataset  이닛 opt  : {opt}')
        # print(f'Batch_Balanced_Dataset  이닛 opt.character : {opt.character}')
        # 로그용
        # if 'ๆ' in opt.character:
        #     # 'ๆ' 문자가 있을 경우
        #     print('Batch_Balanced_Dataset  이닛 opt.character 있음')
        # else:
        #     # 'ๆ' 문자가 없을 경우
        #     print('Batch_Balanced_Dataset  이닛 opt.character 없음')
        # 로그용
        # print(
        #     f'Batch_Balanced_Dataset dataset_root: {opt.train_data}\nopt.select_data: {opt.select_data}\nopt.batch_ratio: {opt.batch_ratio}')
        # print(
        #     f'Batch_Balanced_Dataset dataset_root: {opt.train_data}\nopt.select_data: {opt.select_data}\nopt.batch_ratio: {opt.batch_ratio}')
        log.write(
            f'Batch_Balanced_Dataset dataset_root: {opt.train_data}\nopt.select_data: {opt.select_data}\nopt.batch_ratio: {opt.batch_ratio}\n')
        assert len(opt.select_data) == len(opt.batch_ratio)

        _AlignCollate = AlignCollate(imgH=opt.imgH, imgW=opt.imgW, keep_ratio_with_pad=opt.PAD)
        self.data_loader_list = []
        self.dataloader_iter_list = []
        batch_size_list = []
        Total_batch_size = 0

        # 로그용
        #print(f'@@@@@@@@@@Batch_Balanced_Dataset 태국어도 학습하라고    opt.select_data : {opt.select_data}')

        for selected_d, batch_ratio_d in zip(opt.select_data, opt.batch_ratio):
            print(f'Batch_Balanced_Dataset select_data 반복 selected_d : {selected_d}')
            _batch_size = max(round(opt.batch_size * float(batch_ratio_d)), 1)

            # 로그용
            print(f'opt.batch_size : {opt.batch_size}')
            print(f'opt.batch_ratio : {opt.batch_ratio}')

            print(f'opt.select_data : {opt.select_data}')

            print(f'배치사이즈가 디렉토리마다 다르게 계산됨 ( batch_size * batch_ratio_d ) _batch_size : {_batch_size}')


            print(dashed_line)
            log.write(dashed_line + '\n')
            # print("읽히라고  ")
            # 로그용
            #print(f'Batch_Balanced_Dataset opt.train_data : {opt.train_data}')

            # if 'ๆ' in opt.character:
            #     # 'ๆ' 문자가 있을 경우
            #     print('dataset.py Batch_Balanced_Dataset ๆ 있음')
            # else:
            #     # 'ๆ' 문자가 없을 경우
            #     print('dataset.py Batch_Balanced_Dataset ๆ 없음')

            print(f'Batch_Balanced_Dataset [selected_d] : {[selected_d]}')

            _dataset, _dataset_log = hierarchical_dataset(root=opt.train_data, opt=opt, select_data=[selected_d])
            # 로그용
            # print(f'Batch_Balanced_Dataset _dataset : {_dataset}')
            # print(f'Batch_Balanced_Dataset _dataset_log : {_dataset_log}')
            # print(f'Batch_Balanced_Dataset opt.train_data : {opt.train_data}')
            # print(f'!Batch_Balanced_Dataset 이닛 opt : {opt}')
            total_number_dataset = len(_dataset)
            log.write(_dataset_log)
            # 로그용
            #print(f'dataset.py  _dataset_log : {_dataset_log}')
            print(f'dataset.py total_number_dataset : {total_number_dataset}')
            """
            The total number of data can be modified with opt.total_data_usage_ratio.
            ex) opt.total_data_usage_ratio = 1 indicates 100% usage, and 0.2 indicates 20% usage.
            See 4.2 section in our paper.
            """
            number_dataset = int(total_number_dataset * float(opt.total_data_usage_ratio))
            print(f'total_number_dataset : {total_number_dataset}')
            print(f'opt.total_data_usage_ratio : {opt.total_data_usage_ratio}')
            print(f'number_dataset : {number_dataset}')

            dataset_split = [number_dataset, total_number_dataset - number_dataset]
            # 원본
            #indices = range(total_number_dataset)

            # 긴문장을 주로 학습 시키기 위해서 일단 바꿈 ( 나중엔 셔플로 변경 예정 )
            # indices = range(total_number_dataset)
            # reversed_indices = indices[::-1]
            # indices = reversed_indices


            # 로그용
            #print(f'indices  range(total_number_dataset) : {indices}')
            #print(f'reversed_indices : {reversed_indices}')
            # for index in reversed_indices:
            #     print(f'reversed_indices index : {index}')

            # 리스트를 셔플
            indices = list(range(total_number_dataset))
            random.shuffle(indices)
            shuffle_indices = indices
            indices = shuffle_indices
            # 로그용
            # print(f'dataset.py shuffle_indices : {shuffle_indices}')
            # print(f'dataset.py dataset_split : {dataset_split}')
            # print(f'dataset.py zip(_accumulate(dataset_split), dataset_split) : {zip(_accumulate(dataset_split), dataset_split)}')

            # 로그용 ( offset )
            for offset, length in zip(_accumulate(dataset_split), dataset_split):
                #print(f"Subset Offset: {offset}, Length: {length}")
                subset = Subset(_dataset, indices[offset - length:offset])
                #print(f"Subset subset: {subset} ")
                # 여기에서 subset을 사용하여 작업 수행

            # _dataset, _ = [Subset(_dataset, indices[offset - length : offset])
            #                for offset, length in zip(_accumulate(dataset_split), dataset_split)]

            # _dataset : total_data_usage_ratio 만큼의 데이터
            # _not_usage_dataset : total_data_usage_ratio 만큼의 데이터를 제외한 나머지 Subset 데이터
            # 만약 처음에는 짧은 문장이 많고 뒷부분에 긴 문장이 있다면, _dataset에는 주로 짧은 문장만 포함
            _dataset, _not_usage_dataset = [Subset(_dataset, indices[offset - length : offset])
                           for offset, length in zip(_accumulate(dataset_split), dataset_split)]

            # 출력 예시 ( opt.total_data_usage_ratio = 0.2 일 경우 )
            # _dataset: [1, 2]
            # _not_usage_dataset : [3, 4, 5, 6, 7, 8, 9, 10]

            # 로그용
            # print(f" _dataset: {_dataset} ")
            # print(f"a: {_not_usage_dataset} ")
            # print(f"len(_dataset): {len(_dataset)} ")
            # print(f"len(a): {len(_not_usage_dataset)} ")
            # print(f"type(_dataset): {type(_dataset)} ")

            selected_d_log = f'num total samples of {selected_d}: {total_number_dataset} x {opt.total_data_usage_ratio} (total_data_usage_ratio) = {len(_dataset)}\n'
            selected_d_log += f'num samples of {selected_d} per batch: {opt.batch_size} x {float(batch_ratio_d)} (batch_ratio) = {_batch_size}'
            print(selected_d_log)
            log.write(selected_d_log + '\n')
            batch_size_list.append(str(_batch_size))
            Total_batch_size += _batch_size

            # 로그용
            print(f'dataset.py _batch_size : {_batch_size}')
            # print(f'dataset.py batch_size_list : {batch_size_list}')
            # print(f'dataset.py Total_batch_size : {Total_batch_size}')

            # print( '@@@@@@@@@@@이제 데이터 로더가 안돼   ')
            # print(f'@@@@@@@@@@@@@@@@@이제 데이터 로더가 안돼 opt.workers : {opt.workers}')

            # _AlignCollate 함수 ( 이미지 크기 조절 ( 전처리 ) 및 텍스트 패딩 적용 ( 모델 인풋에 전달할 텐서 생성 ) )
            # 데이터셋으로부터 불러온 각각의 샘플을 정렬하고 패딩(padding)하는 등의 전처리를 수행하여 배치를 생성
            _data_loader = torch.utils.data.DataLoader(
                _dataset, batch_size=_batch_size,
                shuffle=True,
                num_workers=int(opt.workers),
                collate_fn=_AlignCollate, pin_memory=True)
            self.data_loader_list.append(_data_loader)
            self.dataloader_iter_list.append(iter(_data_loader))
            # 로그용
            #print(f'%%%%%%%%%%%%%%%%%% len dataloader_iter_list : {len(self.dataloader_iter_list)}')

        Total_batch_size_log = f'{dashed_line}\n'
        batch_size_sum = '+'.join(batch_size_list)
        Total_batch_size_log += f'Total_batch_size: {batch_size_sum} = {Total_batch_size}\n'
        Total_batch_size_log += f'{dashed_line}'
        opt.batch_size = Total_batch_size

        # 로그용
        #print(f'batch_size_list : {batch_size_list}')


        #print(Total_batch_size_log)
        # 로그용
        # print(f'batch_size_sum : {batch_size_sum}')
        # print(f'opt.batch_size : {opt.batch_size}')
        # print(f'Total_batch_size : {Total_batch_size}')
        #
        # print(f'Total_batch_size_log : {Total_batch_size_log}')
        log.write(Total_batch_size_log + '\n')
        log.close()

    #balanced_batch_texts = []

    def get_batch(self):
        balanced_batch_images = []
        balanced_batch_texts = []
        dataloader_iter_list_cnt = 0

        # print(f'$$$$$$$$$$$$$$$$$$$$$ dataloader_iter_list 길이 : {len(dataloader_iter_list)}')
        #get_batch_cnt = get_batch_cnt +1
        print(f'get_batch_cnt : {get_batch_cnt}')
        #print(f'get_batch self.dataloader_iter_list : {self.dataloader_iter_list}')
        for i, data_loader_iter in enumerate(self.dataloader_iter_list):
            print(f'get_batch i : {i}')
            dataloader_iter_list_cnt = dataloader_iter_list_cnt + 1
            print(f'get_batch for 반복 dataloader_iter_list dataloader_iter_list_cnt : {dataloader_iter_list_cnt}')
            try:
                image, text = next(data_loader_iter)
                #print(f'get_batch  next(data_loader_iter) text : {text}')
                balanced_batch_images.append(image)
                balanced_batch_texts += text
                #print(f'get_batch  enumerate next(data_loader_iter) balanced_batch_texts : {balanced_batch_texts}')
                print(f'get_batch  enumerate next(data_loader_iter) balanced_batch_texts len: {len(balanced_batch_texts)}')


            except StopIteration:
                self.dataloader_iter_list[i] = iter(self.data_loader_list[i])
                image, text = next(self.dataloader_iter_list[i])
                balanced_batch_images.append(image)
                balanced_batch_texts += text
            except ValueError:
                pass
        print(f'get_batch dataloader_iter_list 반복 완료 get_batch_cnt : {get_batch_cnt}')

        #print(f'get_batch dataloader_iter_list 반복 완료 get_batch_cnt : {get_batch_cnt}')

        balanced_batch_images = torch.cat(balanced_batch_images, 0)
        #print(f'!get_batch 반환전 balanced_batch_images : {balanced_batch_images}')
        # 로그용
        print(f'!dataset.py get_batch len(balanced_batch_images) : {len(balanced_batch_images)}')
        #print(f'!get_batch 반환전 balanced_batch_texts : {balanced_batch_texts}')
        # 로그용
        print(f'!dataset.py len(balanced_batch_texts) : {len(balanced_batch_texts)}')
        return balanced_batch_images, balanced_batch_texts


# def hierarchical_dataset(root, opt, select_data='/'):
def hierarchical_dataset(root, opt, select_data=''):
    """ select_data='/' contains all sub-directory of root directory """
    dataset_list = []

    selected_d = 'th'
    selected_d = 'vi'
    selected_d = 'es'
    selected_d = lan

    select_data=[selected_d]

    print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ dataset.py hierarchical_dataset root : {root}')
    print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ dataset.py hierarchical_dataset select_data : {select_data}')
    print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ dataset.py hierarchical_dataset select_data[0] : {select_data[0]}')

    dataset_log = f'dataset_root:    {root}\t dataset: {select_data[0]}'
    print(dataset_log)
    # 로그용
    # print(f'dataset.py hierarchical_dataset root : {root}')
    # print(f'dataset.py hierarchical_dataset select_data : {select_data}')

    dataset_log += '\n'
    # for dirpath, dirnames, filenames in os.walk(root+'/'):
    # for dirpath, dirnames, filenames in os.walk(root + '\\'):
    for dirpath, dirnames, filenames in os.walk(root + r''):

        # 로그용
        #print(f'dataset.py hierarchical_dataset dirpath : {dirpath}')
        # print(f'dataset.py hierarchical_dataset dirnames : {dirnames}')
        # print(f'dataset.py hierarchical_dataset filenames : {filenames}')

        # mdb 파일 있는 경로일 경우 ( 마지막 경로 )
        if not dirnames:

            # 로그용
            #print(f'dataset.py mdb 파일 있는 경로일 경우  dirnames: {dirnames}')

            select_flag = False
            for selected_d in select_data:

                # 로그용
                # print(f'dataset.py for selected_d in select_data -> selected_d : {selected_d}')
                # print(f'dataset.py for selected_d in select_data -> select_data : {select_data}')
                # print(f'dataset.py for selected_d in select_data -> dirpath : {dirpath}')

                #if selected_d in dirpath:
                if selected_d in dirpath and filenames:

                    # 로그용
                    # print(f'dataset.py if selected_d in dirpath and filenames: {filenames}')
                    #
                    # print(f'dataset.py selected_d in dirpath: {dirpath}')
                    # print(f'dataset.py 디렉토리 {dirpath}에 파일이 있음')
                    # print(f'dataset.py 있다 selected_d : {selected_d}')
                    # print(f'dataset.py selected_d in dirpath: {dirpath}')
                    select_flag = True
                    break

            if select_flag:
                # 로그용
                #print(f'dataset.py if select_flag dirpath : {dirpath}')
                # 로그용
                #print(f'dataset.py if select_flag opt : {opt}')

                dataset = LmdbDataset(dirpath, opt)
                #print(f'dataset.py if select_flag dataset : {dataset}')
                # 로그용
                #print(f'dataset.py if select_flag len(dataset) : {len(dataset)}')
                # 라벨 정보 가져오기
                labels2 = []

                # for i in range(len(dataset)):
                #     key = str(i)  # 각 데이터 포인트의 키를 순차적으로 생성
                #     print(f'dataset.py if 각 데이터 포인트의 키 : {key}')
                    # 에러남 get_item 속성 없음
                    # value = dataset.get_item(key)  # 키에 해당하는 값(라벨 및 이미지 데이터) 가져오기
                    # print(f'dataset.py hierarchical_dataset 라벨 정보 가져오기 key : {key}')
                    # print(f'dataset.py hierarchical_dataset 라벨 정보 가져오기 value : {value}')
                    # label = value['label']  # 'label' 키를 사용하여 라벨 정보 가져오기
                    # print(f'dataset.py hierarchical_dataset 라벨 정보 가져오기 label : {label}')
                    #labels2.append(label)
                #print(f'hierarchical_dataset 라벨 정보 가져오기 labels2 : {labels2}')
                # 라벨 출력
                #print("Labels from LmdbDataset labels2:", labels2)

                # 중복된 라벨 확인
                #unique_labels = set(labels2)
                #ㅃprint("!여기서 중복된거 제거돼서 71 개임/??Number of Unique Labels:", len(unique_labels))

                # print(f' dirpath : {dirpath}')
                # print(f'  root : {root}')
                # print(f' os.path.relpath(dirpath, root) : {os.path.relpath(dirpath, root)}')

                # print(f' len(dataset) : {len(dataset)}')

                relative_path = os.path.relpath(dirpath, root)
                relative_path = relative_path.replace('/', '\\')  # 슬래시를 역슬래시로 변경

                sub_dataset_log = f'sub-directory:\t/{os.path.relpath(dirpath, root)}\t num samples: {len(dataset)}'
                # 로그용
                #print(f'dataset.py hierarchical_dataset len(dataset) : {len(dataset)}')
                #print(sub_dataset_log)
                dataset_log += f'{sub_dataset_log}\n'
                dataset_list.append(dataset)
                # 로그용
                #print(f'dataset.py hierarchical_dataset len(dataset_list) : {len(dataset_list)}')
                # print(f'hierarchical_dataset dataset : {dataset}')
                # print(f'hierarchical_dataset dataset_list : {dataset_list}')
                # print(f'hierarchical_dataset dataset_log : {dataset_log}')

    concatenated_dataset = ConcatDataset(dataset_list)
    # 로그용
    #print(f'hierarchical_dataset concatenated_dataset : {concatenated_dataset}')
    #print(f'hierarchical_dataset len(concatenated_dataset) : {len(concatenated_dataset)}')
    return concatenated_dataset, dataset_log


class LmdbDataset(Dataset):

    def __init__(self, root, opt):

        self.root = root
        self.opt = opt
        # 로그용
        #print(f'dataset.py LmdbDataset root {root}')

        #print(f'dataset.py LmdbDataset opt : {opt}')
        # if 'ๆ' in opt.character:
        #     # 'ๆ' 문자가 있을 경우
        #     print('LmdbDataset ๆ 있음')
        # else:
        #     # 'ๆ' 문자가 없을 경우
        #     print('LmdbDataset ๆ 없음')

        self.env = lmdb.open(root, max_readers=32, readonly=True, lock=False, readahead=False, meminit=False)

        # 다음 코드를 추가하여 self.env의 정보를 출력합니다.
        # 로그용
        # print('================================================================')
        # print(f"dataset.py  LMDB Environment Information:\n{self.env.info()}")
        # print('================================================================')

        if not self.env:
            print('cannot create lmdb from %s' % (root))
            sys.exit(0)

        with self.env.begin(write=False) as txn:

            # 데이터베이스의 모든 키-값 쌍을 읽어오기
            cursor = txn.cursor()

            # 데이터베이스에 데이터가 있는지 확인
            if not cursor.first():
                print("dataset.py lmdb 데이터 베이스에 데이터 없음.")
                #return


            for key, value in cursor:
                pass
                # key, value를 출력하거나 원하는 작업 수행
                #print(f'Key : {key}')
                # b'\xff\xd8\xff\xe0\...
                #print(f'LmdbDataset Value : {Value}')

            nSamples = int(txn.get('num-samples'.encode()))
            self.nSamples = nSamples
            # 로그용
            #print(f'LmdbDataset nSamples : {nSamples}')
            #print(f'###########################################LmdbDataset self.nSamples  : {self.nSamples}')

            if self.opt.data_filtering_off:
                # for fast check or benchmark evaluation with no filtering
                self.filtered_index_list = [index + 1 for index in range(self.nSamples)]

                # 로그용
                #print(f'LmdbDataset self.filtered_index_list : {self.filtered_index_list}')

                # 로그용
                # print(
                #     f'^^^^^^^^^^^^^^^^^필터링 안함 self.filtered_index_list : {self.filtered_index_list}')
                # print(
                #     f'^^^^^^^^^^^^^^^^^필터링 안함 self.nSamples : {self.nSamples}')
            else:
                """ Filtering part
                If you want to evaluate IC15-2077 & CUTE datasets which have special character labels,
                use --data_filtering_off and only evaluate on alphabets and digits.
                see https://github.com/clovaai/deep-text-recognition-benchmark/blob/6593928855fb7abb999a99f428b3e4477d4ae356/dataset.py#L190-L192

                And if you want to evaluate them with the model trained with --sensitive option,
                use --sensitive and --data_filtering_off,
                see https://github.com/clovaai/deep-text-recognition-benchmark/blob/dff844874dbe9e0ec8c5a52a7bd08c7f20afe704/test.py#L137-L144
                """
                self.filtered_index_list = []
                for index in range(self.nSamples):
                    index += 1  # lmdb starts with 1
                    label_key = 'label-%09d'.encode() % index
                    print(f'dataset.py __init__  label_key : {label_key}')
                    label = txn.get(label_key).decode('utf-8')
                    print(f'dataset.py __init__  label : {label}')

                    if len(label) > self.opt.batch_max_length:
                        # print(f'The length of the label is longer than max_length: length
                        # {len(label)}, {label} in dataset {self.root}')
                        continue

                    # By default, images containing characters which are not in opt.character are filtered.
                    # You can add [UNK] token to `opt.character` in utils.py instead of this filtering.
                    out_of_char = f'[^{self.opt.character}]'
                    if re.search(out_of_char, label.lower()):
                        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^설마 여기서 필터링 됨?????')
                        continue

                    self.filtered_index_list.append(index)
                    print(f'self.filtered_index_list : {self.filtered_index_list}')
                    print(f'len(self.filtered_index_list) : {len(self.filtered_index_list)}')
                self.nSamples = len(self.filtered_index_list)

    def __len__(self):
        return self.nSamples

    def __getitem__(self, index):
        assert index <= len(self), 'index range error'
        index = self.filtered_index_list[index]

        with self.env.begin(write=False) as txn:
            label_key = 'label-%09d'.encode() % index
            label = txn.get(label_key).decode('utf-8')
            img_key = 'image-%09d'.encode() % index
            imgbuf = txn.get(img_key)

            buf = six.BytesIO()
            buf.write(imgbuf)
            buf.seek(0)
            try:
                if self.opt.rgb:
                    img = Image.open(buf).convert('RGB')  # for color image
                else:
                    img = Image.open(buf).convert('L')

            except IOError:
                print(f'Corrupted image for {index}')
                # make dummy image and dummy label for corrupted image.
                if self.opt.rgb:
                    img = Image.new('RGB', (self.opt.imgW, self.opt.imgH))
                else:
                    img = Image.new('L', (self.opt.imgW, self.opt.imgH))
                label = '[dummy_label]'

            if not self.opt.sensitive:
                label = label.lower()

            # We only train and evaluate on alphanumerics (or pre-defined character set in train.py)
            out_of_char = f'[^{self.opt.character}]'
            # label = re.sub(out_of_char, '', label)
            # 이미지를 시각화하고 저장
            #img.show()  # 이미지를 화면에 표시
        return (img, label)


class RawDataset(Dataset):

    def __init__(self, root, opt):
        self.opt = opt
        self.image_path_list = []
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:
                _, ext = os.path.splitext(name)
                ext = ext.lower()
                if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
                    self.image_path_list.append(os.path.join(dirpath, name))

        self.image_path_list = natsorted(self.image_path_list)
        self.nSamples = len(self.image_path_list)

    def __len__(self):
        return self.nSamples

    def __getitem__(self, index):

        try:
            if self.opt.rgb:
                img = Image.open(self.image_path_list[index]).convert('RGB')  # for color image
            else:
                img = Image.open(self.image_path_list[index]).convert('L')

        except IOError:
            print(f'Corrupted image for {index}')
            # make dummy image and dummy label for corrupted image.
            if self.opt.rgb:
                img = Image.new('RGB', (self.opt.imgW, self.opt.imgH))
            else:
                img = Image.new('L', (self.opt.imgW, self.opt.imgH))

        return (img, self.image_path_list[index])


class ResizeNormalize(object):

    def __init__(self, size, interpolation=Image.BICUBIC):
        self.size = size
        self.interpolation = interpolation
        self.toTensor = transforms.ToTensor()

    def __call__(self, img):
        img = img.resize(self.size, self.interpolation)
        img = self.toTensor(img)
        img.sub_(0.5).div_(0.5)
        return img


class NormalizePAD(object):

    def __init__(self, max_size, PAD_type='right'):
        self.toTensor = transforms.ToTensor()
        self.max_size = max_size
        self.max_width_half = math.floor(max_size[2] / 2)
        self.PAD_type = PAD_type

    def __call__(self, img):
        img = self.toTensor(img)
        img.sub_(0.5).div_(0.5)
        c, h, w = img.size()
        Pad_img = torch.FloatTensor(*self.max_size).fill_(0)
        Pad_img[:, :, :w] = img  # right pad
        if self.max_size[2] != w:  # add border Pad
            Pad_img[:, :, w:] = img[:, :, w - 1].unsqueeze(2).expand(c, h, self.max_size[2] - w)

        return Pad_img


class AlignCollate(object):

    #def __init__(self, imgH=32, imgW=100, keep_ratio_with_pad=False):
    #def __init__(self, imgH=111.0, imgW=141.0, keep_ratio_with_pad=False):
    #def __init__(self, imgH=55.5, imgW=70.5, keep_ratio_with_pad=False):
    def __init__(self, imgH=111.0, imgW=141.0, keep_ratio_with_pad=False):

        self.imgH = imgH
        self.imgW = imgW
        self.imgH = int(imgH)
        self.imgW = int(imgW)

        self.keep_ratio_with_pad = keep_ratio_with_pad

        print(f'dataset.py AlignCollate imgH : {imgH}')
        print(f'dataset.py AlignCollate imgW : {imgW}')
        print(f'dataset.py AlignCollate keep_ratio_with_pad : {keep_ratio_with_pad}')



    def __call__(self, batch):
        batch = filter(lambda x: x is not None, batch)
        images, labels = zip(*batch)

        if self.keep_ratio_with_pad:  # same concept with 'Rosetta' paper
            resized_max_w = self.imgW
            input_channel = 3 if images[0].mode == 'RGB' else 1
            transform = NormalizePAD((input_channel, self.imgH, resized_max_w))

            resized_images = []
            for image in images:
                w, h = image.size
                ratio = w / float(h)
                if math.ceil(self.imgH * ratio) > self.imgW:
                    resized_w = self.imgW
                else:
                    resized_w = math.ceil(self.imgH * ratio)

                resized_image = image.resize((resized_w, self.imgH), Image.BICUBIC)
                resized_images.append(transform(resized_image))
                # resized_image.save('./image_test/%d_test.jpg' % w)

            image_tensors = torch.cat([t.unsqueeze(0) for t in resized_images], 0)

        else:
            transform = ResizeNormalize((self.imgW, self.imgH))
            image_tensors = [transform(image) for image in images]
            image_tensors = torch.cat([t.unsqueeze(0) for t in image_tensors], 0)

        return image_tensors, labels


def tensor2im(image_tensor, imtype=np.uint8):
    image_numpy = image_tensor.cpu().float().numpy()
    if image_numpy.shape[0] == 1:
        image_numpy = np.tile(image_numpy, (3, 1, 1))
    image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0
    return image_numpy.astype(imtype)


def save_image(image_numpy, image_path):
    image_pil = Image.fromarray(image_numpy)
    image_pil.save(image_path)
