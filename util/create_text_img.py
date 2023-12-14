# 라인명으로 이미지 저장
import os
import pyautogui
import time
import pygetwindow as gw

# 모든 열려있는 창 가져오기
windows = gw.getAllTitles()

lan = '태국어'
# 모든 창을 최소화
for window in windows:
    if window != "Program Manager":  # Windows의 Program Manager 창은 최소화하지 않도록 제외
        app = gw.getWindowsWithTitle(window)
        if app:
            app[0].minimize()

print("모든 열려있는 창을 최소화했습니다.")

# 폴더 경로
folder_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\{lan}'
output_folder = fr'C:\Users\TAMSystech\yjh\img\라인명\{lan}'
# folder_path = r'C:\Users\TAMSystech\yjh\text_file\테스트'
# output_folder = r'C:\Users\TAMSystech\yjh\img\테스트'

pyautogui.FAILSAFE = False

# 폴더 내의 모든 txt 파일 가져오기
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
line_number = 0
# 텍스트 파일을 열어서 화면 캡처 및 이미지 저장
for txt_file in txt_files:
    txt_file_path = os.path.join(folder_path, txt_file)

    # 모든 열려있는 창 가져오기
    windows = gw.getAllTitles()

    # 모든 창을 최소화
    for window in windows:
        if window != "Program Manager":  # Windows의 Program Manager 창은 최소화하지 않도록 제외
            app = gw.getWindowsWithTitle(window)
            if app:
                app[0].minimize()

    # txt 파일을 메모장으로 엽니다 (Windows 기준)
    os.system(f'start notepad.exe {txt_file_path}')

    # 메모장 창이 열릴 때까지 대기합니다 (시간을 필요에 따라 조정하세요)
    time.sleep(0.02)

    # 메모장 창 최대화 (Windows 창 최대화 단축키)
    pyautogui.hotkey('win', 'up')  # 창을 최대화합니다
    # time.sleep(0.02)
    # 글자 크기 조정 (키보드 조작을 통해 Ctrl + "-" 키를 누름)
    pyautogui.hotkey('ctrl', '-')
    time.sleep(0.1)  # 조절에 시간이 필요한 경우 대기시간 추가

    # 커서 숨기기
    pyautogui.moveTo(1, 1)  # 커서를 (1, 1)로 이동하여 숨깁니다

    # 화면 캡처를 캡처합니다
    # x, y, width, height = 10, 48, 1800, 120  # 캡처하려는 화면 영역의 좌표와 크기
    x, y, width, height = 6, 48, 1800, 80  # 캡처하려는 화면 영역의 좌표와 크기
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # 이미지를 저장합니다

    # for line in open(txt_file_path):
    for line in open(txt_file_path, 'r', encoding='utf-8'):
        # line_number += 1
        # print(f'line_number : {line_number}')
        # print(f'txt_file : {txt_file}')
        # txt_file = txt_file[:-4]

        # txt_file = int(txt_file)
        # output_file_path = os.path.join(output_folder, f'image-{txt_file:09d}.jpg')
        output_file_path = os.path.join(output_folder, f'image-{line_number:09d}.jpg')
        screenshot.save(output_file_path)
        print(f'스크린샷 이미지를 저장했습니다: {output_file_path}')

    # 메모장 창을 닫습니다
    os.system('taskkill /f /im notepad.exe')
    line_number += 1
print(f'{len(txt_files)} 개의 txt 파일의 스크린샷 이미지를 저장했습니다.')
