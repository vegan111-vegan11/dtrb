import os

# 주어진 경로 설정
input_directory = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common'
output_file_name = '베트남어_빈문자열 제거.txt'

# 입력 파일 경로 설정
input_file_path = os.path.join(input_directory, '베트남어_빈문자열 포함.txt')

# 출력 파일 경로 설정
output_file_path = os.path.join(input_directory, output_file_name)

# 입력 파일 열고 빈 문자열 제거 후 출력 파일에 저장
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        # 빈 문자열 제거 후 저장
        cleaned_line = line.strip()
        if cleaned_line:
            output_file.write(cleaned_line + '\n')

print(f"빈 문자열이 제거된 파일이 생성되었습니다: {output_file_path}")
