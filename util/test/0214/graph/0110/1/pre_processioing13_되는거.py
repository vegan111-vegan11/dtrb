import pandas as pd
import matplotlib.pyplot as plt

# 새로운 엑셀 파일 경로
excel_file4 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'
excel_file4 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.63_결과만4.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file4)

# 전처리 방법에서 서식 부분 추출하여 새로운 열 추가
result_df['Font'] = result_df['Preprocessing Method'].apply(lambda x: x.split('_전처리')[0])

# 서식별로 그룹화
font_groups = result_df.groupby('Font')

# 시스템에 설치된 한글 폰트 목록 확인
import matplotlib.font_manager as fm
font_path = fm.findSystemFonts(fontpaths=None, fontext='ttf')
for font in font_path:
    if 'malgun' in font.lower():
        plt.rcParams['font.family'] = 'Malgun Gothic'
        break

# 서식별로 서브플롯에 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

for (font, group), ax in zip(font_groups, axes.flatten()):
    group.plot(kind='bar', x='Preprocessing Method', y='Success Rate', ax=ax, color='skyblue')
    ax.set_title(f'{font} 서식', fontsize=12)
    ax.set_xlabel('전처리 방법', fontsize=10)
    ax.set_ylabel('성공률', fontsize=10)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_ylim(0, 1)  # y 축 범위 설정



# 서브플롯 간 간격 조절
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.subplots_adjust(hspace=2, wspace=2)

plt.tight_layout()
plt.show()
