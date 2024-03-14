import os

# 경로 설정
directory = r'D:\deep-text-recognition-benchmark\data\ko\rect_invert\train\img\Bold'

# 해당 경로에서 jpg 파일 수를 세는 변수 초기화
jpg_count = 0

# 디렉토리 내 모든 파일 및 디렉토리에 대해 반복
for filename in os.listdir(directory):
    # 파일 경로
    filepath = os.path.join(directory, filename)
    # 파일인지 확인
    if os.path.isfile(filepath):
        # 확장자가 jpg인지 확인
        if filename.lower().endswith('.jpg'):
            # jpg 파일인 경우 카운트 증가
            jpg_count += 1

# 결과 출력
print("경로에 {}개의 jpg 파일이 있습니다.".format(jpg_count))
