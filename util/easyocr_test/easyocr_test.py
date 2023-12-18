import cv2
import easyocr
import os
import pandas as pd
import numpy as np

# 엑셀 파일 경로
file_path = 'D:/data/ocr/1018/태국어_전처리_with_result_updated.xlsx'
file_path = 'D:/data/ocr/1215/태국어_전처리_with_result_updated.xlsx'
df = pd.read_excel(file_path)
ks_list = [1, 3, 5, 7, 9]
ks_list = [1]

# 전처리 단계 리스트
preprocessing_steps = [
    ('CannyEdge', lambda img: cv2.Canny(img, 50, 150)),
    ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
    ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])))
]
preprocessing_steps = [
    ('Original', lambda img: img)  # ,  # 원본 이미지를 그대로 반환
    # ('CannyEdge', lambda img: cv2.Canny(img, 50, 150))#,
    #     ('Dilation', lambda img: cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)),
    #     ('Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])))
]

# OCR 초기화
reader = easyocr.Reader(['th'])
reader = easyocr.Reader(['th', 'en'])

# 이미지 디렉토리 설정
image_dir = 'C:/Users/TAMSystech/yjh/img/태국어'
image_dir = 'C:/Users/TAMSystech/yjh/img/라인명4/태국어'

import os

# 주어진 경로
base_path = r'C:\Users\TAMSystech\yjh\img\라인명4\태국어'
import os

# 경로 설정
gt_base_path = r'C:\Users\TAMSystech\yjh\gt\태국어'
gt_file_path = os.path.join(gt_base_path, 'gt.txt')

# 딕셔너리 생성
filename_gt_dict = {}

# gt.txt 파일 읽어오기
with open(gt_file_path, 'r', encoding='utf-8') as gt_file:
    gt_lines = gt_file.readlines()

# 딕셔너리에 값 할당
for line in gt_lines:
    values = line.strip().split('\t')
    if len(values) >= 2:
        filename, gt = values[0], values[1]
        filename_gt_dict[filename] = gt

print(f'========filename_gt_dict : {filename_gt_dict}')

