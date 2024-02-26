import os
import pandas as pd

# 폴더 경로
folder_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\결과\2'

# 폴더 내의 모든 엑셀 파일 가져오기
excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# 각 엑셀 파일을 읽어서 데이터 출력하고 병합
dfs = []
for file_name in excel_files:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_excel(file_path)
    print(f"File: {file_name}")
    print(df)
    print()
    dfs.append(df)

# 모든 데이터프레임을 병합
combined_df = pd.concat(dfs, ignore_index=True)

# 병합된 데이터프레임을 엑셀 파일로 저장
output_file_path = os.path.join(folder_path, 'total.xlsx')
combined_df.to_excel(output_file_path, index=False)

print(f"Combined data saved to: {output_file_path}")
