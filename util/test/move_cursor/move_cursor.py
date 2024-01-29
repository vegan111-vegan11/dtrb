import os
import openpyxl
import pyautogui

def move_cursor_to_value(excel_file_path, target_value):
    # 엑셀 파일 열기
    os.startfile(excel_file_path)

    # 엑셀 파일 읽기
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active

    # 찾을 값 지정
    target_value = "Xin chào"

    # 값 찾기
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value == target_value:
                # 찾은 셀로 마우스 커서 이동
                print(fr'찾은 셀로 마우스 커서 이동 { cell.value}')
                #pyautogui.click(cell.column, cell.row)

                # 커서를 화면 왼쪽 위 모서리로 이동 (시각적인 표시 없음)
                # pyautogui.FAILSAFE = False  # 실패 안내 기능을 끄고
                # pyautogui.moveTo(0, 0, duration=0.25)  # 화면 왼쪽 위 모서리로 이동
                # pyautogui.FAILSAFE = True  # 실패 안내 기능을 다시 켜기


                return

if __name__ == "__main__":
    excel_file_path = fr"D:\data\다국어문구_글씨 크게.xlsx"  # 엑셀 파일 경로로 변경
    move_cursor_to_value(excel_file_path, "Xin chào")
