import pandas as pd
import matplotlib.pyplot as plt

##################
lan = 'th'

# 데이터 생성
# data = [
# ['black',	1410,	1110,	3,	'O',	'X',	0.01],
# ['white',	1410,	1110,	3,	'O',	'X',	0.03],
# ['white',	1410,	1110,	3,	'O',	'X',	0.05],
# ['white',	1410,	1110,	3,	'X',	'X',	0.03],
# ['white',	1410 * 2,	1110 * 2,	3,	'X',	'X',	0.34],
# ['white',	1410 * 2,	1110 * 2,	5,	'X',	'X',	0.21],
# ['white',	1410 * 2,	1110 * 2,	7,	'X',	'X',	0.1],
# ['white',	1410 * 2,	1110 * 2,	9,	'X',	'X',	0],
# ['white',	1410 * 2,	1110 * 2,	3,	'X',	'O',	0.90],
# ]

# data = [
# [0.01, 0.01]
#
# ]
#
# # 데이터프레임 생성
# #df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])
# df = pd.DataFrame(data, ccolumns=['Preprocessing Method', 'Success Rate'])
#
# # 엑셀 파일에 저장
# #excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\{lan}\facter_{lan}.xlsx'
# excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\{lan}\결과\2\태국어_전처리_with_result_updated_test7_black_background_kernel_3_원본_0.01_결과만.xlsx'
# df.to_excel(excel_file_path, index=False)
#
# # 엑셀 파일 불러오기
# loaded_df = pd.read_excel(excel_file_path)
#
# # 불러온 데이터 출력
# print(loaded_df)
#
# # 데이터만 출력
# data = loaded_df.values.tolist()
# print(data)
#
# import pandas as pd
# import matplotlib.pyplot as plt



######################
# 열 이름과 해당 열의 값
# columns_and_values = {
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.24,
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.22
# }
columns_and_values = {
    'th_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.42,
    'th_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.33
}

# 데이터프레임 생성
result_df = pd.DataFrame(columns_and_values.items(), columns=['Preprocessing Method', 'Success Rate'])

excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\{lan}\결과\{3}\태국어_전처리_with_result_updated_test7_black_background_kernel_3_원본_0.01_결과만.xlsx'
result_df.to_excel(excel_file_path, index=False)

# 엑셀 파일 불러오기
loaded_df = pd.read_excel(excel_file_path)

# 불러온 데이터 출력
print(loaded_df)

# 데이터만 출력
data = loaded_df.values.tolist()
print(data)

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
# 'orange'는 RGB 값으로 (255, 165, 0)이고, 'skyblue'는 (135, 206, 235)
colors = ['orange' if rate == max(result_df['Success Rate']) else 'skyblue' for rate in result_df['Success Rate']]
colors = [(255/255, 165/255, 0/255) if rate == max(result_df['Success Rate']) else (135/255, 206/255, 235/255) for rate in result_df['Success Rate']]
for bar, color in zip(bars, colors):
    bar.set_color(color)

# 각 막대 위에 성공률 값 표
# 주황색에 대비가 잘 되는 보라색의 RGB 값은 (128, 0, 128)
# (0, 128/255, 0)  # 어두운 녹색 계통
# text_color = (1, 0, 0)  # 밝은 빨간색 계통
for bar, rate in zip(bars, result_df['Success Rate']):
    # plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, str(rate),
    #          ha='center', va='bottom', fontsize=10, color='black')
    # plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.002, str(rate),
    #          ha='center', va='bottom', fontsize=10, color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0001, str(rate),
             ha='center', va='bottom', fontsize=10, color=(1, 0, 0))

# x 축과 y 축 라벨 설정
plt.xlabel('전처리 방법', fontsize=12, color=(128/255, 128/255, 128/255))
plt.ylabel('성공률', fontsize=12, color=(128/255, 128/255, 128/255))

# 그래프 제목 설정
#plt.title('vi_white_background_1410_1110 * 4_filter_kernel_3 전처리 방법별 성공률', fontsize=14, color='black')
plt.title(fr'{lan}_white_background_kernel_3 전처리 방법별 성공률', fontsize=14, color=(150/255, 150/255, 150/255))


# x 축 라벨을 사선으로 기울여 표시
# plt.xticks(rotation=45, fontsize=10, color='black')
# plt.yticks(fontsize=10, color='black')
# plt.xticks(rotation=10)
# text_color = (139/255, 69/255, 19/255)  # 어두운 갈색 계통
# plt.xticks(rotation=45, fontsize=10, color=(128/255, 128/255, 128/255))
# plt.yticks(fontsize=10, color=(128/255, 128/255, 128/255))
# plt.xticks(rotation=10)
plt.xticks(rotation=45, fontsize=10, color=(139/255, 69/255, 19/255))
plt.yticks(fontsize=10, color=(139/255, 69/255, 19/255))
plt.xticks(rotation=10)

# 그래프 출력
plt.tight_layout()
plt.show()
