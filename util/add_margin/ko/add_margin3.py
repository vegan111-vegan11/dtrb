from PIL import Image, ImageOps
import os
from shutil import copyfile
lan = 'ko'
# 원본 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train\img'

# 대상 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train2\img'

# 원본 이미지 경로
source_path = r'D:\img\line\vi'

# 대상 이미지 경로
target_path = r'D:\img\vi\margin'
# 원본 이미지 경로
source_path = fr'D:\img\line\{lan}'
source_path = fr'D:\img\라인명\{lan}'
# 대상 이미지 경로
target_path = fr'D:\img\{lan}\margin'


# 패딩 크기 정의
padding_size = 10
padding_size = 100
padding_size = 800

# 각 디렉터리에 대해 작업 수행
for root, dirs, files in os.walk(source_path):
    for dir_name in dirs:
        # 새로운 디렉터리 경로 생성
        source_dir_path = os.path.join(source_path, dir_name)
        target_dir_path = os.path.join(target_path, dir_name)

        # 새로운 디렉터리 생성
        os.makedirs(target_dir_path, exist_ok=True)

        # 각 디렉터리에 있는 jpg 파일 처리
        for filename in os.listdir(source_dir_path):
            # if filename.lower().endswith('.jpg'):
            # 테스트ㅇㅅㅇ
            # if filename.lower().endswith('.jpg') and filename == 'image-000000249.jpg' and dir_name == 'Black':
            # if filename.lower().endswith('.jpg') and dir_name == 'Black':
            # if filename.lower().endswith('.jpg') and dir_name == 'Bold':
            # if filename.lower().endswith('.jpg') and dir_name == 'ExtraBold':
            #if filename.lower().endswith('.jpg') and dir_name == 'ExtraLight':
            #if filename.lower().endswith('.jpg') and dir_name == 'Light':
            #if filename.lower().endswith('.jpg') and dir_name == 'Medium':
            #if filename.lower().endswith('.jpg') and dir_name == 'Regular':
            #if filename.lower().endswith('.jpg') and dir_name == 'SemiBold':
            #if filename.lower().endswith('.jpg'):
            #if filename.lower().endswith('.jpg') and dir_name == 'SemiBold':
            if filename.lower().endswith('.jpg'):
                source_file_path = os.path.join(source_dir_path, filename)
                target_file_path = os.path.join(target_dir_path, filename)

                # PIL을 사용하여 이미지 열기
                img = Image.open(source_file_path)

                # 이미지에 패딩 추가
                img_with_padding = ImageOps.expand(img, border=padding_size, fill='white')

                # 새로운 이미지 저장
                img_with_padding.save(target_file_path)

                print(f"{target_file_path}에 패딩을 추가하여 저장 완료.")
