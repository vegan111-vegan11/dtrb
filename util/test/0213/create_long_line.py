import os

# 파일 경로 및 이름 설정
directory = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common'
output_file = fr'{directory}\베트남어_all_빈문자열 제거_긴문장.txt'


with open(output_file, 'w', encoding='utf-8') as outfile:
    for i in range(523):
        if i <= 522:  # "image-000000522"까지만 포함
            outfile.write(f'image-{i:09d}\n')