# 디렉토리를 반복하면서 출력
for root, dirs, files in os.walk(base_path):

    print(f'========root : {root}')
    print(f'========dirs : {dirs}')
    # print(f'========files : {files}')

    for dir_name in dirs:

        print(f'========dir_name : {dir_name}')
        # print(f'========filename : {filename}')

        dir_path = os.path.join(root, dir_name)
        # print(f'========dir_path : {dir_path}')
        image_dir = os.path.join(root, dir_name)
        print(f'========image_dir : {image_dir}')

        for ks in ks_list:

            for preprocessing_name, preprocessing_func in preprocessing_steps:
                success_count = 0
                fail_count = 0
                태국어_tot_cnt = 0
                태국어_succ_cnt = 0
                태국어_fail_cnt = 0
                # print(f'========img : {img}')
                print(f'========preprocessing_func : {preprocessing_func}')
                print(f'========preprocessing_name : {preprocessing_name}')
                # for filename in os.listdir(image_dir):
                for filename in os.listdir(image_dir):
                    # if filename.endswith(".png"):
                    if filename.endswith(".jpg"):

                        image_path = os.path.join(image_dir, filename)
                        image_path = os.path.join(image_dir, filename)
                        image = Image.open(image_path)
                        # 이미지에서 텍스트 인식
                        # results = reader.readtext(image_path)
                        # 이미지를 그레이스케일로 변환
                        img_cv_grey = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
                        print(img_cv_grey.shape)  # 이미지의 차원 확인

                        # 한국어는 침식 사용
                        # 언어마다 전처리 다 다름
                        # 정확도 높은 전처리를 선택할 예정

                        # 이진화 적용
                        # _, img_cv_bin = cv2.threshold(img_cv_grey, 128, 255, cv2.THRESH_BINARY)
                        # for ks in ks_list:
                        ocr_text_열명 = f'태국어_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_ocr_text'
                        result_열명 = f'태국어_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_result'
                        ocr_text_열명 = f'태국어_{dir_name}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_ocr_text'
                        result_열명 = f'태국어_{dir_name}_전처리_미디안필터_kernel_{ks}_{preprocessing_name}_result'
                        # 이미지에 미디안 필터 적용

                        img_cv_filtered = cv2.medianBlur(img_cv_grey, ks)  # 숫자는 커널 크기, 조절 가능
                        # 작은 커널 크기(3x3)를 사용하여 OCR 전처리를 수행
                        # results = reader.readtext(img_cv_filtered)

                        image_path = os.path.join(image_dir, filename)
                        print(f'========image_path : {image_path}')

                        # image = cv2.imread(image_path)
                        preprocessed_image = preprocessing_func(img_cv_filtered)
                        t = type(preprocessed_image)
                        print(f'========type : {t}')
                        # print(f'========같은 열 있음 filename : {filename}')

                        # 이미지에서 텍스트 인식
                        results = reader.readtext(preprocessed_image)
                        print(f'results : {results}')

                        # OCR 결과를 저장할 리스트
                        recognized_words = []
                        # OCR 결과에서 bbox를 사용하여 단어들을 위치에 따라 정렬
                        results.sort(key=lambda x: x[0][0][0])  # 결과를 x 좌표를 기준으로 정렬

                        # 정렬된 결과를 출력
                        for (bbox, text, prob) in results:
                            recognized_words.append(text)

                        # OCR 결과 리스트를 문자열로 결합
                        recognized_text = ' '.join(recognized_words)
                        print(f'정렬된 결과를 출력 recognized_words : {recognized_words}')

                        # OCR 결과 순회
                        # 파일명에서 확장자 제거, 좌우 공백 및 마침표 제거
                        # filename = os.path.splitext(filename)[0].strip().replace('.', '')
                        print(f'수정전 filename : {filename}')
                        filename = filename_gt_dict[filename]
                        print(f'수정후 filename : {filename}')
                        #                         # gt.txt 파일 읽어오기
                        #                         with open(gt_file_path, 'r', encoding='utf-8') as gt_file:
                        #                             gt_lines = gt_file.readlines()

                        #                         # 라인별로 반복하면서 처리
                        #                         for line in gt_lines:
                        #                             # 탭으로 스플릿
                        #                             values = line.strip().split('\t')

                        #                             if len(values) >= 2:
                        #                                 filename, new_value = values[0], values[1]

                        #                                 # filename과 같은 파일이 존재하면 덮어쓰기
                        #                                 target_file_path = os.path.join(base_path, filename)
                        #                                 if os.path.exists(target_file_path):
                        #                                     with open(target_file_path, 'w', encoding='utf-8') as target_file:
                        #                                         target_file.write(new_value)

                        #                         print("작업 완료.")

                        # filename과 같은 태국어 열의 인덱스를 찾습니다.
                        idx = df.index[df['태국어'] == filename].tolist()
                        print(f'같은 열 없음 idx 리스트: {idx}')

                        if not idx:
                            print(f'같은 열 없음 filename : {filename}')
                        else:
                            print(f'========같은 열 있음 filename : {filename}')
                            print(f'========같은 열 있음 idx : {idx}')
                            print(f'========같은 열 있음 recognized_text : {recognized_text}')

                            # 추출된 텍스트를 '태국어_ocr_text' 열에 넣습니다.
                            df.at[idx[0], ocr_text_열명] = recognized_text
                            # 업데이트 조건과 값
                            condition = (df['태국어'] == filename)

                            # 조건을 만족하는 모든 행 업데이트
                            df.loc[condition, ocr_text_열명] = recognized_text

                            print(f'========같은 열 있음 recognized_text : {recognized_text}')

                            # OCR 결과를 업데이트

                            if recognized_text == df.at[idx[0], '태국어']:
                                df.at[idx[0], result_열명] = 'suc'
                                # 조건을 만족하는 모든 행 업데이트
                                df.loc[condition, result_열명] = 'suc'

                                태국어_suc_cnt += 1
                                print(f'#################같은 열 있음 성공   태국어_suc_cnt : {태국어_suc_cnt}')

                            else:
                                df.at[idx[0], result_열명] = 'fail'
                                # 조건을 만족하는 모든 행 업데이트
                                df.loc[condition, result_열명] = 'fail'

                                태국어_fail_cnt += 1
                                print(f'#################failfailfail 같은 열 있ㄴ,ㄴ  태국어_fail_cnt : {태국어_fail_cnt}')

                        continue  # 일치하는 항목이 없는 경우 다음 이미지로 이동

                last_row_index = df.index[-1]  # 가장 마지막 행의 인덱스
                next_row_index = last_row_index + 1  # 다음 행의 인덱스
                print(f"last_row_index: {last_row_index}")
                print(f"next_row_index: {next_row_index}")
                태국어_tot_cnt = 태국어_suc_cnt + 태국어_fail_cnt
                태국어_성공률 = round(태국어_suc_cnt / 태국어_tot_cnt, 2)
                # 소수 셋째 자리에서 반올림하여 나타냅니다.
                # 태국어_tot_cnt = round(태국어_tot_cnt, 2)
                # 다음 행에 '태국어_전처리1_result' 열에 값을 설정
                # df.at[next_row_index, result_열명] = 태국어_suc_cnt
                df.at[next_row_index, result_열명] = f'{태국어_suc_cnt} / {태국어_tot_cnt} ( {태국어_성공률} )'

                print(f"태국어_suc_cnt:@@@@@@@@@@@@@@@@@@@@@@@@@ {태국어_suc_cnt}")
                # df.to_excel('D:/data/ocr/1018/태국어_전처리_with_result_updated.xlsx', index=False)
                df.to_excel('D:/data/ocr/1215/태국어_전처리_with_result_updated.xlsx', index=False)

        print(f"일치하는 항목 수: {태국어_suc_cnt}")
