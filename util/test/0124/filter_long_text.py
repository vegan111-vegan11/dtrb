file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 28번째 라인의 문자열 길이 출력
        line_28 = lines[27].strip()  # 28번째 라인을 읽어오고 공백 제거
        length_of_line_28 = len(line_28)
        print(f"28번째 라인의 문자열 길이: {length_of_line_28}")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except IndexError:
    print("파일이 28개 라인 이하입니다.")
except Exception as e:
    print(f"오류 발생: {e}")

file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거.txt'

cnt = 0

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # 파일의 각 라인을 읽어서 길이가 13보다 큰 라인을 저장
        lines_over_13 = [line.strip() for line in file.readlines() if len(line.strip()) > 34]
        lines_over_15 = [line.strip() for line in file.readlines() if len(line.strip()) > 15]
        lines_over_14 = [line.strip() for line in file.readlines() if len(line.strip()) > 14]
        lines_over_14 = [line for line in file.readlines() if len(line) > 13]

        # 결과 출력
        print("문자열 길이가 13보다 큰 라인:")
        #for line in lines_over_13:
        #for line in lines_over_15:
        for line in lines_over_13:

            print(line)
            cnt = cnt + 1

        print(f"cnt: {cnt}")

        # 리스트로 반환
        # lines_over_13 변수에 저장된 라인들을 필요에 따라 활용할 수 있습니다.
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {e}")
