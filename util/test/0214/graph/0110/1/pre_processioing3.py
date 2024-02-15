import pandas as pd

# 엑셀 파일 경로
excel_file2 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만2.xlsx'

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file2)

# 결과 열 추출
result_columns = [col for col in result_df.columns if col.endswith('_result')]

# 전처리 방법과 성공률 추출
preprocess_methods = [col.split('_result')[0] for col in result_columns]
success_rates = []
for col in result_columns:
    result = result_df[col].iloc[0]
    if isinstance(result, str):  # 결과가 문자열인 경우에만 처리
        success_rate_str = result.split('(')[-1].split(')')[0]
        success_rates.append(success_rate_str)
    else:
        success_rates.append(None)  # 문자열이 아닌 경우 None으로 처리

# DataFrame 생성
result_data = {'Preprocessing Method': preprocess_methods, 'Success Rate': success_rates}
result_df = pd.DataFrame(result_data)

# 새 Excel 파일에 저장
result_df.to_excel(excel_file3, index=False)

import matplotlib.pyplot as plt

# 새로운 엑셀 파일에서 데이터 읽어오기
result_df = pd.read_excel(excel_file3)

# 전처리 방법과 성공률 추출
preprocess_methods = result_df['Preprocessing Method']
success_rates = result_df['Success Rate'].apply(lambda x: float(x.split('/')[0]) / float(x.split('/')[1].split('(')[0].strip()))

# 막대 그래프로 시각화
plt.figure(figsize=(10, 6))
plt.bar(preprocess_methods, success_rates, color='skyblue')
plt.title('OCR Success Rate by Preprocessing Method')
plt.xlabel('Preprocessing Method')
plt.ylabel('Success Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
