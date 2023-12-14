# 되는거
import os
import subprocess

import shutil
#import random  # random 모듈 추가
from random import sample
import random
from pathlib import Path

cmd = []
cmds = []
split_ratio = 0.8
validation_ratio = 0.2

def find_last_directory_with_jpg(directory_path, base_path):
    last_directory_with_jpg = None

    for dirpath, dirnames, filenames in os.walk(directory_path):
        #if any(filename.lower().endswith('.jpg') for filename in filenames):

        # for filename in filenames:
        #     if filename.lower().endswith('.jpg'):
        if not dirnames:
                # 만약 확장자가 '.jpg'로 끝난다면, 원하는 작업을 수행
                #print(f"{filename} is a JPG file")

                #src_path = os.path.join(dirpath, filename.lower() )
                src_path = dirpath
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
                copy_path = last_directory_with_jpg.replace(r'\12-07-2', r'\val')
                train_path = last_directory_with_jpg.replace(r'\12-07-2', r'\train')
                validation_path = last_directory_with_jpg.replace(r'\12-07-2', r'\val')

                # \data를 \data_lmdb_release로 교체
                # modified_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release\training')
                # mdb_path = last_directory_with_jpg.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf5')
                mdb_path = last_directory_with_jpg.replace(r'\data\12-07-2', r'\data_lmdb_release\validation\ttf8')

                # 특정 부분 제거
                target_subpath = r'\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)'
                # if target_subpath in relative_path:
                mdb_path = mdb_path.replace(target_subpath, '')

                # if target_subpath in relative_path:
                copy_path = copy_path.replace(target_subpath, '')
                train_path = train_path.replace(target_subpath, '')
                validation_path = validation_path.replace(target_subpath, '')
                # print(f' copy_path : {copy_path}')
                #print(f' validation_path : {validation_path}')

                # 새로운 디렉토리 생성
                #os.makedirs(os.path.dirname(copy_path), exist_ok=True, encoding='utf-8')
                #os.makedirs(copy_path, exist_ok=True, encoding='utf-8')
                Path(copy_path).mkdir(parents=True, exist_ok=True)
                Path(validation_path).mkdir(parents=True, exist_ok=True)
                Path(mdb_path).mkdir(parents=True, exist_ok=True)

                # 원본 데이터 파일 리스트 가져오기
                #print(f' src_path : {src_path}')
                #file_list = os.listdir(src_path)
                file_list = os.listdir(dirpath)
                #print(f' file_list : {file_list}')
                #print(f' len(file_list) : {len(file_list)}')

                # 데이터를 섞어서 나누기
                #validation_size = int(len(file_list) * (1 - split_ratio))
                validation_size = int(len(file_list) * validation_ratio)
                #print(f' validation_size : {validation_size}')
                #validation_set = set(sample(file_list, validation_size))
                validation_set = set(random.sample(file_list, validation_size))

                #print(f' validation_set : {validation_set}')
                #print(f' len(validation_set) : {len(validation_set)}')
                #train_set = set(file_list) - validation_set
                # 전체 데이터를 훈련 데이터로 사용
                # 데이터가 많지 않은 경우에 유용
                train_set = set(file_list)

                # 훈련 데이터 복사
                # for file_name in train_set:
                #     shutil.copy(os.path.join(src_path, file_name), os.path.join(train_path, file_name))

                # 검증 데이터 복사
                # for file_name in validation_set:
                #     #shutil.copy(os.path.join(src_path, file_name), os.path.join(validation_path, file_name))
                #     shutil.copy(os.path.join(dirpath, file_name), os.path.join(validation_path, file_name))

                # 원본 데이터 파일 리스트 가져오기
                # file_list = [filename for filename in os.listdir(dirpath) if filename.lower().endswith('.jpg')]
                #
                # # 데이터를 섞어서 나누기
                # validation_size = int(len(file_list) * validation_ratio)
                #
                # # random.sample을 사용하여 일부를 검증 데이터로 선택
                # validation_set = set(random.sample(file_list, validation_size))
                #
                # # 검증 데이터 복사
                # for file_name in validation_set:
                #     src_file_path = os.path.join(dirpath, file_name)
                #     dst_file_path = os.path.join(validation_path, file_name)
                #     shutil.copy(src_file_path, dst_file_path)

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

                # if not os.path.exists(mdb_path):
                #     os.makedirs(mdb_path, exist_ok=True, encoding='utf-8')
                    # print(f'디렉토리생성 mdb_path : {mdb_path}')
                #Path(mdb_path).mkdir(parents=True, exist_ok=True)

                # 테스트용
                # if relative_path == r'skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(20)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black':

                # 해당 경로 출력
                # print(f'mdb_path Path: {mdb_path}')

                # create_lmdb_dataset.py 실행
                #print(f' validation_path 쌍따옴표 추가전 : {validation_path}')
                # validation_path = fr'"{validation_path}"'
                # mdb_path = fr'"{mdb_path}"'
                #print(f' validation_path 쌍따옴표 추가후 : {validation_path}')


                cmd = [
                    'python', 'create_lmdb_dataset.py',
                    #'--inputPath', dirpath,
                    '--inputPath', validation_path,
                    '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
                    '--outputPath', mdb_path
                ]

                cmd_str = ' '.join([
                    'python', 'create_lmdb_dataset.py',
                    #'--inputPath', dirpath,
                    '--inputPath', validation_path,
                    '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
                    '--outputPath', mdb_path
                ])

                # 결과 출력
                # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmd : {cmd}')
                # 결과 출력
                # print(f' cmd_str : {cmd_str}')
                cmds.append(cmd_str)
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')

                # 실행 결과 출력
                print("프로세스 종료 코드:", result.returncode)
                print("표준 출력:")
                print(result.stdout)
                print("표준 에러:")
                print(result.stderr)

                #subprocess.run(cmd)
                # 테스트용
                # if relative_path == r'skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(20)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black':
                #     print(f' 테스트용 들어옴 cmd : {cmd}')
                #     #subprocess.run(cmd)
                #     #result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                #     result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
                #
                #     # 실행 결과 출력
                #     print("프로세스 종료 코드:", result.returncode)
                #     print("표준 출력:")
                #     print(result.stdout)
                #     print("표준 에러:")
                #     print(result.stderr)
                    #print(f' 테스트용 들어옴 subprocess 완료 cmd : {cmd}')
    return cmd_str


# 사용 예시
src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
cmd_str = find_last_directory_with_jpg(directory_path, base_path)
# 결과 출력
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmd_str : {cmd_str}')
import os

# 현재 작업 디렉토리 확인
current_working_directory = os.getcwd()
print("Current Working Directory:", current_working_directory)

# 현재 스크립트 파일의 절대 경로 확인
script_path = os.path.abspath(__file__)
print("Script Path:", script_path)

# 결과 출력
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!modified_paths : {modified_paths}')