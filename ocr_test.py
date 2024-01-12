# #pip install opencv-python
# #pip install --upgrade easyocr
# # 필요한 라이브러리를 임포트합니다.
# import easyocr
# print('임포트 함====')
# import pandas as pd
# import easyocr
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr_test.py import easyocr 완료 easyocr : {easyocr}')
#
# from PIL import Image
# #베트남어 전처리 1
# #윤정훈
# import os
# #pip install pillow
# import cv2
# import numpy as np
#
#
#
# # 엑셀 파일 읽기
# # 되는거 전처리 후
# # df = pd.read_excel('D:/data/베트남어/베트남어_전처리.xlsx')
# # df = pd.read_excel('D:/data/베트남어/베트남어_전처리.xlsx')
# file_path = 'D:/data/ocr/1107/베트남어_전처리_with_result_updated.xlsx'  # 엑셀 파일 경로
# df = pd.read_excel(file_path)
#
#
#
# ks_list = [1, 3, 5, 7, 9]
# ks_list = [1 ]
# # ocr_text_열명 = '베트남어_전처리_이진화_미디안필터_ocr_text'
# # result_열명 = '베트남어_전처리_이진화_미디안필터_result'
# ocr_text_열명 = '베트남어_ocr_text'
# result_열명 = '베트남어_result'
# ocr_text_열명 = '베트남어_전처리_미디안필터_kernel_7_ocr_text'
# result_열명 = '베트남어_전처리_미디안필터_kernel_7_result'
#
# # workbook = openpyxl.load_workbook(file_path)
# # worksheet = workbook.active  # 또는 다른 워크시트를 선택하세요
#
# 베트남어_suc_cnt = 0
# 베트남어_fail_cnt = 0
# # OCR 초기화
# # reader = easyocr.Reader(['th'])
# # reader = easyocr.Reader(['th', 'en'])
#
#
# custom_model_directory = 'C:/Users/TAMSystech/.EasyOCR/user_network'
# custom_model_name = 'thai.pth'
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr_test.py custom_model_directory : {custom_model_directory}')
#
# #reader = easyocr.Reader(['th', 'en'], model_storage_directory=custom_model_directory)
#
# user_network_directory = r'C:/Users/TAMSystech/.EasyOCR/user_network'
# #reader = easyocr.Reader(['th', 'en'], recog_network='None_VGG_BiLSTM_CTC')
# reader = easyocr.Reader(['th', 'en'] )
# #reader = easyocr.Reader(['es', 'en'])
# #reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC')
#
#
# #reader = easyocr.Reader(['th', 'en'], recog_network=os.path.join(user_network_directory, 'None-VGG-BiLSTM-CTC.yaml'))
#
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr_test.py reader : {reader}')
# # 모델 초기화
# #reader = easyocr.Reader(['th', 'en'], recog_network='None-VGG-BiLSTM-CTC')
# #reader = Reader(['en'], recog_network='custom_model.yaml' )
# kernel_size_option = 0
#
# # 이미지 디렉토리 설정
# image_dir = 'C:/Users/TAMSystech/yjh/img/베트남어'
# image_dir = 'C:/Users/TAMSystech/yjh/img/백업/1017/thai_img'
# image_dir = 'C:/Users/TAMSystech/yjh/img/백업/1017/test'
#
# for ks in ks_list:
#
#     베트남어_suc_cnt = 0
#     베트남어_fail_cnt = 0
#
#     # 이미지 루프
#     for filename in os.listdir(image_dir):
#         if filename.endswith(".png"):  # 혹은 다른 이미지 확장자를 사용하시면 변경해주십시오.
#
#             image_path = os.path.join(image_dir, filename)
#
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr_test 루프 image_path  : {image_path}')
#
#
#             image = Image.open(image_path)
#             # 이미지에서 텍스트 인식
#             # results = reader.readtext(image_path)
#             # 이미지를 그레이스케일로 변환
#             img_cv_grey = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
#             print(img_cv_grey.shape)  # 이미지의 차원 확인
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr test img_cv_grey.shape : {img_cv_grey.shape}')
#
#             # 한국어는 침식 사용
#             # 언어마다 전처리 다 다름
#             # 정확도 높은 전처리를 선택할 예정
#
#             # 이진화 적용
#             # _, img_cv_bin = cv2.threshold(img_cv_grey, 128, 255, cv2.THRESH_BINARY)
#             # for ks in ks_list:
#             ocr_text_열명 = f'베트남어_전처리_미디안필터_kernel_{ks}_ocr_text'
#             result_열명 = f'베트남어_전처리_미디안필터_kernel_{ks}_result'
#             # 이미지에 미디안 필터 적용
#
#             img_cv_filtered = cv2.medianBlur(img_cv_grey, ks)  # 숫자는 커널 크기, 조절 가능
#             #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr test img_cv_filtered : {img_cv_filtered }')
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr test results 여기서 에러 img_cv_filtered.shape : {img_cv_filtered.shape}')
#             # 작은 커널 크기(3x3)를 사용하여 OCR 전처리를 수행
#             results = reader.readtext(img_cv_filtered)
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr results = reader.readtext(img_cv_filtered) : {results}')
#
#             # OCR 결과를 저장할 리스트
#             recognized_words = []
#             # OCR 결과에서 bbox를 사용하여 단어들을 위치에 따라 정렬
#             results.sort(key=lambda x: x[0][0][0])  # 결과를 x 좌표를 기준으로 정렬
#
#             # 정렬된 결과를 출력
#             for (bbox, text, prob) in results:
#                 recognized_words.append(text)
#
#             # OCR 결과 리스트를 문자열로 결합
#             recognized_text = ' '.join(recognized_words)
#             print(f'정렬된 결과를 출력 filename : {filename}')
#             print(f'정렬된 결과를 출력 recognized_words : {recognized_words}')
#             print(f'정렬된 결과를 출력 recognized_text : {recognized_text}')
#
#             # OCR 결과 순회
#             # 파일명에서 확장자 제거, 좌우 공백 및 마침표 제거
#             filename = os.path.splitext(filename)[0].strip().replace('.', '')
#             print(f'파일명에서 확장자 제거, 좌우 공백 및 마침표 제거 filename : {filename}')
#             # filename과 같은 베트남어 열의 인덱스를 찾습니다.
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ocr test df : {df}')
#             idx = df.index[df['베트남어'] == filename].tolist()
#
#             if not idx:
#                 print(f'같은 열 없음 filename : {filename}')
#             else:
#                 print(f'========같은 열 있음 idx : {idx}')
#                 print(f'========같은 열 있음 image filename : {filename}')
#                 print(f'========같은 열 있음 recognized_text : {recognized_text}')
#
#                 # 추출된 텍스트를 '베트남어_ocr_text' 열에 넣습니다.
#                 df.at[idx[0], ocr_text_열명] = recognized_text
#                 #print(f'========같은 열 있음 recognized_text : {recognized_text}')
#
#                 # OCR 결과를 업데이트
#
#                 if recognized_text == df.at[idx[0], '베트남어']:
#                     df.at[idx[0], result_열명] = 'suc'
#                     베트남어_suc_cnt += 1
#                     print(f'#################같은 열 있음 성공   베트남어_suc_cnt : {베트남어_suc_cnt}')
#
#                 else:
#                     df.at[idx[0], result_열명] = 'fail'
#                     베트남어_fail_cnt += 1
#                     print(f'#################fail 같은 열 있음  베트남어_fail_cnt : {베트남어_fail_cnt}')
#
#             continue  # 일치하는 항목이 없는 경우 다음 이미지로 이동
#
#     last_row_index = df.index[-1]  # 가장 마지막 행의 인덱스
#     next_row_index = last_row_index + 1  # 다음 행의 인덱스
#     print(f"last_row_index: {last_row_index}")
#     print(f"next_row_index: {next_row_index}")
#     베트남어_tot_cnt = 베트남어_suc_cnt + 베트남어_fail_cnt
#
#     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!베트남어_suc_cnt : {베트남어_suc_cnt}')
#     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!베트남어_fail_cnt : {베트남어_fail_cnt}')
#     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!베트남어_tot_cnt : {베트남어_tot_cnt}')
#
#     #베트남어_성공률 = round(베트남어_suc_cnt / 베트남어_tot_cnt, 2)
#     if 베트남어_suc_cnt != 0:
#         베트남어_성공률 = round(베트남어_suc_cnt / 베트남어_tot_cnt, 2)
#     else:
#         베트남어_성공률 = 0.00  # 또는 다른 값을 지정해도 됨
#     # 소수 셋째 자리에서 반올림하여 나타냅니다.
#     # 베트남어_tot_cnt = round(베트남어_tot_cnt, 2)
#     # 다음 행에 '베트남어_전처리1_result' 열에 값을 설정
#     # df.at[next_row_index, result_열명] = 베트남어_suc_cnt
#     df.at[next_row_index, result_열명] = f'{베트남어_suc_cnt} / {베트남어_tot_cnt} ( {베트남어_성공률} )'
#
#     print(f"베트남어_suc_cnt:@@@@@@@@@@@@@@@@@@@@@@@@@ {베트남어_suc_cnt}")
#     df.to_excel('D:/data/ocr/1107/베트남어_전처리_with_result_updated.xlsx', index=False)
#
# print(f"일치하는 항목 수: {베트남어_suc_cnt}")


