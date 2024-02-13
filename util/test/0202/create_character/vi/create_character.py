# 파일 경로 설정
file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\vi\vi.txt'

# 파일 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    vi_text = file.read()

# 중복 제거
unique_characters = list(set(vi_text))

# 출력
print("Unique Characters:")
print(''.join(unique_characters))
