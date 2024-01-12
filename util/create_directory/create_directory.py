import os

# 주어진 경로 설정
font_directory = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\fonts\thfont_all'
output_root_directory = r'C:\Users\TAMSystech\yjh\text_file\라인명4\베트남어'
output_root_directory = r'C:\Users\TAMSystech\yjh\img\라인명\베트남어'

# 주어진 경로에서 디렉토리를 생성하기 위한 루프
for filename in os.listdir(font_directory):
    # 파일 경로 생성
    file_path = os.path.join(font_directory, filename)

    # 파일명에서 확장자를 제외한 부분을 디렉토리명으로 사용
    dir_name = os.path.splitext(filename)[0]

    # 생성될 디렉토리의 경로 설정
    output_directory = os.path.join(output_root_directory, dir_name)

    # 디렉토리 생성
    os.makedirs(output_directory, exist_ok=True)
    print(f"디렉토리 생성 완료: {output_directory}")

    # # 파일이 디렉토리인지 확인
    # if os.path.isdir(file_path):
    #     # 파일명에서 확장자를 제외한 부분을 디렉토리명으로 사용
    #     dir_name = os.path.splitext(filename)[0]
    #
    #     # 생성될 디렉토리의 경로 설정
    #     output_directory = os.path.join(output_root_directory, dir_name)
    #
    #     # 디렉토리 생성
    #     os.makedirs(output_directory, exist_ok=True)
    #     print(f"디렉토리 생성 완료: {output_directory}")
