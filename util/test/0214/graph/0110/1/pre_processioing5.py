import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 경로
excel_file = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만2.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file)

# 막대 그래프로 시각화
plt.figure(figsize=(12, 6))
for column in df.columns:
    plt.plot(df[column], marker='o', label=column)

plt.title('전처리 방법별 OCR 성공률', fontsize=15)
plt.xlabel('전처리 방법', fontsize=12)
plt.ylabel('성공률', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False

plt.show()
