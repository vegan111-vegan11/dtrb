import time
import pyautogui
import os
# 라인명으로 이미지 저장
# 되는거
# 처음 이미지 저장
import os
import pyautogui
import time
import pygetwindow as gw
import subprocess

# lan = '태국어'
# font = 'NotoSansThaiLooped-Black'
# font = 'NotoSansThaiLooped-Bold'
# font = 'NotoSansThaiLooped-ExtraBold'
# font = 'NotoSansThaiLooped-ExtraLight'
# font = 'NotoSansThaiLooped-Light'
# font = 'NotoSansThaiLooped-Medium'
# font = 'NotoSansThaiLooped-Regular'
# font = 'NotoSansThaiLooped-SemiBold'
# font = 'NotoSansThaiLooped-Thin'
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

font = '가늘게'
font = '아주 가늘게'
font = '보통'
font = '중간'
font = '약간 굵게'
font = 'NotoSansThaiLooped-Black'
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

lan = '태국어'
lan = '베트남어'
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

import re

long_set_num = set()

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
# 테스트용
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\테스트'
#############################################################################

#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명2\테스트\{lan}'
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{font}'
#folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}\{font}'

output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\{font}'
# output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\테스트'
output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}\{font}'
output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명2\{lan}\{font}'
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


# 스크린샷 저장 폴더
screenshot_folder = 'screenshots'
os.makedirs(screenshot_folder, exist_ok=True)

# 한 번에 스크롤하는 거리
scroll_distance = 100

# 스크롤할 횟수
num_scrolls = 10

# 대기 시간 설정 (스크롤이 발생하면 기다려야 함)
scroll_wait_time = 1

# 활성 창을 엑셀로 전환 (창을 열어 두어야 함)
# 이 코드는 Windows 운영체제 기준입니다. macOS나 Linux에서는 다르게 처리해야 할 수 있습니다.
# 만약 다르다면 pyautogui의 활용 방법을 검색하여 찾아주세요.
pyautogui.click(50, 50)  # 좌표는 엑셀 창이 열려 있는 위치로 수정

# 스크롤 및 스크린샷 찍기
for i in range(num_scrolls):
    # 스크롤
    pyautogui.scroll(-scroll_distance)

    # 대기 시간
    time.sleep(scroll_wait_time)

    # 스크린샷 찍기
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.join(screenshot_folder, f'screenshot_{i + 1}.jpg')
    screenshot.save(screenshot_path)
