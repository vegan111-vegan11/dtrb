# import openpyxl
#
# input_excel_path = r"D:\text_file\라인명\test\NotoSansThaiLooped-Thin\000000028.xlsx"
#
# try:
#     input_wb = openpyxl.load_workbook(input_excel_path)
#     input_sheet = input_wb.active
#
#     for row in input_sheet.iter_rows(min_row=1, max_row=10, min_col=1, max_col=10):  # 최대 10행까지 출력
#         row_values = [cell.value for cell in row]
#         print(row_values)
#
#     input_wb.close()
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
#
# import pandas as pd
#
# input_excel_path = "D:\\text_file\\라인명\\test\\NotoSansThaiLooped-Thin\\000000028.xlsx"
# df = pd.read_excel(input_excel_path)
# print(df)

import os

# 대상 경로
target_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf13\train\img'
dest_path = fr'D:\img\라인명\vi'
dest_path = fr'D:\text_file\라인명\vi'
dest_path = fr'C:\Users\TAMSystech\yjh\text_file\라인명\vi'
dest_path = fr'D:\text_file\라인명\vi'
dest_path = fr'D:\text_file\라인명\test'

# 대상 경로에서 디렉토리를 찾아서 출력
for root, dirs, files in os.walk(target_path):
    for directory in dirs:
        full_path = os.path.join(root, directory)
        print(directory)
        # print(full_path)
        full_path = os.path.join(dest_path, directory)
        print(full_path)
        # 디렉토리가 없으면 생성
        os.makedirs(full_path, exist_ok=True)
        #D:\img\라인명\vi