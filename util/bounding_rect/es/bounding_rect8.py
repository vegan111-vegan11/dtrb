from PIL import Image, ImageOps
import os
from shutil import copyfile
import shutil
import os
import cv2
import numpy as np

# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train\img'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train2\img'

# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train2\img'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train3\img'

# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2\train\img'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2_rect\train\img'

# 원본 이미지 경로
source_path = r'D:\img\line_invert\vi'

# 대상 이미지 경로
target_path = r'D:\img\vi\rect'

# 원본 이미지 경로
source_path = r'D:\img\line_invert\vi'

# 대상 이미지 경로
target_path = r'D:\img\vi\rect'

import os

# 확인할 경로
path_to_check = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2\train\img'

# 주어진 경로에 파일 또는 폴더가 존재하는지 확인
if os.path.exists(path_to_check):
    print(f'경로 {path_to_check}에 파일 또는 폴더가 존재합니다.')
else:
    print(f'경로 {path_to_check}에 파일 또는 폴더가 존재하지 않습니다.')

# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2\train\img\skew_angle(0.0)\blur(0.0)'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2_rect\train\img'

# 원본 이미지 경로
source_path = path_to_check

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2_rect\train\img'

# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2\train\img\skew_angle(0.0)\blur(0.0)'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\vi\test7_white_background_1800_760_2_rect\train\img\skew_angle(0.0)\blur(0.0)'

# 원본 이미지 경로
source_path = r'D:\img\line_invert\vi'

# 대상 이미지 경로
target_path = r'D:\img\vi\rect'



base_path = r'D:\img\out3\vi\01-30\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(1)'

# 원본 이미지 경로
source_path = r'D:\img\line_invert\vi'

# 대상 이미지 경로
target_path = r'D:\img\vi\rect'

# 원본 이미지 경로
source_path = r'D:\img\out3\vi\01-30\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(1)'

# 대상 이미지 경로
target_path = r'D:\img\out3\vi\rect\01-30\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(1)'

import os

import os

base_path = fr'D:\img\line_invert\vi'
source_path = fr'D:\img\line_invert\vi'
source_path = fr'D:\img\line\vi'

target_path = r'D:\img\out3\vi\rect\01-30\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(1)'
target_path = fr'D:\img\line_invert\vi'
target_path = fr'D:\img\vi\rect'

source_path = fr'D:\img\vi\margin'
target_path = fr'D:\img\vi\rect'

source_path = fr'D:\img\라인명\la'
source_path = fr'D:\img\라인명\test'
source_path = fr'D:\img\라인명\la'
target_path = fr'D:\img\la\rect'
source_path = fr'D:\img\라인명\vi_all'
target_path = fr'D:\img\vi_all\rect'

lan = 'es'

source_path = fr'D:\img\라인명\{lan}'
target_path = fr'D:\img\{lan}\rect'

# 패딩 크기 정의
padding_size = 10
padding_size = 100

