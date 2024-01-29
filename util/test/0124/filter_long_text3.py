file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거.txt'

file_path_long_text = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장.txt'
file_path_long_text_list = []

file_path_long_text = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장.txt'
file_path_long_text = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장2.txt'
long_set = set()
long_set_num = set()

try:
    with open(file_path_long_text, 'r', encoding='utf-8') as file:
        file_path_long_text_list = file.readlines()

        # 각 라인을 set에 추가
        for line in file_path_long_text_list:
            long_set.add(line.strip())  # 각 라인을 추가하고 공백 제거

        # 결과 출력 및 개수 출력
        print("중복이 제거된 라인:")
        for line in long_set:
            print(line)

        print(f"중복이 제거된 라인의 개수: {len(long_set)}")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path_long_text}")
except Exception as e:
    print(f"오류 발생: {e}")



try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # 28번째 라인의 문자열 길이 출력
        line_28 = lines[27].strip()  # 28번째 라인을 읽어오고 공백 제거
        length_of_line_28 = len(line_28)
        print(f"28번째 라인의 문자열 길이: {length_of_line_28}")

        # 문자열 길이가 13보다 큰 라인과 라인 번호를 저장
        lines_over_13_with_numbers = [(i + 1, line.strip()) for i, line in enumerate(lines) if len(line.strip()) > 34]
        lines_over_13_with_numbers = [(i, line.strip()) for i, line in enumerate(lines) if len(line.strip()) > 34]

        # 결과 출력 및 개수 출력
        print("문자열 길이가 13보다 큰 라인:")

        print(f"!!!!!!!!!!len long_set 추가전 :  {len(long_set)}")


        for line_number, line in lines_over_13_with_numbers:

            #line_number = f'image-{line_number:09d}.jpg'
            line_number = f'image-{line_number:09d}'

            if line_number not in long_set:
                print(f"!!!!!!!!!!라인 {line_number}은(는) long_set에 없습니다: {line}")
                # 각 라인을 추가하고 공백 제거

                long_set.add(line_number)
                print(f"!!!!!!!!!!len long_set 추가후 :  {len(long_set)}")

        print(f"문자열 길이가 13보다 큰 라인의 개수: {len(lines_over_13_with_numbers)}")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {e}")


output_file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장2.txt'

try:
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line_number in long_set:
            new_line = f"{line_number}.jpg\n"
            output_file.write(new_line)

    print(f"새로운 파일이 생성되었습니다: {output_file_path}")
except Exception as e:
    print(f"오류 발생: {e}")


import re

# 파일 경로 지정
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장2.txt'

# 파일 내용 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 정규식 패턴 설정
pattern = re.compile(r'image-(\d+).jpg')

# 각 줄에서 패턴에 일치하는 부분 찾기
matches = pattern.findall(content)

# 결과 출력
for match in matches:
    print(match)
    long_set_num.add(match)

print(long_set_num)