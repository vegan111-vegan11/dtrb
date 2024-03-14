# 라인명으로 이미지 저장
# 되는거
# 처음 이미지 저장
import os
import pyautogui
import time
import pygetwindow as gw
import subprocess
lan = '태국어'
lan = '베트남어'
lan = 'vi'
lan = 'la2'
lan = 'la'
lan = 'es'
lan = 'pt'
lan = 'ko'
lan = 'en'
# lan = '태국어'
# font = 'NotoSansThaiLooped-Black'
# font = 'NotoSansThaiLooped-Bold'
# font = 'NotoSansThaiLooped-ExtraBold'
# font = 'NotoSansThaiLooped-ExtraLight'
# font = 'NotoSansThaiLooped-Light'
# font = 'NotoSansThaiLooped-Medium'
# font = 'NotoSansThaiLooped-Regular'
# font = 'NotoSansThaiLooped-SemiBold'
font = 'NotoSansThaiLooped-Thin'

font = 'Black'
font = 'Bold'
# font = 'ExtraBold'
# font = 'ExtraLight'
# font = 'Light'
# #font = 'Medium'
# font = 'Regular'
# font = 'SemiBold'


#font = 'Regular'


# 글꼴 스타일 리스트 =
# [ 가늘게, 아주 가늘게, 보통, 중간, 약간 굵게, 굵게, 아주 굵게, 검정, 가는 기울임꼴, 아주 가는 기울임꼴, 기울임꼴, 중간 기울임꼴, 약간 굵은 기울임꼴, 굵은 기울임꼴, 아주 굵은 기울임꼴, 검은 기울임꼴]
# 글꼴 스타일 리스트 = [ 가늘게, 아주 가늘게, 보통, 중간, 약간 굵게, 굵게, 아주 굵게, 검정, 가는 기울임꼴, 아주 가는 기울임꼴, 기울임꼴, 중간 기울임꼴, 약간 굵은 기울임꼴, 굵은 기울임꼴, 아주 굵은 기울임꼴, 검은 기울임꼴]
# font_list = [ 가늘게, 아주 가늘게, 보통, 중간, 약간 굵게, 굵게, 아주 굵게, 검정, 가는 기울임꼴, 아주 가는 기울임꼴, 기울임꼴, 중간 기울임꼴, 약간 굵은 기울임꼴, 굵은 기울임꼴, 아주 굵은 기울임꼴, 검은 기울임꼴]
# for font in font_list:
#     print(f'font = \'{font}\'')
font_dict = {}
font_dict = {'검정': 'Black', '굵게': 'Bold', '아주 굵게': 'ExtraBold',
             '아주 가늘게': 'ExtraLight', '가늘게': 'Light', '중간': 'Medium',
             '보통': 'Regular', '약간 굵게': 'SemiBold', '가늘게': 'Thin'
             }

# font = '가늘게'
# font = '아주 가늘게'
# font = '보통'
# font = '중간'
# font = '약간 굵게'
# font = 'NotoSansThaiLooped-Black'
#font = '굵게'
#font = '아주 굵게'
#font = '검정'
# font = '가는 기울임꼴'
# font = '아주 가는 기울임꼴'
# font = '기울임꼴'
# font = '중간 기울임꼴'
# font = '약간 굵은 기울임꼴'
# font = '굵은 기울임꼴'
# font = '아주 굵은 기울임꼴'
# font = '검은 기울임꼴'

# 모든 열려있는 창 가져오기
windows = gw.getAllTitles()


# 폴더 경로
# base_directory = r'C:\Users\TAMSystech\yjh\text_file\라인명\ttf'
# base_directory = r'C:\Users\TAMSystech\yjh\text_file\라인명2'

# 디렉토리를 반복하면서 디렉토리명 출력
# for directory_name in os.listdir(base_directory):
#     directory_path = os.path.join(base_directory, directory_name)


# print(f'directory_path : {directory_path}')
# #if(directory_name == 'LGBD'):
# # 디렉토리인 경우에만 출력
# if os.path.isdir(directory_path):

# 모든 창을 최소화
for window in windows:
    if window != "Program Manager":  # Windows의 Program Manager 창은 최소화하지 않도록 제외
        app = gw.getWindowsWithTitle(window)
        if app:
            app[0].minimize()
print("모든 열려있는 창을 최소화했습니다.")
# 폴더 경로
# folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\ttf\{directory_name}\{lan}'
# output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명2\ttf\{directory_name}\{lan}'
# folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\{lan}'
folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\테스트\{lan}'
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}'
# 실전용
folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{font}'
folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}2\{font}'
folder_path = fr'D:\text_file\라인명\{lan}\{font}'
folder_path = fr'D:\text_file\라인명\{lan}'
#folder_path = fr'D:\text_file\라인명\{lan}\{font}'
folder_path = fr'D:\text_file\라인명\{lan}'
#folder_path = fr'D:\text_file\라인명\{lan}\test'
#folder_path = fr'D:\text_file\라인명\{lan}'
# 테스트용
#folder_path = fr'D:\text_file\라인명\test'
###########################################################################


