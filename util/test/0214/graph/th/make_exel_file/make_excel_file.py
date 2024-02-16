import pandas as pd
import re

# 엑셀 파일 경로
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\결과\2\태국어_전처리_with_result_updated_test7_black_background_margin_kernel_3_원본_0.03_결과만_pre_procession.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(excel_file_path)

# 열(column) 이름과 해당 값을 딕셔너리로 저장
columns_and_values = {}
for col in df.columns:
    #columns_and_values[col] = df[col][0]
    #columns_and_values[col] = df[col][0]
    print(fr'col : {col}')
    print('============')
    columns_and_values[col] = df[col][0]
    text  = df[col][0]
    # 괄호 안에 있는 값 추출
    value_in_parentheses = re.search(r'\((.*?)\)', text).group(1)

    #print(value_in_parentheses)
    print(fr'value_in_parentheses : {value_in_parentheses}')
    #columns_and_values[col] = df[col][0]
    columns_and_values[col] = value_in_parentheses

print(fr'columns_and_values : {columns_and_values}')

#print(columns_and_values)