# 각 디렉터리에 대해 작업 수행
for root, dirs, files in os.walk(source_path):
    for dir_name in dirs:

        print(f'dirs : {dirs}')
        print(f'dir_name : {dir_name}')

        # 새로운 디렉터리 경로 생성
        source_dir_path = os.path.join(source_path, dir_name)
        target_dir_path = os.path.join(target_path, dir_name)

        # source_dir_path = os.path.join(source_path, dir_name, dir_name)
        # target_dir_path = os.path.join(target_path, dir_name, dir_name)

        print(f'source_dir_path : {source_dir_path}')
        print(f'target_dir_path : {target_dir_path}')

        os.makedirs(target_dir_path, exist_ok=True)

        # 새로운 디렉터리 생성
        #os.makedirs(target_dir_path, exist_ok=True)

        # 각 디렉터리에 있는 jpg 파일 처리
        for filename in os.listdir(source_dir_path):
            #if filename.lower().endswith('.jpg'):
            # 테스트ㅇㅅㅇ
            #if filename.lower().endswith('.jpg') and filename == 'image-000000249.jpg' and dir_name == 'Black':
            #if filename.lower().endswith('.jpg') and dir_name == 'Black':
            #if filename.lower().endswith('.jpg') and dir_name == 'Bold':
            #if filename.lower().endswith('.jpg') and dir_name == 'ExtraBold':
            #if filename.lower().endswith('.jpg') and dir_name == 'ExtraLight':
            #if filename.lower().endswith('.jpg') and dir_name == 'Light':
            #if filename.lower().endswith('.jpg') and dir_name == 'Medium':
            #if filename.lower().endswith('.jpg') and dir_name == 'Regular':
            #if filename.lower().endswith('.jpg') and dir_name == 'NotoSansThaiLooped-Black':
            #if filename.lower().endswith('.jpg') and dir_name == 'Bold':
            if filename.lower().endswith('.jpg'):

                src_file_path = os.path.join(source_dir_path, filename)
                target_file_path = os.path.join(target_dir_path, filename)

                print(f'이건 정상으로 디렉토리일때 반복할때 filename : {filename}')
                src_image_path = os.path.join(source_dir_path, filename)
                print(f'이건 정상으로 디렉토리일때 반복할때 src_image_path : {src_image_path}')
                source_file_path = os.path.join(source_dir_path, filename)
                target_file_path = os.path.join(target_dir_path, filename)

                print(f'target_dir_path : {target_dir_path}')

                # 해당 디렉토리가 존재하지 않으면 생성
                #os.makedirs(target_dir_path, exist_ok=True)


                # 이미지 로드
                src_image = Image.open(src_image_path)

                # 이미지를 그레이스케일로 변환
                src_img_cv_grey = cv2.cvtColor(np.array(src_image), cv2.COLOR_BGR2GRAY)

                # 이미지 이진화
                _, src_binary = cv2.threshold(src_img_cv_grey, 128, 255, cv2.THRESH_BINARY_INV)


                # 윤곽선 찾기
                src_contours, _ = cv2.findContours(src_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # print(f"src_contours: {src_contours} ")

                # 전체 텍스트 영역을 포함하는 bounding box 계산
                x_min, y_min, x_max, y_max = float('inf'), float('inf'), 0, 0
                x_min, y_min, x_max, y_max = float('inf'), float('inf'), 0, 0

                # 추가할 여백 값
                margin = 5  # 예시로 10으로 설정하였습니다. 필요에 따라 조절하세요.
                margin = 5  # 예시로 10으로 설정하였습니다. 필요에 따라 조절하세요.

                for contour in src_contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    print(f"!!!!!!!!!!!!!!!!!!!!!!!x: {x}, y: {y}, w: {w}, h: {h}")

                    x_min = min(x_min, x)
                    y_min = min(y_min, y)
                    #                     x_min = x
                    #                     y_min = y
                    #                     x_min = min(x_min, x)
                    #                     y_min = min(y_min, y)
                    x_max = max(x_max, x + w)
                    y_max = max(y_max, y + h)

                    # 좌우 위 아래 여백 추가
                    #                     x_min = max(0, x_min - margin)
                    #                     y_min = max(0, y_min - margin)
                    #                     x_max += margin
                    #                     y_max += margin

                    #                     x_min = min(x_min, x_min - margin)
                    #                     y_min = min(y_min, y_min - margin)
                    #                     x_max += margin
                    #                     y_max += margin

                    x_min = x_min - margin
                    y_min = y_min - margin
                    x_max = x_max + margin
                    y_max = y_max + margin
                    # 결과 확인
                    print(f"x_min: {x_min}, y_min: {y_min}, x_max: {x_max}, y_max: {y_max}")

                # 이미지에서 전체 텍스트 부분만 자르기
                text_region = src_image.crop((x_min, y_min, x_max, y_max))
                text_region = src_image.crop((30, 30, 50, 50))
                text_region = src_image.crop((x_min, y_min, x_max, y_max))
                #                 text_region = src_image.crop((1, 200, x_max, y_max))
                #                 text_region = src_image.crop((1, y - margin, x_max, y_max))

                # 결과 이미지 저장 (덮어쓰기)
                # text_region.save(image_path)
                # 해당 디렉토리가 존재하지 않으면 생성
                # if not os.path.exists(target_file_path):
                #     os.makedirs(target_file_path)

                text_region.save(target_file_path)

                print(f"Saved text region for {filename} in {target_dir_path}")

                # # 이미지에 패딩 추가
                # img_with_padding = ImageOps.expand(img, border=padding_size, fill='white')
                #
                # # 새로운 이미지 저장
                # img_with_padding.save(target_file_path)

                #print(f"{filename}에 패딩을 추가하여 저장 완료.")
