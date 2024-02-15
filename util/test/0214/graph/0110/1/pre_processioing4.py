import pandas as pd

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file3)

print(fr'df : {result_df}')

# 문자열로 변환
#result_df['Success Rate'] = result_df['Success Rate'].astype(str)

import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 생성
data = {
    'Preprocessing Method': ['태국어_가늘게_전처리_미디안필터_kernel_1_Original', '태국어_검정_전처리_미디안필터_kernel_1_Original',
                             '태국어_굵게_전처리_미디안필터_kernel_1_Original', '태국어_보통_전처리_미디안필터_kernel_1_Original',
                             '태국어_아주 가늘게_전처리_미디안필터_kernel_1_Original', '태국어_아주 굵게_전처리_미디안필터_kernel_1_Original',
                             '태국어_아주 검정_전처리_미디안필터_kernel_1_Original', '태국어_아주 보통_전처리_미디안필터_kernel_1_Original',
                             '태국어_가늘게_전처리_미디안필터_kernel_3_Original', '태국어_검정_전처리_미디안필터_kernel_3_Original'],
    'Success Rate': [0.31, 0.35, 0.36, 0.34, 0.40, 0.38, 0.34, 0.39, 0.33, 0.34]
}

df = pd.DataFrame(data)

# 막대 그래프로 시각화
plt.figure(figsize=(12, 6))
plt.bar(df['Preprocessing Method'], df['Success Rate'], color='skyblue')
plt.title('OCR Success Rate by Preprocessing Method', fontsize=15)
plt.xlabel('Preprocessing Method', fontsize=12)
plt.ylabel('Success Rate', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




# 전처리 방법과 성공률 추출
#preprocess_methods = result_df['Preprocessing Method']
#success_rates = result_df['Success Rate'].apply(lambda x: float(x.split('/')[0]) / float(x.split('/')[1].split('(')[0].strip()))

# 막대 그래프로 시각화
# plt.figure(figsize=(10, 6))
# #plt.bar(preprocess_methods, success_rates, color='skyblue')
# plt.title('OCR Success Rate by Preprocessing Method')
# plt.xlabel('Preprocessing Method')
# plt.ylabel('Success Rate')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()
