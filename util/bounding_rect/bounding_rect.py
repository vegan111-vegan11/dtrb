# import shutil
# import os
# import cv2
# import numpy as np
# 여기부터
# 경로 설정
src_base_dir_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf\train\img'
dest_base_dir_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf\train2\img'
src_base_dir_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train\img'
dest_base_dir_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train2\img'
# C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf\gt 경로의 디렉토리 루프
for root, dirs, files in os.walk(src_base_dir_path):
    print(f' root : {root}')
    print(f' dirs : {dirs}')
    print(f' files : {files}')

    if root == src_base_dir_path:
        print(f'개짜증나!!!!!! 디렉토리만 해야는데 루트일때도 디렉토리로 함 root : {root}')
        print(f'개짜증나!!!!!! 디렉토리만 해야는데 루트일때도 디렉토리로 함 dirs : {dirs}')

        for dir_name in dirs:
            print(f'개짜증나!!!!!! 디렉토리만 해야는데 루트일때도 디렉토리로 함 dir_name : {dir_name}')

            dest_dir_path = os.path.join(dest_base_dir_path, dir_name)
            os.makedirs(dest_dir_path, exist_ok=True)
            print(f'디렉토리 만듬 dest_dir_path : {dest_dir_path}')
        # continue

    else:

        for dir_name in dirs:

            # 현재 디렉토리에서 기준 경로를 뺀 상대 경로 생성
            rel_path = os.path.relpath(root, src_base_dir_path)
            print(f'  rel_path : {rel_path}')

            print(f'이건 정상으로 디렉토리일때 반복할때 root : {root}')
            print(f'이건 정상으로 디렉토리일때 반복할때 dirs : {dirs}')
            print(f'이건 정상으로 디렉토리일때 반복할때 dir_name : {dir_name}')
            src_dir_path = os.path.join(src_base_dir_path, rel_path, dir_name)
            dest_dir_path = os.path.join(dest_base_dir_path, rel_path, dir_name)
            print(f'이건 정상으로 디렉토리일때 반복할때 src_dir_path : {src_dir_path}')
            print(f'이건 정상으로 디렉토리일때 반복할때 dest_dir_path : {dest_dir_path}')

            #             src_file_path = os.path.join(src_dir_path, dir_name)
            #             dest_file_path = os.path.join(dest_dir_path, dir_name)

            os.makedirs(dest_dir_path, exist_ok=True)

            # 각 이미지에 대한 루프
            for filename in os.listdir(src_dir_path):
                print(f'이건 정상으로 디렉토리일때 반복할때 filename : {filename}')
                src_image_path = os.path.join(src_dir_path, filename)
                print(f'이건 정상으로 디렉토리일때 반복할때 src_image_path : {src_image_path}')
                src_file_path = os.path.join(src_dir_path, filename)
                dest_file_path = os.path.join(dest_dir_path, filename)

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
                text_region.save(dest_file_path)

                print(f"Saved text region for {filename} in {dest_dir_path}")

#             image_path = os.path.join(root, filename)

#             # 이미지 로드
#             image = Image.open(image_path)

#             # 이미지를 그레이스케일로 변환
#             img_cv_grey = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

#             # 이미지 이진화
#             _, binary = cv2.threshold(img_cv_grey, 128, 255, cv2.THRESH_BINARY_INV)

#             # 윤곽선 찾기
#             contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#             # 전체 텍스트 영역을 포함하는 bounding box 계산
#             x_min, y_min, x_max, y_max = float('inf'), float('inf'), 0, 0
#             for contour in contours:
#                 x, y, w, h = cv2.boundingRect(contour)
#                 x_min = min(x_min, x)
#                 y_min = min(y_min, y)
#                 x_max = max(x_max, x + w)
#                 y_max = max(y_max, y + h)

#             # 이미지에서 전체 텍스트 부분만 자르기
#             text_region = image.crop((x_min, y_min, x_max, y_max))

#             # 결과 이미지 저장 (덮어쓰기)
#             text_region.save(image_path)

###################################
# print(f"Saved text region for {filename} in {folder_name}")
#                   if(dir_name != 'failed'):


#                       # gt.txt 파일 복사
#                       src_file_path = os.path.join(src_base_dir_path, dir_name, 'gt.txt')
#                       dest_dir_path = os.path.join(dest_base_dir_path, rel_path)
#                       print(f' 디렉토리 dest_dir_path : {dest_dir_path}')
#                       dest_file_path = os.path.join(dest_dir_path, 'gt.txt')
#                       print(f' 파일명 dest_file_path : {dest_file_path}')

#                       # 디렉토리가 이미 존재하면 무시하고 계속 진행
#                       os.makedirs(dest_dir_path, exist_ok=True)
#                       # 디렉토리가 이미 존재하면 무시하고 계속 진행
#                       os.makedirs(dest_dir_path, exist_ok=True)

#                       # gt.txt 파일 복사
#                       #shutil.copy(src_file_path, dest_file_path)
#                       print(f'gt.txt 파일 src_file_path : {src_file_path}')
#                       print(f'gt.txt 파일 dest_file_path : {dest_file_path}')