import cv2
import easyocr
import os
import pandas as pd
import numpy as np
from PIL import Image

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

lan = 'vi'

# 나머지 코드에서 Image 모듈을 사용할 수 있음

# 엑셀 파일 경로
file_path = fr'D:/data/ocr/1018/베트남어_전처리_with_result_updated.xlsx'
file_path = fr'D:/data/ocr/1215/베트남어_전처리_with_result_updated.xlsx'
file_path = fr'D:/data/ocr/1226/베트남어_전처리_with_result_updated.xlsx'
file_path = fr'C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/1226/{lan}/{lan}_전처리_with_result_updated.xlsx'
file_path = fr'C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/0110/{lan}/{lan}_전처리_with_result_updated.xlsx'

df = pd.read_excel(file_path)
ks_list = [1, 3, 5, 7, 9]
ks_list = [1]
ks_list = [7]
ks_list = [3]
ks_list = [5, 7, 9]
ks_list = [1]
ks_list = [3]
#def imageProcessing(image_path):
def imageProcessing(image_path):

    # 이미지를 그레이스케일로 읽어옵니다.
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 이미지가 제대로 로드되었는지 확인합니다.
    if image is None:
        #logger.debug("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
        raise ValueError("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")

    # Adaptive Thresholding을 적용하여 글자를 더욱 선명하게 합니다.
    sharpened_image = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    # 세로 선을 감지하기 위한 구조 요소를 생성합니다.
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))

    # erode와 dilate를 적용하여 세로 선을 제거합니다.
    # 이로 인해 글자가 더 얇게 보일 것입니다.
    sharpened_image = cv2.erode(sharpened_image, vertical_kernel, iterations=1)
    c = cv2.dilate(sharpened_image, vertical_kernel, iterations=1)

    point = 7

    # Gaussian Blur를 적용합니다.
    blurred_image = cv2.GaussianBlur(sharpened_image, (point, point), 0)

    # 다시 이진화를 적용합니다.
    _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 결과 이미지를 저장합니다.
    #cv2.imwrite(image_path, binary_image)

    #logger.debug("전처리 변경 완료")

    # 변경된 이미지를 반환합니다.
    return binary_image


