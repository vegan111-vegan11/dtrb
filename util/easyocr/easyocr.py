# -*- coding: utf-8 -*-

from .recognition import get_recognizer, get_text
from .utils import group_text_box, get_image_list, calculate_md5, get_paragraph, \
    download_and_unzip, printProgressBar, diff, reformat_input, \
    make_rotated_img_list, set_result_with_confidence, \
    reformat_input_batched, merge_to_free
from .config import *
from bidi.algorithm import get_display
import numpy as np
import cv2
import torch
import os
import sys
from PIL import Image
from logging import getLogger
import yaml
import json
import None_VGG_BiLSTM_CTC  # 모델 아키텍처가 정의된 모듈을 임포트
from None_VGG_BiLSTM_CTC import None_VGG_BiLSTM_CTC  # 모델 아키텍처가 정의된 모듈을 임포트

import None_VGG_BiLSTM_CTC  # 모델 아키텍처가 정의된 모듈을 임포트
from None_VGG_BiLSTM_CTC import None_VGG_BiLSTM_CTC  # 모델 아키텍처가 정의된 모듈을 임포트

# 모듈이 위치한 경로를 시스템 경로에 추가
module_path = r"C:\Users\TAMSystech\anaconda3\envs\ocr2\Lib\site-packages\easyocr\model"
sys.path.append(module_path)
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!model 경로 추가 :  ')

# import TPS_ResNet_BiLSTM_Attn  # 모델 아키텍처가 정의된 모듈을 임포트
# from TPS_ResNet_BiLSTM_Attn import TPS_ResNet_BiLSTM_Attn  # 모델 아키텍처가 정의된 모듈을 임포트


# 모듈을 import
# from TPS_ResNet_BiLSTM_Attn2 import YourModule

# 나머지 코드 계속 진행


print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!None_VGG_BiLSTM_CTC 임포트 완료 :  ')

if sys.version_info[0] == 2:
    from io import open
    from six.moves.urllib.request import urlretrieve
    from pathlib2 import Path
else:
    from urllib.request import urlretrieve
    from pathlib import Path

LOGGER = getLogger(__name__)


