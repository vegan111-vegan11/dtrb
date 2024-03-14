import os

lan = 'ko'

# 파일 경로
input_file = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\pt\pt2.txt'
output_file = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\pt\pt3.txt'

input_file = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}2.txt'
output_file = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}3.txt'
output_file = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}_auto.txt'

# 파일 읽기
with open(input_file, 'r', encoding='utf-8') as f:
    #linpt = f.readlinpt()
    linpt = f.readline()
    lines = f.readlines()

    print(fr'lines : {lines}')

# 빈 문자열 제거 및 쓰기
with open(output_file, 'w', encoding='utf-8') as f:

    #for line in linpt:
    for line in lines:

        line = line.strip()
        if line:  # 빈 문자열이 아닌 경우에만 쓰기
            print(fr'line : {line}')
            f.write(line + '\n')

print("작업이 완료되었습니다.")
