import os
from shutil import copytree

# 기존 이미지 경로
source_path = r'C:\Users\TAMSystech\yjh\img\라인명4\태국어'

# 대체될 이미지 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train\img'

# font_dict 정의
font_dict = {'검정': 'Black', '굵게': 'Bold', '아주 굵게': 'ExtraBold',
             '아주 가늘게': 'ExtraLight', '가늘게': 'Light', '중간': 'Medium',
             '보통': 'Regular', '약간 굵게': 'SemiBold'}

# os.walk 함수를 사용하여 디렉터리를 탐색하고 파일을 복사
for root, dirs, files in os.walk(source_path):
    for dir_name in dirs:
        if dir_name in font_dict:
            source_dir_path = os.path.join(source_path, dir_name)
            target_dir_name = font_dict[dir_name]
            target_dir_path = os.path.join(target_path, target_dir_name)

            # 대체된 디렉터리 생성
            copytree(source_dir_path, target_dir_path)

            print(f"디렉터리 {dir_name}을(를) {target_dir_name}으로 대체하여 복사 완료.")
