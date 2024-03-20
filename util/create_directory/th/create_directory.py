import os
lan = 'en'
lan = 'th'
def print_and_create_directories(base_path, target_folder, new_folder):
    # 지정된 경로에 있는 각 디렉터리의 이름을 가져와 프린트
    for dir_name in os.listdir(os.path.join(base_path, target_folder)):
        print(dir_name)

        # 새로운 경로 생성
        new_path = os.path.join(base_path, target_folder.replace("img", "gt"), dir_name)

        # 새로운 경로로 이동하여 디렉터리가 존재하지 않으면 새로 생성
        if not os.path.exists(new_path):
            os.makedirs(new_path)

# 지정된 경로와 폴더명으로 함수 호출
# print_and_create_directories("D:\\deep-text-recognition-benchmark\\data\\ko\\rect_invert\\train", "img", "gt")
# print_and_create_directories(fr"D:\\deep-text-recognition-benchmark\\data\\{lan}\\rect_invert\\train", "img", "gt")
print_and_create_directories(fr"D:\deep-text-recognition-benchmark\data\{lan}\ttf13\train", "img", "gt")

