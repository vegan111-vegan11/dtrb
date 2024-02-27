import os

# 파일 경로
input_file = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\pt\pt2.txt'
output_file = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\pt\pt3.txt'

# 파일 읽기
with open(input_file, 'r', encoding='utf-8') as f:
    linpt = f.readlinpt()

# 빈 문자열 제거 및 쓰기
with open(output_file, 'w', encoding='utf-8') as f:
    for line in linpt:
        line = line.strip()
        if line:  # 빈 문자열이 아닌 경우에만 쓰기
            f.write(line + '\n')

print("작업이 완료되었습니다.")
