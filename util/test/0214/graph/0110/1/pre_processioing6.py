import pandas as pd
import matplotlib.pyplot as plt

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file3)

# 문자열로 변환
result_df['Success Rate'] = result_df['Success Rate'].astype(str)

# 막대 그래프로 시각화
plt.figure(figsize=(12, 6))
plt.bar(result_df['Preprocessing Method'], result_df['Success Rate'], color='skyblue')
plt.title('전처리 방법별 OCR 성공률', fontsize=15)
plt.xlabel('전처리 방법', fontsize=12)
plt.ylabel('성공률', fontsize=12)
plt.xticks(rotation=45, ha='right')

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False

plt.tight_layout()
plt.show()