#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\테스트\{lan}'
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{font}'
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{font}'

output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\{font}'
# output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\테스트'
output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\{font}'
output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}2\{font}'
output_folder = fr'D:\img\라인명\{lan}\{font}'
#output_folder = fr'D:\img\라인명\{lan}\test'
# 테스트용
#output_folder = fr'D:\img\라인명\test'
###########################################################################

#output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\테스트'
# output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명2\테스트\{lan}\{font}'
# folder_path = r'C:\Users\TAMSystech\yjh\text_file\테스트\테스트'
# output_folder = fr'C:\Users\TAMSystech\yjh\img\ttf2\{directory_name}\{lan}'

# 디렉토리가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
pyautogui.FAILSAFE = False
# 폴더 내의 모든 txt 파일 가져오기
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# 폴더 내의 모든 txt 파일 가져오기
# txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt') and any(str(num) in f for num in [202, 203, 204, 211, 220])]
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!txt_files : {txt_files}')
line_number = 0

import re

# 파일 경로 지정
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장2.txt'
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장4.txt'
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장.txt'
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거_긴문장2.txt'
file_path = r'C:\Users\TAMSystech\yjh\text_file\전체 언어 텍스트 파일\ttf3\common\베트남어_빈문자열 제거.txt'
file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}.txt'
#file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_긴문장.txt'
# file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_긴문장2.txt'
# file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_test.txt'

file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_긴문장.txt'
# file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_긴문장2.txt'
# file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_긴문장3.txt'

#file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_del_blank_line.txt'
#file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\common\{lan}_test.txt'

###################################
###################################

long_set_num = set()

# 파일 내용 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(fr'content : {content}')

# 정규식 패턴 설정
pattern = re.compile(r'image-(\d+)')
#pattern = re.compile(r'image-(\d+).jpg')

# 각 줄에서 패턴에 일치하는 부분 찾기
matches = pattern.findall(content)

# # 결과 출력
# for match in matches:
#     print(match)
#     print(fr'match : {match}')
#     long_set_num.add(match)
#
# #print(long_set_num)
# print(fr'long_set_num : {long_set_num}')

lines = []  # 빈 리스트 생성

# 파일 열기
with open(file_path, 'r', encoding='utf-8') as file:
    # 파일의 각 줄을 읽어서 리스트에 추가
    print(fr'file : {file}')
    for line in file:
        print(fr'line : {line}')

        # 각 줄에서 패턴에 일치하는 부분 찾기
        matches = pattern.findall(line.strip())

        # 각 매치된 부분에 .txt를 추가하여 리스트에 추가
        for match in matches:
            lines.append(match + ".txt")
            print(fr'lines : {lines}')

# 결과 출력
#print(lines)
print(fr'lines : {lines}')
###################################
###################################

# 이미지 잘 못 생성된 경우 다시 생성
#txt_files = lines
###################################
###################################

print(fr'txt_files 변경후 : {txt_files}')

max_line_length = 20
max_line_length = len('Hẹn giờ đang tắt')
print(fr'max_line_length : {max_line_length}')
max_line_length = 30
max_line_length = 25
max_line_length = 30
max_line_length = 40
max_line_length = 200

