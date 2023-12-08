# 되는거
# 되는거
import os
import subprocess
import shutil
import os

# 새로운 작업 디렉토리 경로
new_working_directory = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark'

# 디렉토리 변경
os.chdir(new_working_directory)

# 변경된 작업 디렉토리 확인
current_working_directory = os.getcwd()
# print(f'현재 작업 디렉토리: {current_working_directory}')

cmd = []
cmds = []
directory_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'


def find_last_directory_with_jpg(directory_path, base_path):
    last_directory_with_jpg = None

    for dirpath, dirnames, filenames in os.walk(directory_path):
        if any(filename.lower().endswith('.jpg') for filename in filenames):

            # src_path = os.path.join(dirpath, filename.lower() )
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
            relative_path_copy = relative_path
            # print(f' relative_path_copy : {relative_path_copy}')
            # relative_path_copy = '"' + relative_path_copy + '"'

            # print(f' relative_path : {relative_path}')

            # \data를 \data_lmdb_release로 교체
            copy_path = last_directory_with_jpg.replace(r'\12-07-2', r'\ttf5')

            # \data를 \data_lmdb_release로 교체
            # modified_path = last_directory_with_jpg.replace(r'\data', r'\data_lmdb_release\training')
            # mdb_path = last_directory_with_jpg.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf7')
            # mdb_path = relative_path.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf7')
            mdb_path = relative_path_copy
            # print(f' replace 적용 전 mdb_path : {mdb_path}')
            # mdb_path = relative_path.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf7')
            # print(f' replace 적용 후 ( data_lmdb_release 폴더에 생성 ) mdb_path : {mdb_path}')

            # mdb_path = relative_path_copy.replace(r'data\12-07-2', r'data_lmdb_release\training\ttf7')
            mdb_path = relative_path_copy.replace(r'data\12-07-2', r'data_lmdb_release\training\th\ttf7')
            # print(f' replace 적용 후2 ( data_lmdb_release 폴더에 생성 ) mdb_path : {mdb_path}')

            # updated_path = path.replace(r'\data\12-07-2', r'\data_lmdb_release\training\ttf7')

            # 특정 부분 제거
            target_subpath = r'\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)'

            # if target_subpath in relative_path:
            # relative_path = relative_path.replace(target_subpath, '')
            # if target_subpath in relative_path:
            copy_path = copy_path.replace(target_subpath, '')
            # print(f' copy_path : {copy_path}')
            mdb_path = mdb_path.replace(target_subpath, '')

            # mdb_path = '"' + mdb_path + '"'

            # 새로운 디렉토리 생성
            # os.makedirs(os.path.dirname(copy_path), exist_ok=True)
            # os.makedirs(copy_path, exist_ok=True)

            # 복사
            # print(f'Copying {src_path} to {copy_path}')
            # shutil.copy2(src_path, copy_path)
            # shutil.copy(src_path, copy_path)
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
            # if relative_path == r'data\12-07-2\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(20)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black':

            # 해당 경로 출력
            # print(f'mdb_path Path: {mdb_path}')

            # create_lmdb_dataset.py 실행
            #                cmd = [
            #                    'python', 'create_lmdb_dataset.py',
            #                    '--inputPath', relative_path_copy,
            #                    '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
            #                    '--outputPath', mdb_path
            #                ]
            run_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\create_lmdb_dataset.py'
            run_path = 'create_lmdb_dataset.py'
            cmd = [
                'python', run_path,
                '--inputPath', relative_path_copy,
                '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
                '--outputPath', mdb_path
            ]
            # print(f'cmd : {cmd}')
            relative_path_copy = fr'"{relative_path_copy}"'
            mdb_path = fr'"{mdb_path}"'
            # print(f' relative_path_copy 쌍따옴표 추가후 : {relative_path_copy}')

            #                cmd_str = ' '.join([
            #                    'python', 'create_lmdb_dataset.py',
            #                '--inputPath', relative_path_copy,
            #                '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
            #                '--outputPath', mdb_path
            #                ])
            cmd_str = ' '.join([
                'python', run_path,
                '--inputPath', relative_path_copy,
                '--gtFile', os.path.join('data', 'ttf', 'train2', 'gt', 'LGBD', '태국어', 'gt.txt'),
                '--outputPath', mdb_path
            ])

            # 결과 출력
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmd : {cmd}')
            # 결과 출력
            # print(f' cmd_str : {cmd_str}')
            cmds.append(cmd_str)
            # subprocess.run(cmd)
            # subprocess.run(cmd)
            result = subprocess.run(cmd, capture_output=True, text=True)
            # 결과 출력
            print("표준 출력:")
            print(result.stdout)
            print("표준 에러 출력:")
            print(result.stderr)
            # 종료 코드 출력
            print("종료 코드:", result.returncode)
    return cmds


# 사용 예시
src_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\12-07-2'
base_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark'
cmd = find_last_directory_with_jpg(directory_path, base_path)
# 결과 출력
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!cmds : {cmds}')
# 결과 출력
# print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!modified_paths : {modified_paths}')