class Reader(object):

    def __init__(self, lang_list, gpu=True, model_storage_directory=None,
                 user_network_directory=None, detect_network="craft",
                 recog_network='standard', download_enabled=True,
                 detector=True, recognizer=True, verbose=True,
                 quantize=True, cudnn_benchmark=False):

        # print(            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.user_network_directory : {self.user_network_directory}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self!!: {self}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.user_network_directory 파라미터 전달 받음 !!: {model_storage_directory}')

        self.user_network_directory = "C:\\Users\\TAMSystech\\.EasyOCR\\user_network"
        # self.user_network_directory = model_storage_directory
        # print(
        #     f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.user_network_directory 파라미터 전달 받음 self.user_network_directory = model_storage_directory !!: {self.user_network_directory}')

        self.detect_network = detect_network
        self.recog_network = recog_network
        self.download_enabled = download_enabled
        self.detector = detector
        self.recognizer = recognizer
        self.cudnn_benchmark = cudnn_benchmark
        self.model_storage_directory = model_storage_directory

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.user_network_directory 변경후!!: {self.user_network_directory}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.detect_network : {self.detect_network}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.recog_network : {self.recog_network}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.download_enabled : {self.download_enabled}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.detector : {self.detector}')

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.recognizer : {self.recognizer}')
        # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.detector : {self.detector}')
        # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.recognizer : {self.recognizer}')
        # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.verbose= : {self.verbose=}')
        # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.cudnn_benchmark : {self.cudnn_benchmark}')

        """Create an EasyOCR Reader

        Parameters:
            lang_list (list): Language codes (ISO 639) for languages to be recognized during analysis.

            gpu (bool): Enable GPU support (default)

            model_storage_directory (string): Path to directory for model data. If not specified,
            models will be read from a directory as defined by the environment variable
            EASYOCR_MODULE_PATH (preferred), MODULE_PATH (if defined), or ~/.EasyOCR/.

            user_network_directory (string): Path to directory for custom network architecture.
            If not specified, it is as defined by the environment variable
            EASYOCR_MODULE_PATH (preferred), MODULE_PATH (if defined), or ~/.EasyOCR/.

            download_enabled (bool): Enabled downloading of model data via HTTP (default).
        """
        self.verbose = verbose
        self.download_enabled = download_enabled

        self.model_storage_directory = MODULE_PATH + '/model'
        self.model_storage_directory = MODULE_PATH + '/model'
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.model_storage_directory : {self.model_storage_directory}')
        self.model_storage_directory = "C:\\Users\\TAMSystech\\.EasyOCR\\model"
        self.model_storage_directory = r"C:/Users/TAMSystech/.EasyOCR/model"
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.model_storage_director 수정후: {self.model_storage_directory}')
        # self.model_storage_directory = "C:\\Users\\TAMSystech\\.EasyOCR\\user_network"
        # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  model_storage_directory 수정후!!: {self.model_storage_directory}')

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr class Reader __init__ self.MODULE_PATH : {MODULE_PATH}')
        if model_storage_directory:
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr model_storage_directory 있음 : {model_storage_directory}')
            # self.model_storage_directory = model_storage_directory
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.model_storage_directory 대입 : {self.model_storage_directory}')
        Path(self.model_storage_directory).mkdir(parents=True, exist_ok=True)
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr self.model_storage_directory 디렉토리 만듬 : {self.model_storage_directory}')
        self.user_network_directory = MODULE_PATH + '/user_network'
        self.user_network_directory = MODULE_PATH + 'user_network'
        user_network_directory = MODULE_PATH + 'user_network/'
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr user_network_directory : {user_network_directory}')
        if user_network_directory:
            self.user_network_directory = user_network_directory
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr user_network_directory 있음 self.user_network_directory 디렉토리 만듬 : {self.user_network_directory}')
        Path(self.user_network_directory).mkdir(parents=True, exist_ok=True)
        sys.path.append(self.user_network_directory)
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr user_network_directory 어펜드 완료 : {self.user_network_directory}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!self.user_network_directory 추가완료: {self.user_network_directory}')
        # self.model_storage_directory = user_network_directory
        # self.model_storage_directory = user_network_directory
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!self.model_storage_directory : {self.model_storage_directory}')
        # print('내가 바꿈!!!!!!!!!!')
        if gpu is False:
            self.device = 'cpu'
            if verbose:
                LOGGER.warning('Using CPU. Note: This module is much faster with a GPU.')
        elif gpu is True:
            if torch.cuda.is_available():
                self.device = 'cuda'
            elif torch.backends.mps.is_available():
                self.device = 'mps'
            else:
                self.device = 'cpu'
                if verbose:
                    LOGGER.warning(
                        'Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.')
        else:
            self.device = gpu

        self.detection_models = detection_models
        self.recognition_models = recognition_models

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognition_models  : {recognition_models}')

        # check and download detection model
        self.support_detection_network = ['craft', 'dbnet18']
        self.quantize = quantize,
        self.cudnn_benchmark = cudnn_benchmark
        if detector:
            detector_path = self.getDetectorPath(detect_network)
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!detector 있음 detector_path : {detector_path}')

        # recognition model
        separator_list = {}
        gen1 = recognition_models['gen1']
        gen2 = recognition_models['gen2']
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!detector 있음 recog_network : {recog_network}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!detector 있음 recognition_models : {recognition_models}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!detector 있음 recognition_models gen1 : {gen1}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!detector 있음 recognition_models gen2 : {gen2}')

        if recog_network in ['standard'] + [model for model in recognition_models['gen1']] + [model for model in
                                                                                              recognition_models[
                                                                                                  'gen2']]:
            if recog_network in [model for model in recognition_models['gen1']]:
                model = recognition_models['gen1'][recog_network]
                recog_network = 'generation1'
                self.model_lang = model['model_script']
            elif recog_network in [model for model in recognition_models['gen2']]:
                model = recognition_models['gen2'][recog_network]
                recog_network = 'generation2'
                self.model_lang = model['model_script']
            else:  # auto-detect
                unknown_lang = set(lang_list) - set(all_lang_list)
                if unknown_lang != set():
                    raise ValueError(unknown_lang, 'is not supported')
                # choose recognition model
                if lang_list == ['en']:
                    self.setModelLanguage('english', lang_list, ['en'], '["en"]')
                    model = recognition_models['gen2']['english_g2']
                    recog_network = 'generation2'
                elif 'th' in lang_list:
                    self.setModelLanguage('thai', lang_list, ['th', 'en'], '["th","en"]')
                    model = recognition_models['gen1']['thai_g1']
                    recog_network = 'generation1'

                    md5s = model['md5sum']

                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!타이니까 여기에서 모델 설정 정해져있는거만 쓸수 있음?    recognition_models : {recognition_models}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!타이니까 여기에서 모델 설정 model : {model}')

                    # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!타이니까 여기에서 모델 설정 recognition_models : {recognition_models}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!타이니까 여기에서 모델 설정 recog_network : {recog_network}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!타이니까 여기에서 모델 설정 모델이 기대하는 해시값 뭔데 md5s : {md5s}')

                elif 'ch_tra' in lang_list:
                    self.setModelLanguage('chinese_tra', lang_list, ['ch_tra', 'en'], '["ch_tra","en"]')
                    model = recognition_models['gen1']['zh_tra_g1']
                    recog_network = 'generation1'
                elif 'ch_sim' in lang_list:
                    self.setModelLanguage('chinese_sim', lang_list, ['ch_sim', 'en'], '["ch_sim","en"]')
                    model = recognition_models['gen2']['zh_sim_g2']
                    recog_network = 'generation2'
                elif 'ja' in lang_list:
                    self.setModelLanguage('japanese', lang_list, ['ja', 'en'], '["ja","en"]')
                    model = recognition_models['gen2']['japanese_g2']
                    recog_network = 'generation2'
                elif 'ko' in lang_list:
                    self.setModelLanguage('korean', lang_list, ['ko', 'en'], '["ko","en"]')
                    model = recognition_models['gen2']['korean_g2']
                    recog_network = 'generation2'
                elif 'ta' in lang_list:
                    self.setModelLanguage('tamil', lang_list, ['ta', 'en'], '["ta","en"]')
                    model = recognition_models['gen1']['tamil_g1']
                    recog_network = 'generation1'
                elif 'te' in lang_list:
                    self.setModelLanguage('telugu', lang_list, ['te', 'en'], '["te","en"]')
                    model = recognition_models['gen2']['telugu_g2']
                    recog_network = 'generation2'
                elif 'kn' in lang_list:
                    self.setModelLanguage('kannada', lang_list, ['kn', 'en'], '["kn","en"]')
                    model = recognition_models['gen2']['kannada_g2']
                    recog_network = 'generation2'
                elif set(lang_list) & set(bengali_lang_list):
                    self.setModelLanguage('bengali', lang_list, bengali_lang_list + ['en'], '["bn","as","en"]')
                    model = recognition_models['gen1']['bengali_g1']
                    recog_network = 'generation1'
                elif set(lang_list) & set(arabic_lang_list):
                    self.setModelLanguage('arabic', lang_list, arabic_lang_list + ['en'], '["ar","fa","ur","ug","en"]')
                    model = recognition_models['gen1']['arabic_g1']
                    recog_network = 'generation1'
                elif set(lang_list) & set(devanagari_lang_list):
                    self.setModelLanguage('devanagari', lang_list, devanagari_lang_list + ['en'],
                                          '["hi","mr","ne","en"]')
                    model = recognition_models['gen1']['devanagari_g1']
                    recog_network = 'generation1'
                elif set(lang_list) & set(cyrillic_lang_list):
                    self.setModelLanguage('cyrillic', lang_list, cyrillic_lang_list + ['en'],
                                          '["ru","rs_cyrillic","be","bg","uk","mn","en"]')
                    model = recognition_models['gen2']['cyrillic_g2']
                    recog_network = 'generation2'
                else:
                    self.model_lang = 'latin'
                    model = recognition_models['gen2']['latin_g2']
                    recog_network = 'generation2'
            self.character = model['characters']

            model_path = os.path.join(self.model_storage_directory, model['filename'])
            model_path = os.path.join(self.user_network_directory, model['filename'])
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  user_network_directory 로 바꿈 model_path : {model_path}')
            # check recognition model file

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  219 model_storage_directory: {self.model_storage_directory}')

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  model  !!!!!!: {model}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  model_path: {model_path}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  recognizer: {recognizer}')

            if recognizer:
                model_storage_directory = "C:\\Users\\TAMSystech\\.EasyOCR\\model"
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  if recognizer model_storage_directory model_storage_directory: {self.model_storage_directory}')

                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  if recognizer model 수정후!!!!!!: {model}')
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py if recognizer 230  model_path: {model_path}')

                custom_model_directory = 'C:/Users/TAMSystech/.EasyOCR/user_network'

                model_path = r'C:/Users/TAMSystech/.EasyOCR/user_network/thai.pth'
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr  if recognizer 여기서 에러남 calculate_md5 계산은 함 calculate_md5(model_path) : {calculate_md5(model_path)}')
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr if recognizer  여기서 에러남 model md5sum : {md5s}')

                if os.path.isfile(model_path) == False:

                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  FalseFalseFalseFalse os.path.isfile(model_path): {os.path.isfile(model_path)}')
                    if not self.download_enabled:
                        raise FileNotFoundError("Missing %s and downloads disabled" % model_path)
                    LOGGER.warning('Downloading recognition model, please wait. '
                                   'This may take several minutes depending upon your network connection.')
                    download_and_unzip(model['url'], model['filename'], self.model_storage_directory, verbose)

                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  model: {model}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py  self.model_storage_directory: {self.model_storage_directory}')
                    corrupt_msg = '커럽 메세지'
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyOcr.py os.path.isfile(model_path) == False 커럽 메세지가 없대 corrupt_msg: {corrupt_msg}')

                    assert calculate_md5(model_path) == model['md5sum'], corrupt_msg
                    md5s = model['md5sum']
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!os.path.isfile(model_path) == False 커럽 메세지 출력해야함 calculate_md5(model_path) : {calculate_md5(model_path)}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!os.path.isfile(model_path) == False 커럽 메세지 출력해야함 md5sum : {md5s}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!os.path.isfile(model_path) == False 커럽 메세지 출력해야함 model : {model}')

                    LOGGER.info('Download complete.')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 여기서 에러남 calculate_md5(model_path) : {calculate_md5(model_path)}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 여기서 에러남 model md5sum : {model}')
                elif calculate_md5(model_path) != model['md5sum']:
                    md5s = model['md5sum']
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!model_path 널 아님 근데 해시값 틀림 model_path : {model_path}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!model_path 널 아님 근데 해시값 틀림 md5s 기대값이래 = : {md5s}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!model_path 널 아님 근데 해시값 틀림 model = : {model}')
                    if not self.download_enabled:
                        raise FileNotFoundError("MD5 mismatch for %s and downloads disabled" % model_path)
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델패스는 있는데 해시값 틀림 여기서 에러남 model_path : {model_path}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델패스는 있는데 해시값 틀림 여기서 에러남 calculate_md5(model_path) : {calculate_md5(model_path)}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델패스는 있는데 해시값 틀림 여기서 에러남 모델 기대값 해시 기대값  md5s : {md5s}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델패스는 있는데 해시값 틀림 여기서 에러남 model : {model}')

                    corrupt_msg = '커럽 메세지'
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr corrupt_msg : {corrupt_msg}')
                    LOGGER.warning(corrupt_msg)
                    os.remove(model_path)
                    LOGGER.warning('Re-downloading the recognition model, please wait. '
                                   'This may take several minutes depending upon your network connection.')

                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델 다운로드하기 전  model_storage_directory : {model_storage_directory}')
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델 다운로드하기 전  model_path : {model_path}')
                    file_name = model['filename']
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!모델 filefile_name 으로 저장 다운 받아서 파일이름으로 저장한다: {file_name}')

                    download_and_unzip(model['url'], model['filename'], self.model_storage_directory, verbose)
                    print(
                        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델 다운로드하는 중 self.model_storage_directory : {self.model_storage_directory}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델 다운로드하는 중  model : {model}')
                    assert calculate_md5(model_path) == model['md5sum'], corrupt_msg
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr2 의 easyOcr 모델 다운로드하는 중 해시값 틀리면 경고문 후 중단 model : {model}')
                    LOGGER.info('Download complete')
            self.setLanguageList(lang_list, model)

        ########################################################################
        else:  # user-defined model
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 BASE_PATH : {BASE_PATH}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 self.user_network_directory : {self.user_network_directory}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 recog_network : {recog_network}')
            file_path = self.user_network_directory + recog_network + '.yaml'
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 file_path : {file_path}')

            with open(file_path, encoding='utf8') as file:
                # 파일 내용을 읽는 코드 작성

                # with open(os.path.join(self.user_network_directory, recog_network+ '.yaml'), encoding='utf8') as file:
                # with open('C:/Users/TAMSystech/.EasyOCR/user_network/None-VGG-BiLSTM-CTC.yaml'), encoding='utf8') as file:
                recog_config = yaml.load(file, Loader=yaml.FullLoader)

                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 recog_config yaml 파일 읽음 성공: {recog_config}')

            global imgH  # if custom model, save this variable. (from *.yaml)
            if recog_config['imgH']:
                imgH = recog_config['imgH']

            available_lang = recog_config['lang_list']
            self.setModelLanguage(recog_network, lang_list, available_lang, str(available_lang))
            # char_file = os.path.join(self.user_network_directory, recog_network+ '.txt')
            self.character = recog_config['character_list']
            model_file = recog_network + '.pth'
            model_path = os.path.join(self.model_storage_directory, model_file)
            self.setLanguageList(lang_list, recog_config)

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 self.character : {self.character}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 lang_list : {lang_list}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 recog_network : {recog_network}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 detector : {detector}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 detector_path : {detector_path}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 recognizer : {recognizer}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 BASE_PATH : {BASE_PATH}')

        dict_list = {}
        for lang in lang_list:
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 for lang in lang_list lang: {lang}')

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 for lang in lang_list  : {lang_list}')

            dict_list[lang] = os.path.join(BASE_PATH, 'dict', lang + ".txt")

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 dict_list : {dict_list}')

        if detector:
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 if detector : {detector}')
            self.detector = self.initDetector(detector_path)
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임inputs[0] if detector  initDetector 호출 완료 detector_path : {detector_path}')
            # print(
            #     f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임inputs[0] if detector  initDetector 호출 완료 inputs[0] : {inputs[0]}')
        if recognizer:

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!user-defined model 임 recog_network : {recog_network}')

            if recog_network == 'generation1':
                network_params = {
                    'input_channel': 1,
                    'output_channel': 512,
                    'hidden_size': 512
                }
            elif recog_network == 'generation2':
                network_params = {
                    'input_channel': 1,
                    'output_channel': 256,
                    'hidden_size': 256
                }
            else:
                network_params = recog_config['network_params']

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 recog_network : {recog_network}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 network_params : {network_params}')

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 separator_list : {separator_list}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 dict_list : {dict_list}')

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 model_path : {model_path}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 quantize : {quantize}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 self.device : {self.device}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전 self.character : {self.character}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행전  network_params : {network_params}')

            # 모델 아키텍처를 초기화
            # model = None_VGG_BiLSTM_CTC.None_VGG_BiLSTM_CTC(input_size, output_size)
            input_channel = 1  # 입력 채널 수
            output_channel = 512  # 출력 채널 수
            hidden_size = 256  # 은닉 상태의 크기
            num_classes = 100  # 출력 클래스(레이블)의 수 # 나중에 레이블 수로 수정해야함. 다시 훈련시켜야 함

            # 클래스 인스턴스 생성
            # model = None_VGG_BiLSTM_CTC(input_channel, output_channel, hidden_size, num_classes)
            model = None_VGG_BiLSTM_CTC(input_channel, output_channel, hidden_size, num_classes)

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr one_VGG_BiLSTM_CTC 호출 완료 num_classes : {num_classes}')

            user_network_directory = r'C:/Users/TAMSystech/.EasyOCR/user_network'
            # reader = easyocr.Reader(['th', 'en'], recog_network='None_VGG_BiLSTM_CTC')

            # reader = easyocr.Reader(['th', 'en'], recog_network=os.path.join(user_network_directory, 'None-VGG-BiLSTM-CTC.yaml'))

            # recog_network = os.path.join(user_network_directory, 'None-VGG-BiLSTM-CTC.yaml')
            recog_network = os.path.join(user_network_directory, 'None-VGG-BiLSTM-CTC.yaml')

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recog_network 경로 get_recognizer 에 전달할 변수 recog_network : {recog_network}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recog_network 경로 get_recognizer 에 전달할 model_path : {model_path}')
            # model_path = os.path.join(user_network_directory, 'thai.pth')
            model_path = os.path.join(user_network_directory, 'thai.pth')

            self.recognizer, self.converter = get_recognizer(recog_network, network_params, \
                                                             self.character, separator_list, \
                                                             dict_list, model_path, device=self.device,
                                                             quantize=quantize)

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행후 recog_config : {recog_config}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행후 self.recognizer : {self.recognizer}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr user-defined model 임 get_recognizer 함수 실행후 self.converter : {self.converter}')

    def getDetectorPath(self, detect_network):
        if detect_network in self.support_detection_network:
            self.detect_network = detect_network
            if self.detect_network == 'craft':
                from .detection import get_detector, get_textbox
            elif self.detect_network in ['dbnet18']:
                from .detection_db import get_detector, get_textbox
            else:
                raise RuntimeError("Unsupport detector network. Support networks are craft and dbnet18.")
            self.get_textbox = get_textbox
            self.get_detector = get_detector
            corrupt_msg = 'MD5 hash mismatch, possible file corruption'
            detector_path = os.path.join(self.model_storage_directory,
                                         self.detection_models[self.detect_network]['filename'])
            if os.path.isfile(detector_path) == False:
                if not self.download_enabled:
                    raise FileNotFoundError("Missing %s and downloads disabled" % detector_path)
                LOGGER.warning('Downloading detection model, please wait. '
                               'This may take several minutes depending upon your network connection.')
                download_and_unzip(self.detection_models[self.detect_network]['url'],
                                   self.detection_models[self.detect_network]['filename'], self.model_storage_directory,
                                   self.verbose)
                assert calculate_md5(detector_path) == self.detection_models[self.detect_network]['md5sum'], corrupt_msg
                LOGGER.info('Download complete')
            elif calculate_md5(detector_path) != self.detection_models[self.detect_network]['md5sum']:
                if not self.download_enabled:
                    raise FileNotFoundError("MD5 mismatch for %s and downloads disabled" % detector_path)
                LOGGER.warning(corrupt_msg)
                os.remove(detector_path)
                LOGGER.warning('Re-downloading the detection model, please wait. '
                               'This may take several minutes depending upon your network connection.')
                download_and_unzip(self.detection_models[self.detect_network]['url'],
                                   self.detection_models[self.detect_network]['filename'], self.model_storage_directory,
                                   self.verbose)
                assert calculate_md5(detector_path) == self.detection_models[self.detect_network]['md5sum'], corrupt_msg
        else:
            raise RuntimeError("Unsupport detector network. Support networks are {}.".format(
                ', '.join(self.support_detection_network)))

        return detector_path

    def initDetector(self, detector_path):
        return self.get_detector(detector_path,
                                 device=self.device,
                                 quantize=self.quantize,
                                 cudnn_benchmark=self.cudnn_benchmark
                                 )

    def setDetector(self, detect_network):
        detector_path = self.getDetectorPath(detect_network)
        self.detector = self.initDetector(detector_path)

    def setModelLanguage(self, language, lang_list, list_lang, list_lang_string):
        self.model_lang = language
        if set(lang_list) - set(list_lang) != set():
            if language == 'ch_tra' or language == 'ch_sim':
                language = 'chinese'
            raise ValueError(
                language.capitalize() + ' is only compatible with English, try lang_list=' + list_lang_string)

    def getChar(self, fileName):
        char_file = os.path.join(BASE_PATH, 'character', fileName)
        with open(char_file, "r", encoding="utf-8-sig") as input_file:
            list = input_file.read().splitlines()
            char = ''.join(list)
        return char

    def setLanguageList(self, lang_list, model):
        self.lang_char = []
        for lang in lang_list:
            char_file = os.path.join(BASE_PATH, 'character', lang + "_char.txt")
            with open(char_file, "r", encoding="utf-8-sig") as input_file:
                char_list = input_file.read().splitlines()
            self.lang_char += char_list
        if model.get('symbols'):
            symbol = model['symbols']
        elif model.get('character_list'):
            symbol = model['character_list']
        else:
            symbol = '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        self.lang_char = set(self.lang_char).union(set(symbol))
        self.lang_char = ''.join(self.lang_char)

    def detect(self, img, min_size=20, text_threshold=0.7, low_text=0.4, \
               link_threshold=0.4, canvas_size=2560, mag_ratio=1., \
               slope_ths=0.1, ycenter_ths=0.5, height_ths=0.5, \
               width_ths=0.5, add_margin=0.1, reformat=True, optimal_num_chars=None,
               threshold=0.2, bbox_min_score=0.2, bbox_min_size=3, max_candidates=0,
               ):
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr detext 함수 들어옴 self: {self}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr detext 함수 들어옴 reformat: {reformat}')

        if reformat:
            img, img_cv_grey = reformat_input(img)

        text_box_list = self.get_textbox(self.detector,
                                         img,
                                         canvas_size=canvas_size,
                                         mag_ratio=mag_ratio,
                                         text_threshold=text_threshold,
                                         link_threshold=link_threshold,
                                         low_text=low_text,
                                         poly=False,
                                         device=self.device,
                                         optimal_num_chars=optimal_num_chars,
                                         threshold=threshold,
                                         bbox_min_score=bbox_min_score,
                                         bbox_min_size=bbox_min_size,
                                         max_candidates=max_candidates,
                                         )

        horizontal_list_agg, free_list_agg = [], []
        for text_box in text_box_list:
            horizontal_list, free_list = group_text_box(text_box, slope_ths,
                                                        ycenter_ths, height_ths,
                                                        width_ths, add_margin,
                                                        (optimal_num_chars is None))
            if min_size:
                horizontal_list = [i for i in horizontal_list if max(
                    i[1] - i[0], i[3] - i[2]) > min_size]
                free_list = [i for i in free_list if max(
                    diff([c[0] for c in i]), diff([c[1] for c in i])) > min_size]
            horizontal_list_agg.append(horizontal_list)
            free_list_agg.append(free_list)

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr detext 함수 들어옴 horizontal_list_agg: {horizontal_list_agg}')

        return horizontal_list_agg, free_list_agg

    def recognize(self, img_cv_grey, horizontal_list=None, free_list=None, \
                  decoder='greedy', beamWidth=5, batch_size=1, \
                  workers=0, allowlist=None, blocklist=None, detail=1, \
                  rotation_info=None, paragraph=False, \
                  contrast_ths=0.1, adjust_contrast=0.5, filter_ths=0.003, \
                  y_ths=0.5, x_ths=1.0, reformat=True, output_format='standard'):

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 img_cv_grey : {img_cv_grey}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 horizontal_list : {horizontal_list}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 free_list : {free_list}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 decoder : {decoder}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 beamWidth : {beamWidth}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 batch_size : {batch_size}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 workers : {workers}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 allowlist : {allowlist}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 reformat : {reformat}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 allowlist : {allowlist}')

        if reformat:
            img, img_cv_grey = reformat_input(img_cv_grey)
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 img : {img}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 img_cv_grey : {img_cv_grey}')

        if allowlist:
            ignore_char = ''.join(set(self.character) - set(allowlist))
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 ignore_char : {ignore_char}')


        elif blocklist:
            ignore_char = ''.join(set(blocklist))
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 blocklist : {blocklist}')


        else:
            ignore_char = ''.join(set(self.character) - set(self.lang_char))
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴 else  ignore_char : {ignore_char}')

        if self.model_lang in ['chinese_tra', 'chinese_sim']: decoder = 'greedy'

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   decoder : {decoder}')

        if (horizontal_list == None) and (free_list == None):
            y_max, x_max = img_cv_grey.shape
            horizontal_list = [[0, x_max, 0, y_max]]
            free_list = []

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   y_max : {y_max}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   x_max : {x_max}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   horizontal_list : {horizontal_list}')

        # without gpu/parallelization, it is faster to process image one by one
        if ((batch_size == 1) or (self.device == 'cpu')) and not rotation_info:
            result = []
            for bbox in horizontal_list:
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cpu or 배치사이즈 1 and not rotation_info  bbox : {bbox}')

                h_list = [bbox]
                f_list = []
                image_list, max_width = get_image_list(h_list, f_list, img_cv_grey, model_height=imgH)

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cpu or 배치사이즈 1 and not rotation_info  get text 호출전 image_list : {image_list}')

                result0 = get_text(self.character, imgH, int(max_width), self.recognizer, self.converter, image_list, \
                                   ignore_char, decoder, beamWidth, batch_size, contrast_ths, adjust_contrast,
                                   filter_ths, \
                                   workers, self.device)

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr -> recognize 함수 cpu or 배치사이즈 1 and not rotation_info  get text 호출완료 image_list : {image_list}')
                result += result0
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr -> recognize 함수 cpu or 배치사이즈 1 and not rotation_info  get text 호출완료 result0 : {result0}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr -> recognize 함수 cpu or 배치사이즈 1 and not rotation_info  get text 호출완료 result : {result}')

            for bbox in free_list:
                h_list = []
                f_list = [bbox]
                image_list, max_width = get_image_list(h_list, f_list, img_cv_grey, model_height=imgH)
                result0 = get_text(self.character, imgH, int(max_width), self.recognizer, self.converter, image_list, \
                                   ignore_char, decoder, beamWidth, batch_size, contrast_ths, adjust_contrast,
                                   filter_ths, \
                                   workers, self.device)
                result += result0

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cpu or 배치사이즈 1 and not rotation_info  result : {result}')
        # default mode will try to process multiple boxes at the same time
        else:

            image_list, max_width = get_image_list(horizontal_list, free_list, img_cv_grey, model_height=imgH)

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   else 지피요 사용시 image_list : {image_list}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   else 지피요 사용시 max_width : {max_width}')

            image_len = len(image_list)

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   else 지피요 사용시 image_len : {image_len}')

            if rotation_info and image_list:
                image_list = make_rotated_img_list(rotation_info, image_list)
                max_width = max(max_width, imgH)

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   if rotation_info and image_list  지피요 사용시 image_list : {image_list}')
                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   if rotation_info and image_list  지피요 사용시 max_width : {max_width}')

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   result  get_text 함수 호출전 : ')
            result = get_text(self.character, imgH, int(max_width), self.recognizer, self.converter, image_list, \
                              ignore_char, decoder, beamWidth, batch_size, contrast_ths, adjust_contrast, filter_ths, \
                              workers, self.device)
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   get_text 함수 호출 완료 result : {result}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴   get_text 함수 호출 완료 여기서 에러남????  result: {result}')

            if rotation_info and (horizontal_list + free_list):
                # Reshape result to be a list of lists, each row being for
                # one of the rotations (first row being no rotation)
                result = set_result_with_confidence(
                    [result[image_len * i:image_len * (i + 1)] for i in range(len(rotation_info) + 1)])

                print(
                    f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr recognize 함수 들어옴  if rotation_info and (horizontal_list+free_list)  get_text 함수 호출 완료 여기서 에러남????  result: {result}')

        if self.model_lang == 'arabic':
            direction_mode = 'rtl'
            result = [list(item) for item in result]
            for item in result:
                item[1] = get_display(item[1])
        else:
            direction_mode = 'ltr'

        if paragraph:
            result = get_paragraph(result, x_ths=x_ths, y_ths=y_ths, mode=direction_mode)

        if detail == 0:
            return [item[1] for item in result]
        elif output_format == 'dict':
            if paragraph:
                return [{'boxes': item[0], 'text': item[1]} for item in result]
            return [{'boxes': item[0], 'text': item[1], 'confident': item[2]} for item in result]
        elif output_format == 'json':
            if paragraph:
                return [
                    json.dumps({'boxes': [list(map(int, lst)) for lst in item[0]], 'text': item[1]}, ensure_ascii=False)
                    for item in result]
            return [
                json.dumps({'boxes': [list(map(int, lst)) for lst in item[0]], 'text': item[1], 'confident': item[2]},
                           ensure_ascii=False) for item in result]
        elif output_format == 'free_merge':
            return merge_to_free(result, free_list)
        else:
            return result

    def readtext(self, image, decoder='greedy', beamWidth=5, batch_size=1, \
                 workers=0, allowlist=None, blocklist=None, detail=1, \
                 rotation_info=None, paragraph=False, min_size=20, \
                 contrast_ths=0.1, adjust_contrast=0.5, filter_ths=0.003, \
                 text_threshold=0.7, low_text=0.4, link_threshold=0.4, \
                 canvas_size=2560, mag_ratio=1., \
                 slope_ths=0.1, ycenter_ths=0.5, height_ths=0.5, \
                 width_ths=0.5, y_ths=0.5, x_ths=1.0, add_margin=0.1,
                 threshold=0.2, bbox_min_score=0.2, bbox_min_size=3, max_candidates=0,
                 output_format='standard'):
        '''
        Parameters:
        image: file path or numpy-array or a byte stream object
        '''

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr readtext 함수 image 여기서 에러???? image :  ')

        img, img_cv_grey = reformat_input(image)

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr readtext 함수 img : {img}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr readtext 함수 img_cv_grey : {img_cv_grey}')

        # self.
        horizontal_list, free_list = self.detect(img,
                                                 min_size=min_size, text_threshold=text_threshold, \
                                                 low_text=low_text, link_threshold=link_threshold, \
                                                 canvas_size=canvas_size, mag_ratio=mag_ratio, \
                                                 slope_ths=slope_ths, ycenter_ths=ycenter_ths, \
                                                 height_ths=height_ths, width_ths=width_ths, \
                                                 add_margin=add_margin, reformat=False, \
                                                 threshold=threshold, bbox_min_score=bbox_min_score, \
                                                 bbox_min_size=bbox_min_size, max_candidates=max_candidates
                                                 )
        # get the 1st result from hor & free list as self.detect returns a list of depth 3
        horizontal_list, free_list = horizontal_list[0], free_list[0]

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr result 여기서 에러 readtext 함수 호출전 여기서 에러남????  함수에서 에러???>????? horizontal_list : {horizontal_list}')

        result = self.recognize(img_cv_grey, horizontal_list, free_list, \
                                decoder, beamWidth, batch_size, \
                                workers, allowlist, blocklist, detail, rotation_info, \
                                paragraph, contrast_ths, adjust_contrast, \
                                filter_ths, y_ths, x_ths, False, output_format)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr result 여기서 에러 readtext 함수에서 에러???>?????  : {result}')

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!easyocr readtext 함수 horizontal_list : {horizontal_list}')
        return result

    def readtextlang(self, image, decoder='greedy', beamWidth=5, batch_size=1, \
                     workers=0, allowlist=None, blocklist=None, detail=1, \
                     rotation_info=None, paragraph=False, min_size=20, \
                     contrast_ths=0.1, adjust_contrast=0.5, filter_ths=0.003, \
                     text_threshold=0.7, low_text=0.4, link_threshold=0.4, \
                     canvas_size=2560, mag_ratio=1., \
                     slope_ths=0.1, ycenter_ths=0.5, height_ths=0.5, \
                     width_ths=0.5, y_ths=0.5, x_ths=1.0, add_margin=0.1,
                     threshold=0.2, bbox_min_score=0.2, bbox_min_size=3, max_candidates=0,
                     output_format='standard'):
        '''
        Parameters:
        image: file path or numpy-array or a byte stream object
        '''
        img, img_cv_grey = reformat_input(image)

        horizontal_list, free_list = self.detect(img,
                                                 min_size=min_size, text_threshold=text_threshold, \
                                                 low_text=low_text, link_threshold=link_threshold, \
                                                 canvas_size=canvas_size, mag_ratio=mag_ratio, \
                                                 slope_ths=slope_ths, ycenter_ths=ycenter_ths, \
                                                 height_ths=height_ths, width_ths=width_ths, \
                                                 add_margin=add_margin, reformat=False, \
                                                 threshold=threshold, bbox_min_score=bbox_min_score, \
                                                 bbox_min_size=bbox_min_size, max_candidates=max_candidates
                                                 )
        # get the 1st result from hor & free list as self.detect returns a list of depth 3
        horizontal_list, free_list = horizontal_list[0], free_list[0]
        result = self.recognize(img_cv_grey, horizontal_list, free_list, \
                                decoder, beamWidth, batch_size, \
                                workers, allowlist, blocklist, detail, rotation_info, \
                                paragraph, contrast_ths, adjust_contrast, \
                                filter_ths, y_ths, x_ths, False, output_format)

        char = []
        directory = 'characters/'
        for i in range(len(result)):
            char.append(result[i][1])

        def search(arr, x):
            g = False
            for i in range(len(arr)):
                if arr[i] == x:
                    g = True
                    return 1
            if g == False:
                return -1

        def tupleadd(i):
            a = result[i]
            b = a + (filename[0:2],)
            return b

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open('characters/' + filename, 'rt', encoding="utf8") as myfile:
                    chartrs = str(myfile.read().splitlines()).replace('\n', '')
                    for i in range(len(char)):
                        res = search(chartrs, char[i])
                        if res != -1:
                            if filename[0:2] == "en" or filename[0:2] == "ch":
                                print(tupleadd(i))

    def readtext_batched(self, image, n_width=None, n_height=None, \
                         decoder='greedy', beamWidth=5, batch_size=1, \
                         workers=0, allowlist=None, blocklist=None, detail=1, \
                         rotation_info=None, paragraph=False, min_size=20, \
                         contrast_ths=0.1, adjust_contrast=0.5, filter_ths=0.003, \
                         text_threshold=0.7, low_text=0.4, link_threshold=0.4, \
                         canvas_size=2560, mag_ratio=1., \
                         slope_ths=0.1, ycenter_ths=0.5, height_ths=0.5, \
                         width_ths=0.5, y_ths=0.5, x_ths=1.0, add_margin=0.1,
                         threshold=0.2, bbox_min_score=0.2, bbox_min_size=3, max_candidates=0,
                         output_format='standard'):
        '''
        Parameters:
        image: file path or numpy-array or a byte stream object
        When sending a list of images, they all must of the same size,
        the following parameters will automatically resize if they are not None
        n_width: int, new width
        n_height: int, new height
        '''
        img, img_cv_grey = reformat_input_batched(image, n_width, n_height)

        horizontal_list_agg, free_list_agg = self.detect(img,
                                                         min_size=min_size, text_threshold=text_threshold, \
                                                         low_text=low_text, link_threshold=link_threshold, \
                                                         canvas_size=canvas_size, mag_ratio=mag_ratio, \
                                                         slope_ths=slope_ths, ycenter_ths=ycenter_ths, \
                                                         height_ths=height_ths, width_ths=width_ths, \
                                                         add_margin=add_margin, reformat=False, \
                                                         threshold=threshold, bbox_min_score=bbox_min_score, \
                                                         bbox_min_size=bbox_min_size, max_candidates=max_candidates
                                                         )
        result_agg = []
        # put img_cv_grey in a list if its a single img
        img_cv_grey = [img_cv_grey] if len(img_cv_grey.shape) == 2 else img_cv_grey
        for grey_img, horizontal_list, free_list in zip(img_cv_grey, horizontal_list_agg, free_list_agg):
            result_agg.append(self.recognize(grey_img, horizontal_list, free_list, \
                                             decoder, beamWidth, batch_size, \
                                             workers, allowlist, blocklist, detail, rotation_info, \
                                             paragraph, contrast_ths, adjust_contrast, \
                                             filter_ths, y_ths, x_ths, False, output_format))

        return result_agg
