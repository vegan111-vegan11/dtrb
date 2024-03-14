import os

lan = "베트남어"
lan = "vi"
lan = "la"
lan = "vi_all"
lan = "es"
# 입력 파일 경로
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\vi\{lan}_빈문자열 제거.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\{lan}\{lan}.txt'
input_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}.txt'

# 출력 파일 경로
output_file_path = os.path.join(os.path.dirname(input_file_path), fr'{lan}_gt.txt')
output_file_path = fr''

print(f'output_file_path : {output_file_path}')


# 라인 번호 형식 지정 함수
def format_line_number(line_number):
    return f"{line_number:09d}"

# 파일 읽기 및 처리
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

#import os

def print_directory_names(path):
    # 주어진 경로의 모든 파일과 디렉토리 목록을 얻습니다.
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        # 만약 현재 항목이 디렉토리인 경우에만 출력합니다.
        if os.path.isdir(full_path):
            #print(entry)
            print(fr'entry: {entry}')
            print(fr'full_path: {full_path}')

            output_file_path = full_path
            new_directory = output_file_path.replace("img", "gt")
            output_file_path = new_directory

            print(fr'output_file_path: {output_file_path}')

            os.makedirs(output_file_path, exist_ok=True)

            # 결과를 gt.txt로 저장
            with open(output_file_path, 'w+', encoding='utf-8') as output_file:
                for i, line in enumerate(lines, start=0):
                    # 라인 번호 형식 지정
                    formatted_line_number = format_line_number(i)

                    # .jpg 추가 및 탭으로 구분
                    formatted_line = f"image-{formatted_line_number}.jpg\t{line.strip()}\n"

                    # 결과 파일에 쓰기
                    output_file.write(formatted_line)

            print(f"작업 완료. 결과 파일 경로: {output_file_path}")


# 경로를 설정합니다.
path = r"D:\deep-text-recognition-benchmark\data\es\rect_invert\train\img"

# 디렉토리명을 출력합니다.
print("디렉토리 목록:")
print_directory_names(path)


# # 결과를 gt.txt로 저장
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for i, line in enumerate(lines, start=0):
#         # 라인 번호 형식 지정
#         formatted_line_number = format_line_number(i)
#
#         # .jpg 추가 및 탭으로 구분
#         formatted_line = f"image-{formatted_line_number}.jpg\t{line.strip()}\n"
#
#         # 결과 파일에 쓰기
#         output_file.write(formatted_line)
#
# print(f"작업 완료. 결과 파일 경로: {output_file_path}")
