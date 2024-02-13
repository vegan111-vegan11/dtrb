import os
import random
import shutil

lan = 'vi'
lan = 'la'

# 원본 이미지 경로 및 gt.txt 파일 경로
train_image_folder = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test\train\img'
train_gt_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test\train\gt\gt.txt'

train_image_folder = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf15\train\img'
train_gt_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf15\train\gt\gt.txt'

# 대상 이미지 경로와 gt.txt 파일 저장 경로
val_image_folder = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf15\val\img'
val_gt_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf15\val\gt\gt.txt'

train_image_folder = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\train\img'
train_gt_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}_gt.txt'

# 대상 이미지 경로와 gt.txt 파일 저장 경로
val_image_folder = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\val\img'
val_gt_file_path = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\val\gt\gt.txt'

train_image_folder = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\train\img'
train_gt_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}_gt.txt'
train_gt_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}\{lan}_gt.txt'

# 대상 이미지 경로와 gt.txt 파일 저장 경로
val_image_folder = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\val\img'
val_gt_file_path = fr'D:\deep-text-recognition-benchmark\data\{lan}\rect_invert\val\gt\gt.txt'

# 확률적으로 훈련 세트를 검증 세트로 변경할 확률
validation_percentage = 10
validation_percentage = 0.2


old = 'train'
new = 'val'

# gt.txt 파일 읽기
with open(train_gt_file_path, 'r', encoding='utf-8') as train_gt_file:
    train_gt_lines = train_gt_file.readlines()

os.makedirs(os.path.dirname(val_gt_file_path), exist_ok=True)

# 원본 이미지 폴더에서 랜덤으로 선택한 파일을 검증 세트로 복사
for root, dirs, files in os.walk(train_image_folder):

    print(f'root : {root}')
    print(f'dirs : {dirs}')
    print(f'files : {files}')

    t= random.sample(files, int(len(files) * validation_percentage))
    print(f'!!!!!!!!!len(files) : {len(files)}')
    print(f'!!!!!!!!!int(len(files) * validation_percentage) : {int(len(files) * validation_percentage)}')
    print(f'!!!!!!!!!t : {t}')

    for file in random.sample(files, int(len(files) * validation_percentage)):
        print(f'!!!!!!!!!file : {file}')

        if file.lower().endswith('.jpg'):
            # 이미지 파일 경로
            source_image_path = os.path.join(root, file)

            print(f'source_image_path : {source_image_path}')

            # # gt.txt 파일 읽기
            # with open(train_gt_file_path, 'r', encoding='utf-8') as train_gt_file:
            #     train_gt_lines = train_gt_file.readlines()

            # # gt.txt 파일 업데이트
            # #with open(val_gt_file_path, 'w', encoding='utf-8') as val_gt_file:
            # with open(val_gt_file_path, 'a', encoding='utf-8') as val_gt_file:
            #     for train_gt_line in train_gt_lines:
            #         # 파일명 추출 (확장자 전까지)
            #         file_name = os.path.splitext(file)[0]
            #
            #         # 파일명과 일치하는 라인만 수정
            #         #if line.split()[0] == file_name:
            #         if train_gt_line.split()[0] == source_image_path:
            #             #line = line.replace('train', 'val')
            #
            #             # gt.txt 파일에 쓰기
            #             val_gt_file.write(train_gt_line)

            # 이미지를 검증 세트로 복사
            #destination_image_path = os.path.join(val_image_folder, file)
            destination_image_path = source_image_path.replace(old, new)
            print(f'destination_image_path : {destination_image_path}')

            os.makedirs(os.path.dirname(destination_image_path), exist_ok=True)
            shutil.copy(source_image_path, destination_image_path)
