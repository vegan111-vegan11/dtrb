import os

# 경로 설정
path = r'D:\deep-text-recognition-benchmark\data\vi\rect_invert\train\img'
path = r'D:\deep-text-recognition-benchmark\data\la\rect_invert\train\img'
path = r'D:\deep-text-recognition-benchmark\data\vi_all\rect_invert\train\img'
path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf15\train\img\skew_angle(0.0)'
path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf\train\img'
path = r'C:/Users/TAMSystech/yjh/ipynb/deep-text-recognition-benchmark/data/train-easyocr/step3/training/thdata'

# JPG 파일 수를 저장할 변수 초기화
jpg_file_count = 0
pg_file_count_total = 0

# walk 함수를 사용하여 주어진 경로의 모든 하위 디렉토리를 재귀적으로 탐색
for root, dirs, files in os.walk(path):
    # 각 디렉토리에 포함된 JPG 파일의 수를 세어 jpg_file_count에 더함
    jpg_files = [file for file in files if file.endswith('.jpg')]
    print("dirs:", dirs)

    print("JPG 파일의 수:", jpg_file_count)

    jpg_file_count += len(jpg_files)
    pg_file_count_total += jpg_file_count

# 결과 출력
print("pg_file_count_total :", pg_file_count_total)
