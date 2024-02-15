import os

lan = "베트남어"
lan = "vi"
lan = "la"
lan = "vi_all"
# 입력 파일 경로
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\vi\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}\{lan}.txt'

# 출력 파일 경로
output_file_path = os.path.join(os.path.dirname(input_file_path), fr'{lan}_gt.txt')
print(f'output_file_path : {output_file_path}')


# 라인 번호 형식 지정 함수
def format_line_number(line_number):
    return f"{line_number:09d}"

# 파일 읽기 및 처리
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# 결과를 gt.txt로 저장
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i, line in enumerate(lines, start=0):
        # 라인 번호 형식 지정
        formatted_line_number = format_line_number(i)

        # .jpg 추가 및 탭으로 구분
        formatted_line = f"image-{formatted_line_number}.jpg\t{line.strip()}\n"

        # 결과 파일에 쓰기
        output_file.write(formatted_line)

print(f"작업 완료. 결과 파일 경로: {output_file_path}")
