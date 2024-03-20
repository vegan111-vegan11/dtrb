import os

# 주어진 디렉토리
directory = r'D:\deep-text-recognition-benchmark\data\th\ttf13\train\img'

# 모든 하위 폴더 탐색 및 출력
for root, dirs, files in os.walk(directory):
    for folder in dirs:
        # 폴더명 출력
        print(folder)

        # 새로운 폴더 경로 생성
        new_folder_path = os.path.join(root.replace("ttf13", "ttf13_th"), folder)

        # 새로운 폴더 생성
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"'{new_folder_path}' 폴더를 생성했습니다.")

print("작업 완료")
