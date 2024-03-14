import os

# 경로 설정
folder_path = r"D:\deep-text-recognition-benchmark\data\en\rect_invert\train\img"

# 해당 경로 내의 디렉토리별 jpg 파일 개수 저장할 딕셔너리
directory_counts = {}

# 해당 경로 내의 모든 파일 및 디렉토리에 대해 반복
for root, dirs, files in os.walk(folder_path):
    # 디렉토리 내의 jpg 파일 개수 카운트
    jpg_count = 0
    for file in files:
        # 파일 확장자가 .jpg인 경우
        if file.endswith(".jpg"):
            jpg_count += 1

    # 현재 디렉토리 경로를 키로 사용하여 개수를 딕셔너리에 저장
    directory_counts[root] = jpg_count

# 결과 출력
for directory, count in directory_counts.items():
    print(f"{directory}: {count}개의 jpg 파일")