# 전처리 단계 리스트
#preprocessing_steps = [
#     ('Original', lambda img: img),  # ,  # 원본 이미지를 그대로 반환
#     ('CannyEdge', lambda img: cv2.Canny(img, 50, 150)),
#     ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
#     ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))),
#     #('BinaryThresholding', lambda img: cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
#     ('imageProcessing', lambda img: cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
#
# ]

preprocessing_steps = [
    # ('Original', lambda img: img),  # ,  # 원본 이미지를 그대로 반환
    # ('CannyEdge', lambda img: cv2.Canny(img, 50, 150)),
    # ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
    # ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))),
    # #('BinaryThresholding', lambda img: cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    #('imageProcessing', lambda img: imageProcessing(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    ('imageProcessing', lambda img: imageProcessing(image_path))

]

preprocessing_steps = [
    #('Original', lambda img: img),  # ,  # 원본 이미지를 그대로 반환
    # ('CannyEdge', lambda img: cv2.Canny(img, 50, 150)),
    # ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
    ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))),
    # #('BinaryThresholding', lambda img: cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    #('imageProcessing', lambda img: imageProcessing(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
    ('imageProcessing', lambda img: imageProcessing(image_path))

]

# preprocessing_steps = [
#     # ('Original', lambda img: img),  # ,  # 원본 이미지를 그대로 반환
#     # ('CannyEdge', lambda img: cv2.Canny(img, 50, 150)),
#     # ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
#     ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])))#,
#     # #('BinaryThresholding', lambda img: cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
#     #('imageProcessing', lambda img: imageProcessing(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
#     #('imageProcessing', lambda img: imageProcessing(image_path))
#
# ]

