import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 경로
excel_file_path = "vi_전처리_with_result_updated_test7_white_background_1800_760_2_kernel_3_원본_0.24_결과만.xlsx"
excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\vi\vi_전처리_with_result_updated_test7_white_background_1800_760_2_kernel_3_원본_0.24_결과만.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file_path)

print(result_df)

import pandas as pd

# 엑셀 파일에서 데이터 읽어오기
#df_excel = pd.read_excel('your_excel_file.xlsx', header=None)  # 열명이 없는 경우 header=None 설정

# 열명 지정
result_df.columns = ['Preprocessing Method', 'Success Rate']

print('=================')
# 출력
print(result_df)


# 전처리 방법 열에서 성공률 값을 가져와서 dictionary 형태로 변환
columns_and_values = dict(zip(result_df['Preprocessing Method'], result_df['Success Rate']))

# 데이터프레임 생성
result_df = pd.DataFrame(columns_and_values.items(), columns=['Preprocessing Method', 'Success Rate'])

# 한글 폰트 설정
import matplotlib.font_manager as fm
font_path = fm.findSystemFonts(fontpaths=None, fontext='ttf')
for font in font_path:
    if 'malgun' in font.lower():
        plt.rcParams['font.family'] = 'Malgun Gothic'
        break

# 막대 그래프 시각화
plt.figure(figsize=(10, 6))  # 그래프의 크기 조정
bars = plt.bar(result_df['Preprocessing Method'], result_df['Success Rate'])

# 성공률에 따라 색상 지정
colors = ['orange' if rate == max(result_df['Success Rate']) else 'skyblue' for rate in result_df['Success Rate']]
for bar, color in zip(bars, colors):
    bar.set_color(color)

# 막대 위에 성공률 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, height,
             ha='center', va='bottom', fontsize=10, color='black')

# x 축과 y 축 라벨 설정
plt.xlabel('전처리 방법', fontsize=12, color='black')
plt.ylabel('성공률', fontsize=12, color='black')

# 그래프 제목 설정
plt.title('white_background_1800_760 * 2 전처리 방법별 성공률', fontsize=14, color='black')

# x 축 라벨을 사선으로 기울여 표시
plt.xticks(rotation=45, fontsize=10, color='black')
plt.yticks(fontsize=10, color='black')
plt.xticks(rotation=20)

# 그래프 출력
plt.tight_layout()
plt.show()
