import os

input_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\th_1212_3.txt'
output_folder_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\gt\th'

# 결과를 새로운 파일에 저장
output_file_path = os.path.join(output_folder_path, 'gt.txt')

# gt 폴더가 없다면 생성
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 파일 읽기
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# 결과를 새로운 파일에 저장
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for idx, line in enumerate(lines):
        padded_index = f"{idx:09}"  # 9자리로 만들고 나머지는 0으로 채우기
        image_filename = f"image-{padded_index}.jpg\t{line.strip()}\n"  # 탭으로 구분
        output_file.write(image_filename)

print(f"각 라인에 패딩과 이미지 파일명이 추가된 내용이 {output_file_path}에 저장되었습니다.")
