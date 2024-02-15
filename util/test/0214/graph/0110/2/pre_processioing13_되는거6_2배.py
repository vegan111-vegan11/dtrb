import pandas as pd
import matplotlib.pyplot as plt

# 열 이름과 해당 열의 값
columns_and_values = {
    'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.24,
    'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.22
}

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

# 각 막대 위에 성공률 값 표시
for bar, rate in zip(bars, result_df['Success Rate']):
    # plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, str(rate),
    #          ha='center', va='bottom', fontsize=10, color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.002, str(rate),
             ha='center', va='bottom', fontsize=10, color='black')

# x 축과 y 축 라벨 설정
plt.xlabel('전처리 방법', fontsize=12, color='black')
plt.ylabel('성공률', fontsize=12, color='black')

# 그래프 제목 설정
plt.title('white_background_1800_760 * 2 전처리 방법별 성공률', fontsize=14, color='black')

# x 축 라벨을 사선으로 기울여 표시
plt.xticks(rotation=45, fontsize=10, color='black')
plt.yticks(fontsize=10, color='black')
plt.xticks(rotation=10)

# 그래프 출력
plt.tight_layout()
plt.show()