# 텍스트 파일을 열어서 화면 캡처 및 이미지 저장
for txt_file in txt_files:

    # 파일 열기
    txt_file_path = fr'{folder_path}/{txt_file}'
    print(fr'txt_file : {txt_file}')
    print(fr'txt_file_path : {txt_file_path}')

    with open(txt_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(fr'content : {content}')

    # 특정 길이 이상인 경우 엔터 추가하여 두 줄로 만들기
    modified_content = ""
    # for line in content.splitlines():
    #     if len(line) > max_line_length:
    #         while len(line) > max_line_length:
    #             modified_content += line[:max_line_length] + '\n'
    #             line = line[max_line_length:]
    #             line = "  " + line[max_line_length:]
    #
    #
    #
    #     else:
    #         modified_content += line + '\n'

    for line in content.splitlines():
        print(fr'line : {line}')

        if len(line) > max_line_length:
            while len(line) > max_line_length:
                modified_content += "  " + line[:max_line_length] + "  " + '\n'
                line = line[max_line_length:]

            # 남은 부분이 max_line_length 미만인 경우에도 줄바꿈 추가
            if len(line) > 0:
                modified_content += "  " + line + "  " + '\n'
                print(fr'############# if len(line) > 0 line : {line}')
                print(fr'#############if len(line) > 0 modified_content : {modified_content}')
        else:
            modified_content += line + '\n'
            print(fr'############# else 짧은 경우 modified_content : {modified_content}')

        # if len(line) > max_line_length:
        #     chunks = [line[i:i + max_line_length] for i in range(0, len(line), max_line_length)]
        #
        #     # 각 chunk에 앞뒤로 공백을 추가하여 modified_content에 추가
        #     # modified_content += "\n".join(["  " + chunk + "  " for chunk in chunks]) + "\n"
        #     modified_content += "".join(["  " + chunk + "  " for chunk in chunks]) + "\n"
        #     print(fr'modified_content : {modified_content}')
        #
        #     # 다음 라인 준비
        #     # line = "  " + line[max_line_length:]
        #     line = line[max_line_length:]
        #     print(fr'line : {line}')

            # while len(line) > max_line_length:
            #     #modified_content += line[:max_line_length] + '\n'
            #     #modified_content += "  " + line[:max_line_length].strip() + "  \n"
            #     #modified_content += "  " + line[:max_line_length].strip() + "  " + "\n"
            #     # modified_content += "  " + line[:max_line_length]+ "  ==\n"
            #     # line = line[max_line_length:]
            #
            #     # line을 max_line_length만큼 나눠서 리스트에 저장
            #     chunks = [line[i:i + max_line_length] for i in range(0, len(line), max_line_length)]
            #
            #     # 각 chunk에 앞뒤로 공백을 추가하여 modified_content에 추가
            #     #modified_content += "\n".join(["  " + chunk + "  " for chunk in chunks]) + "\n"
            #     modified_content += "".join(["  " + chunk + "  " for chunk in chunks]) + "\n"
            #     print(fr'modified_content : {modified_content}')
            #
            #     # 다음 라인 준비
            #     #line = "  " + line[max_line_length:]
            #     line = line[max_line_length:]
            #     print(fr'line : {line}')


            # 남은 부분이 max_line_length 미만인 경우에도 줄바꿈 추가
            # if len(line) > 0:
            #     modified_content += "  " + line + '\n'
            #     print(fr'############# if len(line) > 0 line : {line}')
            #     print(fr'#############if len(line) > 0 modified_content : {modified_content}')

        # else:
        #     modified_content += line + '\n'

    # 수정된 내용을 파일에 쓰기
    modified_file_path = file_path.replace('.txt', '_modified.txt')
    modified_file_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}2\{txt_file}'
    modified_file_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{txt_file}'
    modified_file_path = fr'D:\text_file\라인명\{lan}\{txt_file}'
    with open(modified_file_path, 'w', encoding='utf-8') as modified_file:
        modified_file.write(modified_content)
        #print(fr'modified_content : {modified_content}')

    # 파일명에서 .txt를 제외한 부분 추출
    txt_file_without_extension = txt_file.split('\\')[-1].replace('.txt', '')

    # 해당 부분이 long_set_num에 있는 경우에만 반복
    #if txt_file_without_extension in long_set_num:
    if True:


        txt_file_path = os.path.join(folder_path, txt_file)
        txt_file_path = modified_file_path

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!txt_file_path : {txt_file_path}')

        # 모든 열려있는 창 가져오기
        windows = gw.getAllTitles()
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1 : ')
        # 모든 창을 최소화
        #     for window in windows:
        #         #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!window : {window}')
        #         if window != "Program Manager":  # Windows의 Program Manager 창은 최소화하지 않도록 제외
        #             #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!3 : ')
        #             app = gw.getWindowsWithTitle(window)
        #             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!app : {app}')
        #             #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!4 : ')
        #             if app:
        #                 #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!5 : ')
        #                 app[0].minimize()
        #                 #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!6 : ')

        # txt 파일을 메모장으로 엽니다 (Windows 기준)
        # os.system(f'start notepad.exe {txt_file_path}')
        # 노트패드로 파일 열기
        # subprocess.run(['notepad.exe', txt_file_path])
        # 노트패드로 파일 열기
        # subprocess.run(['notepad.exe', txt_file_path])
        # subprocess.run(['notepad.exe', txt_file_path])
        # notepadpp_path = r'C:\Program Files\Notepad++\notepad++.exe'
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7 : ')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!8 : ')
        os.system(f'start notepad.exe {txt_file_path}')



        # with open(modified_file_path, 'w') as modified_file:
        #     modified_file.write(modified_content)



        # Notepad++로 파일 열기
        # subprocess.run([notepadpp_path, txt_file_path])
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!9 : ')
        # C:\Program Files\Notepad++\notepad++.exe
        time.sleep(0.1)
        time.sleep(0.1)
        #time.sleep(1)
        print(f'노트패드로 파일 열기txt_file_path : {txt_file_path}')

        # 메모장 창이 열릴 때까지 대기합니다 (시간을 필요에 따라 조정하세요)
        # #time.sleep(1)
        # 메모장 창 최대화 (Windows 창 최대화 단축키)
        pyautogui.hotkey('win', 'up')  # 창을 최대화합니다
        time.sleep(0.1)
        time.sleep(0.1)
        #time.sleep(1)
        # 글자 크기 조정 (키보드 조작을 통해 Ctrl + "-" 키를 누름)
        # pyautogui.hotkey('ctrl', '-')
        # time.sleep(0.5)  # 조절에 시간이 필요한 경우 대기시간 추가
        # 커서 숨기기
        # pyautogui.moveTo(-1, -1)  # 커서를 (1, 1)로 이동하여 숨깁니다
        # time.sleep(0.5)  # 조절에 시간이 필요한 경우 대기시간 추가
        # 화면 캡처를 캡처합니다
        # x, y, width, height = 10, 48, 1800, 120  # 캡처하려는 화면 영역의 좌표와 크기
        # x, y, width, height = 6, 48, 1800, 80  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 19, 242, 1800, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 19, 242, 100, 100  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 19, 242, 1000, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 1, 1, 1000, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 10, 1, 1000, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 30, 60, 1000, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 30, 60, 1800, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 30, 60, 1850, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 30, 60, 1870, 760  # 캡처하려는 화면 영역의 좌표와 크기
        x, y, width, height = 30, 60, 1875, 760  # 캡처하려는 화면 영역의 좌표와 크기
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        #time.sleep(1)
        # 이미지를 저장합니다
        # time.sleep(0.5)  # 조절에 시간이 필요한 경우 대기시간 추가

        line_number = int(txt_file[:-4])
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!line_number : {line_number}')

        output_file_path = os.path.join(output_folder, f'image-{line_number:09d}.jpg')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!output_file_path : {output_file_path}')
        # screenshot.save(output_file_path)
        # print(f'스크린샷 이미지를 저장했습니다: {output_file_path}')

        # 이미 파일이 존재하는지 체크
        if os.path.exists(output_file_path):
            # print(f'파일이 이미 존재합니다: {output_file_path}')
            os.remove(output_file_path)

            # print(f'기존 파일 삭제: {output_file_path}')

            screenshot.save(output_file_path)
            print(f'스크린샷 이미지를 저장했습니다: {output_file_path}')
            # time.sleep(0.5)  # 조절에 시간이 필요한 경우 대기시간 추가
            # print(f'{line_number} 개의 txt 파일의 스크린샷 이미지를 저장했습니다.')
            # 여기에 필요한 처리를 추가하세요 (덮어쓰기, 새로운 이름 사용 등)
        else:
            screenshot.save(output_file_path)
            print(f'스크린샷 이미지를 저장했습니다2: {output_file_path}')

        # for line in open(txt_file_path):
        # for line in open(txt_file_path, 'r', encoding='utf-8'):
        #     # line_number += 1
        #     # print(f'line_number : {line_number}')
        #     # print(f'txt_file : {txt_file}')
        #     # txt_file = txt_file[:-4]
        #     # txt_file = int(txt_file)
        #     # output_file_path = os.path.join(output_folder, f'image-{txt_file:09d}.jpg')
        #     line_number = int(txt_file[:-4])
        #     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!line_number : {line_number}')
        #
        #     output_file_path = os.path.join(output_folder, f'image-{line_number:09d}.jpg')
        #     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!output_file_path : {output_file_path}')
        #     # screenshot.save(output_file_path)
        #     # print(f'스크린샷 이미지를 저장했습니다: {output_file_path}')
        #
        #     # 이미 파일이 존재하는지 체크
        #     if os.path.exists(output_file_path):
        #         # print(f'파일이 이미 존재합니다: {output_file_path}')
        #         os.remove(output_file_path)
        #
        #         # print(f'기존 파일 삭제: {output_file_path}')
        #
        #         screenshot.save(output_file_path)
        #         print(f'스크린샷 이미지를 저장했습니다: {output_file_path}')
        #         # time.sleep(0.5)  # 조절에 시간이 필요한 경우 대기시간 추가
        #         # print(f'{line_number} 개의 txt 파일의 스크린샷 이미지를 저장했습니다.')
        #         # 여기에 필요한 처리를 추가하세요 (덮어쓰기, 새로운 이름 사용 등)
        #     else:
        #         screenshot.save(output_file_path)
        #         print(f'스크린샷 이미지를 저장했습니다2: {output_file_path}')

    # 메모장 창을 닫습니다
    os.system('taskkill /f /im notepad.exe')
    # line_number += 1
print(f'{len(txt_files)} 개의 txt 파일의 스크린샷 이미지를 저장했습니다.')