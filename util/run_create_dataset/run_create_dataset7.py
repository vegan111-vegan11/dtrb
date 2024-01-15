# 되는거
import os
import subprocess

import shutil
#import random  # random 모듈 추가
from random import sample

cmd = []
cmds = []
split_ratio = 0.8

def find_last_directory_with_jpg(directory_path, base_path):
    last_directory_with_jpg = None

    for dirpath, dirnames, filenames in os.walk(directory_path):
        if any(filename.lower().endswith('.jpg') for filename in filenames):
        # for filename in filenames:
        #     if filename.lower().endswith('.jpg'):
                # 만약 확장자가 '.jpg'로 끝난다면, 원하는 작업을 수행
                #print(f"{filename} is a JPG file")

                #src_path = os.path.join(dirpath, filename.lower() )
                # 현재 디렉토리에 jpg 파일이 있는 경우, 갱신
                last_directory_with_jpg = dirpath
                # src_path = os.path.join(dirpath, filename.lower())
                # print(f' src_path : {src_path}')

                # log 디렉토리 삭제
                #            log_directory = os.path.join(dirpath, 'log')
                #            if os.path.exists(log_directory):
                #                os.rmdir(log_directory)
                #            # mask_bbox 디렉토리 삭제
                #            mask_bbox_directory = os.path.join(dirpath, 'mask_bbox')
                #            if os.path.exists(mask_bbox_directory):
                #                os.rmdir(mask_bbox_directory)

                # "C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\" 부분 제거
                relative_path = os.path.relpath(last_directory_with_jpg, base_path)
                # print(f' relative_path : {relative_path}')

                # \data를 \data_lmdb_release로 교체
                # copy_path = last_directory_with_jpg.replace(r'\12-07-2', r'\ttf5')
                #copy_path = last_directory_with_jpg.replace(r'\12-07-2', r'\val')
                train_path = last_directory_with_jpg.replace(r'\test', r'\train')
                validation_path = last_directory_with_jpg.replace(r'\test', r'\val')

                # \data를 \data_lmdb_release로 교체
                # modified_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release\training')
                # mdb_path = last_directory_with_jpg.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf5')
                training_mdb_path = last_directory_with_jpg.replace(r'\data\test', r'\data_lmdb_release\training\test')
                validation_mdb_path = last_directory_with_jpg.replace(r'\data\test', r'\data_lmdb_release\validation\test')
                mdb_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release')
                mdb_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release')
        mdb_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release\th')
                print(f'mdb_path : {mdb_path}')

                gt_dir_path = last_directory_with_jpg.replace(r'\img', r'\gt')
                print(f'gt_dir_path : {gt_dir_path}')

                gt_path = os.path.join(gt_dir_path, 'gt.txt')
                print(f'gt_path : {gt_path}')

                #mdb_path = mdb_path.replace(r'\data\test', r'\data_lmdb_release\validation\test')

        # 특정 부분 제거
                target_subpath = r'\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)'
                # if target_subpath in relative_path:
                #mdb_path = mdb_path.replace(target_subpath, '')

                # if target_subpath in relative_path:
                #copy_path = copy_path.replace(target_subpath, '')
                #train_path = train_path.replace(target_subpath, '')
                #validation_path = validation_path.replace(target_subpath, '')
                # print(f' copy_path : {copy_path}')

                # 새로운 디렉토리 생성
                #os.makedirs(os.path.dirname(copy_path), exist_ok=True)
                #os.makedirs(copy_path, exist_ok=True)

                # 원본 데이터 파일 리스트 가져오기
                #print(f' src_path : {src_path}')
                #file_list = os.listdir(src_path)
                #file_list = os.listdir(dirpath)
                #print(f' file_list : {file_list}')

                # 데이터를 섞어서 나누기
                #alidation_size = int(len(file_list) * (1 - split_ratio))
                #validation_set = set(sample(file_list, validation_size))
                #print(f' validation_set : {validation_set}')
                #train_set = set(file_list) - validation_set
                # 전체 데이터를 훈련 데이터로 사용
                # 데이터가 많지 않은 경우에 유용
                #train_set = set(file_list)

                # 훈련 데이터 복사
                # for file_name in train_set:
                #     shutil.copy(os.path.join(src_path, file_name), os.path.join(train_path, file_name))

                # 검증 데이터 복사
                #for file_name in validation_set:
                    #shutil.copy(os.path.join(src_path, file_name), os.path.join(validation_path, file_name))
                    #shutil.copy(os.path.join(dirpath, file_name), os.path.join(validation_path, file_name))

                # 복사
                # print(f'Copying {src_path} to {copy_path}')
                # shutil.copy2(src_path, copy_path)
                #shutil.copy(src_path, copy_path)
                # 주의: dest_path가 이미 존재하면 삭제하거나 다른 이름으로 변경해야 합니다.
                # shutil.copytree(dirpath, copy_path)
                #            subpath_parts = target_subpath.split('\\')
                #            print(f'subpath_parts: {subpath_parts}')

                # 결과 출력
                # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!mdb_path : {mdb_path}')

                if not os.path.exists(mdb_path):
                    os.makedirs(mdb_path, exist_ok=True)
                    # print(f'디렉토리생성 mdb_path : {mdb_path}')

                # 테스트용
                # if relative_path == r'skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(20)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black':

                # 해당 경로 출력
                # print(f'mdb_path Path: {mdb_path}')

                # create_lmdb_dataset.py 실행
                cmd = [
                    'python', 'create_lmdb_dataset.py',
                    '--inputPath', dirpath,
                    #'--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
                    '--gtFile', gt_path,
                    '--outputPath', mdb_path
                ]

                cmd_str = ' '.join([
                    'python', 'create_lmdb_dataset.py',
                    '--inputPath', dirpath,
                    '--gtFile', gt_path,
                    '--outputPath', mdb_path
                ])

                # 결과 출력
                # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmd : {cmd}')
                # 결과 출력
                # print(f' cmd_str : {cmd_str}')
                cmds.append(cmd_str)
                subprocess.run(cmd)
    return cmd


# 사용 예시
src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'

src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'


src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'
directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'

src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'

directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test'

img_folder =  'test2/train'
img_folder =  'test2/train'
img_folder =  'test/train'
img_folder =  'test/train'
img_folder =  'test/val'
img_folder =  'test/train'
img_folder =  'test/val'
img_folder =  'test_0110/val'
img_folder =  'test_0110/train'
img_folder =  'test_0110/val'
#img_folder =  'test/train'

directory_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{img_folder}'
base_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{img_folder}'

cmd = find_last_directory_with_jpg(directory_path, base_path)
# 결과 출력
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmd : {cmd}')
import os

# 현재 작업 디렉토리 확인
current_working_directory = os.getcwd()
print("Current Working Directory:", current_working_directory)

# 현재 스크립트 파일의 절대 경로 확인
script_path = os.path.abspath(__file__)
print("Script Path:", script_path)

# 결과 출력
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!modified_paths : {modified_paths}')