import os

# 폴더 경로
folder_path = r'C:\Users\TAMSystech\Downloads\이은영 소장님'

# 결과를 저장할 파일 경로
output_file_path = os.path.join(folder_path, 'all.txt')

# 결과 파일 열기
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # 폴더 내의 모든 파일 및 폴더에 대해 반복
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # 텍스트 파일인 경우에만 처리
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    content = input_file.read()
                    # 파일 내용을 결과 파일에 쓰기
                    output_file.write(content)
                    output_file.write('\n')  # 파일 간 구분을 위해 줄 바꿈 추가
