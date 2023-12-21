import os
import shutil

source_folder = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-19'
#source_folder = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\test'
destination_folder = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf14\train\img'

# 필요없는 부분을 제거할 경로 문자열
remove_path = r'\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(1)'
src_replace_path = r'TextRecognitionDataGenerator\out3\th\test'
src_replace_path = r'TextRecognitionDataGenerator\out3\th\12-19'
dst_replace_path = r'deep-text-recognition-benchmark\data\ttf14\train\img'

src_ext = 'png'
dst_ext = 'jpg'

#common_path = r'C:\Users\TAMSystech\yjh\ipynb\'

# source_folder를 기준으로 폴더 내부의 파일을 찾기
for root, dirs, files in os.walk(source_folder):
    print(f'root, : {root,}')
    print(f'dirs : {dirs}')
    print(f'files : {files}')

    for file in files:
        if file.lower().endswith('.png'):  # jpg 파일만 선택
            source_path = os.path.join(root, file)
            print(f'source_path : {source_path}')

            # 필요없는 부분 제거
            new_path = source_path.replace(remove_path, '')
            print(f'필요없는 부분 제거 new_path : {new_path}')

            new_path = new_path.replace(src_replace_path, dst_replace_path)

            print(f'replace new_path : {new_path}')

            new_path = new_path.replace(src_ext, dst_ext)
            print(f'replace new_path2 JPG 로 : {new_path}')

            # 목적지 경로 생성 및 복사
            destination_path = os.path.join(destination_folder, new_path)
            #print(f'destination_path1 : {destination_path}')
            destination_path = new_path
            #print(f'destination_path2 : {destination_path}')

            # 파일 확장자 변경
            #destination_path = destination_path[:-3] + 'png'
            #print(f'destination_path : {destination_path}')
            # print(f'destination_path[:-3] : {destination_path[:-3]}')
            # print(f'destination_path[-3:] : {destination_path[-3: ]}')
            # #os.rename(destination_path, destination_path[:-3] + 'jpg')
            # os.rename(destination_path[-3:],  'jpg')
            # print(f'!!!!!!!!!!!!destination_path3 : {destination_path}')


            print(f'목적지 경로 생성 destination_path : {destination_path}')
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # 폴더가 없으면 생성
            shutil.copy(source_path, destination_path)



