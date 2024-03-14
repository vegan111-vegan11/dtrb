lan = 'es'
lan = 'pt'
lan = 'ko'
lan = 'en'

file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}.txt'

# 중복된 character를 저장하기 위한 집합(set)을 생성합니다.
unique_characters = set()

# 파일을 읽어와서 중복된 character를 제거한 후 unique_characters에 추가합니다.
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # 라인의 양 끝 공백 및 개행 문자를 제거합니다.
        unique_characters.update(line)

# 중복된 character를 제거하고 정렬된 character들을 포함하는 리스트를 생성합니다.
#unique_characters_list = sorted(unique_characters)
unique_characters_list = unique_characters


# 중복된 character를 제거하고 정렬된 character들을 포함하는 문자열을 생성합니다.
#unique_characters_string = ''.join(sorted(unique_characters))
unique_characters_string = ''.join(unique_characters)

# 결과 문자열을 출력합니다.
print(unique_characters_string)
print(fr'unique_characters_string : {unique_characters_string}')