# preprocessing_steps = [
#     ('Original', lambda img: img)  # ,  # 원본 이미지를 그대로 반환
#     # ('CannyEdge', lambda img: cv2.Canny(img, 50, 150))#,
#     #     ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
#     #     ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])))
# ]

# OCR 초기화
#reader = easyocr.Reader(['th'])
#reader = easyocr.Reader(['th', 'en'])
reader = easyocr.Reader(['vi'])

# #reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC')
# user_network_directory = r'C:/Users/TAMSystech/.EasyOCR/user_network'
user_network_directory = r'C:/Users/TAMSystech/.EasyOCR/user_network'
#reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC')
#reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC_custom')
#reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC_custom')
#reader = easyocr.Reader(['th', 'en'], model_storage_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC_th')
#reader = easyocr.Reader(['th', 'en'], user_network_directory = user_network_directory, recog_network='None_VGG_BiLSTM_CTC_th')

# 이미지 디렉토리 설정
image_dir = 'C:/Users/TAMSystech/yjh/img/베트남어'
image_dir = 'C:/Users/TAMSystech/yjh/img/라인명4/베트남어'
image_dir = 'C:/Users/TAMSystech/yjh/ipynb/deep-text-recognition-benchmark/data/ttf14/train/img/skew_angle(0.0)/blur(0.0)'

import os

# 주어진 경로
base_path = r'C:\Users\TAMSystech\yjh\img\라인명4\베트남어'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img\skew_angle(0.0)\blur(0.0)'

#테스트용
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test3\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test5\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test4\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test6\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_2\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background\train\img\skew_angle(0.0)\blur(0.0)'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_1410_1110_2\train\img\skew_angle(0.0)\blur(0.0)'
import os

# 경로 설정
gt_base_path = r'C:\Users\TAMSystech\yjh\gt\베트남어'
gt_base_path = r'C:\Users\TAMSystech\yjh\gt\베트남어'
gt_base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background\train\gt\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
gt_base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data'
gt_base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data'
gt_file_path = os.path.join(gt_base_path, 'gt.txt')

base_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760\train\img\skew_angle(0.0)\blur(0.0)'
base_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}\train\img\skew_angle(0.0)\blur(0.0)'


# 경로 설정
gt_base_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\gt'
gt_file_path = os.path.join(gt_base_path, 'gt.txt')

# 딕셔너리 생성
filename_gt_dict = {}

# gt.txt 파일 읽어오기
with open(gt_file_path, 'r', encoding='utf-8') as gt_file:
    gt_lines = gt_file.readlines()

# 딕셔너리에 값 할당
for line in gt_lines:
    values = line.strip().split('\t')
    if len(values) >= 2:
        filename, gt = values[0], values[1]
        filename_gt_dict[filename] = gt

print(f'========filename_gt_dict : {filename_gt_dict}')

