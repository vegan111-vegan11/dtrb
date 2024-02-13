# 제일 처음 텍스트로 저장
# 텍스트로 저장
import os
import time

lan = '태국어'
lan = '베트남어'
lan = 'la'
#lan = 'vi'
font = 'NotoSansThaiLooped-Black'
font = 'NotoSansThaiLooped-Bold'
# font = 'NotoSansThaiLooped-ExtraBold'
# font = 'NotoSansThaiLooped-ExtraLight'
# font = 'NotoSansThaiLooped-Light'
# font = 'NotoSansThaiLooped-Medium'
# font = 'NotoSansThaiLooped-Regular'
# font = 'NotoSansThaiLooped-SemiBold'
# font = 'NotoSansThaiLooped-Thin'

font = 'Black'
# font = 'Bold'
# font = 'ExtraBold'
font = 'ExtraLight'
# font = 'Light'
# font = 'Medium'
# font = 'Regular'
# font = 'SemiBold'

# 메모장 숮서
#font = 'Black'
# font = 'Bold'
# font = 'ExtraBold'
# font = 'ExtraLight'
# font = 'Light'
# font = 'Medium'
# font = 'Regular'
# font = 'SemiBold'

font_list = ['가늘게', '아주 가늘게', '보통', '중간', '약간 굵게', '굵게', '아주 굵게', '검정']
font_dict = {}
font_dict = {'검정': 'Black', '굵게': 'Bold', '아주 굵게': 'ExtraBold',
             '아주 가늘게': 'ExtraLight', '가늘게': 'Light', '중간': 'Medium',
             '보통': 'Regular', '약간 굵게': 'SemiBold', '가늘게': 'Thin'
             }

# font = '가늘게'
# font = '아주 가늘게'
# font = 'NotoSansThaiLooped-Black'
# font = '보통'
# font = '중간'
# font = '약간 굵게'
# font = '굵게'
# font = '아주 굵게'
# font = '검정'

# 특정 디렉토리 경로
base_directory = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3'
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\태국어_빈문자열 제거.txt'

# 디렉토리를 반복하면서 디렉토리명 출력
for root, dirs, files in os.walk(base_directory):
    for directory in dirs:
        directory_path = os.path.join(root, directory)
        # print(directory_path)

        # 입력 파일 경로
        # input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\{lan}.txt
        input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\{lan}_빈문자열 제거.txt'
        input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\{lan}.txt'

        # input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\{lan}3.txt'
        # input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{lan}.txt'
        #input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\태국어2.txt'
        #input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\{directory}\태국어2.txt'

        #         # 폴더 경로
        output_folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\{lan}'
        output_folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명4\{lan}2\{font}'
        output_folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}'
        output_folder_path = fr'D:\text_file\라인명\{lan}\{font}'
        # print(f'input_file_path : {input_file_path}')
        # input_file_path = fr'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf\{directory}\{lan}.txt'

        # 폴더 경로
        # output_folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\ttf\{directory}\{lan}'

        # 디렉토리가 없으면 생성
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
            os.makedirs(output_folder_path, exist_ok=True)
            print(f'output_folder_path : {output_folder_path}')

        # input_file_path = r'C:\Users\TAMSystech\yjh\LGBD\베트남어'
        # output_folder_path = r'C:\Users\TAMSystech\yjh\LGBD\text_file\베트남어'
        # 파일을 한 줄씩 읽어서 처리
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

            print(f'lines : {lines}')


        # 불법 파일명 문자를 밑줄 문자로 대체하는 함수
        def replace_illegal_characters(file_name):
            illegal_characters = '/\\:*?"<>|'
            for char in illegal_characters:
                file_name = file_name.replace(char, '_')
            return file_name


        # 각 줄을 파일로 저장
        # for line in lines:
        for line_number, line in enumerate(lines, 0):
            # 파일명으로 사용할 내용
            file_content = line.strip()
            # file_conent = '   ' + file_conent
            # file_conent = '   ' + file_conent
            #             file_content = '\n' + file_content
            #             file_content = '   ' + file_content

            #             #file_conent = file_conent + "\n"
            #             print(f'file_conent : {file_content}')
            #             file_content2 = '   ' + file_content
            #             print(f'file_content2 : {file_content2}')
            #             file_content = file_content2

            #             # 좌측에 3개의 공백 추가
            #             file_content_padded = file_content.ljust(len(file_content) + 3)
            #             file_content = file_content_padded
            #             file_content_padded2 = 'test'.ljust(len('test') + 3)
            #             # 결과 출력
            #             print(f'file_content_padded : {file_content_padded}')
            #             print(f'최종 file_content : {file_content}')

            file_path = str(line_number).zfill(9)  # line_number를 9자리 숫자로 변환
            # 2초 동안 일시 정지
            time.sleep(0.02)
            # 파일명에 사용할 수 없는 문자 대체
            # file_name = replace_illegal_characters(file_name)

            # 파일 경로 생성
            output_file_path = os.path.join(output_folder_path, f'{file_path}.txt')

            # 새로운 파일 작성
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                # 파일 내용 작성 (예: 파일명을 파일 내용으로 저장)
                # output_file.write('       ')
                # output_file.write(file_content_padded2)
                output_file.write("\n")
                # output_file.write(file_content_padded2)
                output_file.write('       ')
                # output_file.write(file_content)

                # output_file.write(file_content_padded)
                output_file.write(file_content)
                # 엔터를 입력하여 커서를 다음 줄로 옮김
                # output_file.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")
                # time.sleep(0.1)
                # 커서 숨기기
                # pyautogui.moveTo(1000, 1000)  # 커서를 (1, 1)로 이동하여 숨깁니다
                # time.sleep(0.02)  # 조절에 시간이 필요한 경우 대기시간 추가

        print(f'{len(lines)} 개의 파일이 생성되었습니다.')

