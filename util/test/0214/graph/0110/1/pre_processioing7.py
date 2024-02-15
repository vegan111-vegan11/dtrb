import pandas as pd
import matplotlib.pyplot as plt

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file3)

# 전처리 방법에서 글꼴 추출
result_df['Font'] = result_df['Preprocessing Method'].apply(lambda x: x.split('_')[2])

# 글꼴 그룹별로 데이터 분할
font_groups = result_df.groupby('Font')

# 그래프 구역 설정
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# 각 글꼴 그룹에 대한 시각화
for (font, group), ax in zip(font_groups, axes.flatten()):
    group.plot(kind='bar', x='Preprocessing Method', y='Success Rate', ax=ax, color='skyblue')
    ax.set_title(f'{font} 글꼴', fontsize=12)
    ax.set_xlabel('전처리 방법', fontsize=10)
    ax.set_ylabel('성공률', fontsize=10)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_ylim(0, 1)  # y 축 범위 설정

# 서브플롯 간 간격 조절
plt.tight_layout()
plt.show()