# 디렉토리를 반복하면서 출력
for root, dirs, files in os.walk(base_path):

    #print(f'========root : {root}')
    #print(f'========dirs : {dirs}')
    # print(f'========files : {files}')

    for dir_name in dirs:

        #print(f'========dir_name : {dir_name}')
        # print(f'========filename : {filename}')

        dir_path = os.path.join(root, dir_name)
        # print(f'========dir_path : {dir_path}')
        image_dir = os.path.join(root, dir_name)
        #print(f'========image_dir : {image_dir}')

        for ks in ks_list:

            베트남어_suc_cnt = 0
            베트남어_fail_cnt = 0

            for preprocessing_name, preprocessing_func in preprocessing_steps:
                success_count = 0
                fail_count = 0
                베트남어_tot_cnt = 0
                베트남어_succ_cnt = 0
                베트남어_fail_cnt = 0
                # print(f'========img : {img}')
                #print(f'========preprocessing_func : {preprocessing_func}')
                #print(f'========preprocessing_name : {preprocessing_name}')
                # for filename in os.listdir(image_dir):
                for filename in os.listdir(image_dir):
                    # if filename.endswith(".png"):
                    if filename.endswith(".jpg"):

                        #image_path = os.path.join(image_dir, filename)
                        image_path = os.path.join(image_dir, filename)
                        image = Image.open(image_path)
                        # 이미지에서 텍스트 인식
                        # results = reader.readtext(image_path)
                        # 이미지를 그레이스케일로 변환
                        img_cv_grey = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
                        #print(img_cv_grey.shape)  # 이미지의 차원 확인

                        # 한국어는 침식 사용
                        # 언어마다 전처리 다 다름
                        # 정확도 높은 전처리를 선택할 예정

                        # 이진화 적용
                        # _, img_cv_bin = cv2.threshold(img_cv_grey, 128, 255, cv2.THRESH_BINARY)
                        # for ks in ks_list:
                        ocr_text_열명 = fr'{lan}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_ocr_text'
                        result_열명 = fr'{lan}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_result'
                        ocr_text_열명 = fr'{lan}_{dir_name}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_ocr_text'
                        result_열명 = fr'{lan}_{dir_name}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_result'
                        # 이미지에 미디안 필터 적용

                        img_cv_filtered = cv2.medianBlur(img_cv_grey, ks)  # 숫자는 커널 크기, 조절 가능
                        # 작은 커널 크기(3x3)를 사용하여 OCR 전처리를 수행
                        # results = reader.readtext(img_cv_filtered)

                        #image_path = os.path.join(image_dir, filename)
                        print(f'========image_path : {image_path}')
                        print(f'========preprocessing_name : {preprocessing_name}')
                        print(f'========image_path : {image_path}')

                        # image = cv2.imread(image_path)
                        #preprocessed_image = preprocessing_func(img_cv_filtered)
                        #if preprocessing_name != imageProcessing:
                        if preprocessing_name != 'imageProcessing':
                            preprocessed_image = preprocessing_func(img_cv_filtered)
                        else:
                            preprocessed_image = preprocessing_func(image_path)

                        t = type(preprocessed_image)
                        #print(f'========type : {t}')
                        # print(f'========같은 열 있음 filename : {filename}')

                        # 이미지에서 텍스트 인식
                        results = reader.readtext(preprocessed_image)
                        print(f'ocr_test.py results : {results}')

                        # OCR 결과를 저장할 리스트
                        recognized_words = []
                        # OCR 결과에서 bbox를 사용하여 단어들을 위치에 따라 정렬
                        results.sort(key=lambda x: x[0][0][0])  # 결과를 x 좌표를 기준으로 정렬

                        # 정렬된 결과를 출력
                        for (bbox, text, prob) in results:
                            recognized_words.append(text)

                        # OCR 결과 리스트를 문자열로 결합
                        recognized_text = ' '.join(recognized_words)
                        #print(f'정렬된 결과를 출력 recognized_words : {recognized_words}')

                        # OCR 결과 순회
                        # 파일명에서 확장자 제거, 좌우 공백 및 마침표 제거
                        # filename = os.path.splitext(filename)[0].strip().replace('.', '')
                        #print(f'수정전 filename : {filename}')
                        filename = filename_gt_dict[filename]
                        #print(f'수정후 filename : {filename}')
                        #                         # gt.txt 파일 읽어오기
                        #                         with open(gt_file_path, 'r', encoding='utf-8') as gt_file:
                        #                             gt_lines = gt_file.readlines()

                        #                         # 라인별로 반복하면서 처리
                        #                         for line in gt_lines:
                        #                             # 탭으로 스플릿
                        #                             values = line.strip().split('\t')

                        #                             if len(values) >= 2:
                        #                                 filename, new_value = values[0], values[1]

                        #                                 # filename과 같은 파일이 존재하면 덮어쓰기
                        #                                 target_file_path = os.path.join(base_path, filename)
                        #                                 if os.path.exists(target_file_path):
                        #                                     with open(target_file_path, 'w', encoding='utf-8') as target_file:
                        #                                         target_file.write(new_value)

                        #                         print("작업 완료.")

                        # filename과 같은 베트남어 열의 인덱스를 찾습니다.
                        idx = df.index[df['베트남어'] == filename].tolist()
                        print(f'filename: {filename}')
                        print(f'idx: {idx}')

                        if not idx:
                            print(f'같은 열 없음 filename : {filename}')
                        else:
                            print(f'========같은 열 있음 filename : {filename}')
                            #print(f'========같은 열 있음 idx : {idx}')
                            print(f'========같은 열 있음 recognized_text : {recognized_text}')

                            # 추출된 텍스트를 '베트남어_ocr_text' 열에 넣습니다.
                            df.at[idx[0], ocr_text_열명] = recognized_text
                            # 업데이트 조건과 값
                            condition = (df['베트남어'] == filename)

                            # 조건을 만족하는 모든 행 업데이트
                            df.loc[condition, ocr_text_열명] = recognized_text

                            #print(f'========같은 열 있음 recognized_text : {recognized_text}')

                            # OCR 결과를 업데이트

                            if recognized_text == df.at[idx[0], '베트남어']:
                                df.at[idx[0], result_열명] = 'suc'
                                # 조건을 만족하는 모든 행 업데이트
                                df.loc[condition, result_열명] = 'suc'

                                베트남어_suc_cnt += 1
                                #print(f'#################같은 열 있음 성공   베트남어_suc_cnt : {베트남어_suc_cnt}')

                            else:
                                df.at[idx[0], result_열명] = 'fail'
                                # 조건을 만족하는 모든 행 업데이트
                                df.loc[condition, result_열명] = 'fail'

                                베트남어_fail_cnt += 1
                                #print(f'#################failfailfail 같은 열 있ㄴ,ㄴ  베트남어_fail_cnt : {베트남어_fail_cnt}')

                        continue  # 일치하는 항목이 없는 경우 다음 이미지로 이동

                last_row_index = df.index[-1]  # 가장 마지막 행의 인덱스
                next_row_index = last_row_index + 1  # 다음 행의 인덱스
                print(f"last_row_index: {last_row_index}")
                print(f"next_row_index: {next_row_index}")
                베트남어_tot_cnt = 베트남어_suc_cnt + 베트남어_fail_cnt
                베트남어_성공률 = round(베트남어_suc_cnt / 베트남어_tot_cnt, 2)
                # 소수 셋째 자리에서 반올림하여 나타냅니다.
                # 베트남어_tot_cnt = round(베트남어_tot_cnt, 2)
                # 다음 행에 '베트남어_전처리1_result' 열에 값을 설정
                # df.at[next_row_index, result_열명] = 베트남어_suc_cnt
                df.at[next_row_index, result_열명] = f'{베트남어_suc_cnt} / {베트남어_tot_cnt} ( {베트남어_성공률} )'

                print(f"베트남어_suc_cnt:@@@@@@@@@@@@@@@@@@@@@@@@@ {베트남어_suc_cnt}")
                # df.to_excel('D:/data/ocr/1018/베트남어_전처리_with_result_updated.xlsx', index=False)
                #df.to_excel('D:/data/ocr/1215/베트남어_전처리_with_result_updated.xlsx', index=False)
                # df.to_excel('D:/data/ocr/1226/베트남어_전처리_with_result_updated.xlsx', index=False)
                # df.to_excel('C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/1226/베트남어_전처리_with_result_updated.xlsx', index=False)
                # df.to_excel(
                #     'C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/0110/베트남어_전처리_with_result_updated.xlsx',
                #     index=False)
                # df.to_excel(
                #     fr'C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/0110/{lan}/{lan}_전처리_with_result_updated_test7_white_background_1800_760_kernel_3_원본.xlsx',
                #     index=False)
                df.to_excel(
                    fr'C:/Users/TAMSystech\yjh\ipynb\deep-text-recognition-benchmark/ocr_test/0110/{lan}/{lan}_전처리_with_result_updated_test7_white_background_1800_760_{2}_kernel_3_원본.xlsx',
                    index=False)


        print(f"일치하는 항목 수: {베트남어_suc_cnt}")
