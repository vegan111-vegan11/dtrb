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


# 패딩 크기 정의
padding_size = 10
padding_size = 100

# 각 디렉터리에 대해 작업 수행
for root, dirs, files in os.walk(source_path):
    for dir_name in dirs:

        print(f'dir_name : {dir_name}')

        # 새로운 디렉터리 경로 생성
        source_dir_path = os.path.join(source_path, dir_name)
        target_dir_path = os.path.join(target_path, dir_name)

        print(f'source_dir_path : {source_dir_path}')
        print(f'target_dir_path : {target_dir_path}')

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
            if filename.lower().endswith('.jpg') and dir_name == 'NotoSansThaiLooped-Black':

                src_file_path = os.path.join(source_dir_path, filename)
                target_file_path = os.path.join(target_dir_path, filename)

                print(f'이건 정상으로 디렉토리일때 반복할때 filename : {filename}')
                src_image_path = os.path.join(source_dir_path, filename)
                print(f'이건 정상으로 디렉토리일때 반복할때 src_image_path : {src_image_path}')
                source_file_path = os.path.join(source_dir_path, filename)
                target_file_path = os.path.join(target_dir_path, filename)


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
                    print(f"x: {x}, y: {y}, w: {w}, h: {h}")

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
                #                 text_region = src_image.crop((1, 200, x_max, y_max))
                #                 text_region = src_image.crop((1, y - margin, x_max, y_max))

                # 결과 이미지 저장 (덮어쓰기)
                # text_region.save(image_path)
                text_region.save(target_file_path)

                print(f"Saved text region for {filename} in {target_dir_path}")

                # # 이미지에 패딩 추가
                # img_with_padding = ImageOps.expand(img, border=padding_size, fill='white')
                #
                # # 새로운 이미지 저장
                # img_with_padding.save(target_file_path)

                #print(f"{filename}에 패딩을 추가하여 저장 완료.")
