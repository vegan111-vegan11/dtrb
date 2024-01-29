import openpyxl
import pyautogui
import os
import time

# 엑셀 파일 경로
excel_file_path = r'D:\data\다국어문구_글씨 크게.xlsx'

# 스크린샷 저장 폴더
output_folder = r'C:\Users\TAMSystech\yjh\img\라인명2\베트남어'
os.makedirs(output_folder, exist_ok=True)

# 스크롤 간격 및 대기 시간 설정
scroll_distance = 3  # 스크롤 간격 (열 단위로 조절 가능)
scroll_wait_time = 1  # 대기 시간 (초)

# 엑셀 파일 열기
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# 특정 행의 데이터 출력
row_number = 1
row_data = [cell.value for cell in sheet[row_number]]

print(f"특정 행 데이터: {row_data}")

# 대기 시간을 고려하여 스크롤 및 스크린샷 찍기
for _ in range(2):  # 예시로 5번 스크롤
    # 스크롤
    pyautogui.scroll(scroll_distance)

    # 대기 시간
    time.sleep(scroll_wait_time)

    # 스크린샷 찍기
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.join(output_folder, f'screenshot_{row_number}.jpg')
    screenshot.save(screenshot_path)

# 엑셀 파일 닫기
wb.close()
