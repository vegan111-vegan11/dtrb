import pandas as pd

# 엑셀 파일 경로
excel_file = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file)

# 결과 열 추출
result_columns = [col for col in df.columns if col.endswith('_result')]

# 결과 열의 마지막 행 값 출력
for column in result_columns:
    last_valid_index = df[column].last_valid_index()  # 가장 마지막 유효한 인덱스 가져오기
    last_value = df.at[last_valid_index, column] if last_valid_index else None  # 유효한 인덱스가 있는 경우 해당 행의 값 가져오기
    print(f'{column}: {last_value}')
