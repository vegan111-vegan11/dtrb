data_file_path = "데이터_파일_경로.txt"  # 데이터 파일의 경로를 지정해주세요.

with open(data_file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()  # 줄 끝의 공백 및 개행 문자 제거
        image_path, label = line.split('\t')
        print("Image Path:", image_path)
        print("Label:", label)
