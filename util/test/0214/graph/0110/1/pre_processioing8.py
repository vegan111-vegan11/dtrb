import pandas as pd
import matplotlib.pyplot as plt

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file3)

# 전처리 방법에서 서식 부분 추출하여 새로운 열 추가
result_df['Font'] = result_df['Preprocessing Method'].apply(lambda x: x.split('_전처리')[0])

# 서식별로 그룹화
font_groups = result_df.groupby('Font')

# 서식별로 서브플롯에 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 시스템에 설치된 한글 폰트 목록
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# 사용 가능한 한글 폰트 목록
available_fonts = [font for font in font_list if 'Malgun Gothic' in font.lower() or 'Malgun Gothic' in font.lower()]

# Matplotlib에서 사용할 한글 폰트 선택
if available_fonts:
    print('젠장할')
    plt.rcParams['font.family'] = 'Malgun Gothic'  # 예시로 나눔고딕을 선택
else:
    print("한글 폰트를 찾을 수 없습니다. 폰트 경로를 확인하거나 시스템에 한글 폰트를 설치해주세요.")

for (font, group), ax in zip(font_groups, axes.flatten()):
    group.plot(kind='bar', x='Preprocessing Method', y='Success Rate', ax=ax, color='skyblue')
    ax.set_title(f'{font} 서식', fontsize=12)
    ax.set_xlabel('전처리 방법', fontsize=10)
    ax.set_ylabel('성공률', fontsize=10)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_ylim(0, 1)  # y 축 범위 설정

# 서브플롯 간 간격 조절
plt.tight_layout()
plt.show()
