import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 새로운 엑셀 파일 경로
excel_file3 = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\th\태국어_전처리_with_result_updated_kernel_7_0.64_결과만3.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file3)

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
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 100))
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# for (font, group), ax in zip(font_groups, axes.flatten()):
#     group.plot(kind='bar', x='Preprocessing Method', y='Success Rate', ax=ax, color='skyblue')
#     # ax.set_title(f'{font} 서식', fontsize=12)
#     ax.set_title(f'{font} 서식', fontsize=12, color=(150/255, 150/255, 150/255))
#     # ax.set_xlabel('전처리 방법', fontsize=10)
#     # ax.set_ylabel('성공률', fontsize=10)
#     ax.set_xlabel('전처리 방법', fontsize=10, color=(128/255, 128/255, 128/255))
#     ax.set_ylabel('성공률', fontsize=10, color=(128/255, 128/255, 128/255))
#
#     #ax.tick_params(axis='x', labelrotation=45)
#     # ax.tick_params(axis='x', labelrotation=45,  color=(139 / 255, 69 / 255, 19 / 255))
#     # ax.tick_params(axis='y', color=(139/255, 69/255, 19/255))
#     # ax.tick_params(axis='x', labelrotation=45, color=(150/255, 150/255, 150/255),
#     #                labelcolor=(139 / 255, 69 / 255, 19 / 255))
#     ax.tick_params(axis='x', labelrotation=45, color=(150 / 255, 150 / 255, 150 / 255),
#                    labelcolor=(139 / 255, 69 / 255, 19 / 255))
#     ax.tick_params(axis='y', color=(150/255, 150/255, 150/255), labelcolor=(139 / 255, 69 / 255, 19 / 255))
#     # ax.tick_params(axis='x', labelrotation=45, color=(170/255, 170/255, 170/255),
#     #                labelcolor=(170/255, 170/255, 170/255))
#     # ax.tick_params(axis='y', color=(170/255, 170/255, 170/255), labelcolor=(170/255, 170/255, 170/255))
#
#     # ax.tick_params(axis='x', labelrotation=45, color=(139/255, 69/255, 19/255))
#     # ax.tick_params(axis='y', color=(139/255, 69/255, 19/255))
#     # x 축 눈금 설정
#     # ax.set_xticks(ax.get_xticks()[::2])  # x 축 눈금을 2 간격으로 설정
#     # # y 축 눈금 설정
#     # ax.set_yticks(ax.get_yticks()[::2])  # y 축 눈금을 2 간격으로 설정
#     import matplotlib.ticker as ticker
#
#     # x 축 눈금 설정
#     # ax.xaxis.set_major_locator(ticker.MultipleLocator(base=2))  # x 축 눈금 간격을 2로 설정
#     # # y 축 눈금 설정
#     # ax.yaxis.set_major_locator(ticker.MultipleLocator(base=0.1))  # y 축 눈금 간격을 0.1로 설정
#
#     ax.set_ylim(0, 1)  # y 축 범위 설정

for (font, group), ax in zip(font_groups, axes.flatten()):
    bars = group.plot(kind='bar', x='Preprocessing Method', y='Success Rate', ax=ax, color='skyblue')
    ax.set_title(f'{font} 서식', fontsize=12, color=(150 / 255, 150 / 255, 150 / 255))
    ax.set_xlabel('전처리 방법', fontsize=10, color=(128 / 255, 128 / 255, 128 / 255))
    ax.set_ylabel('성공률', fontsize=10, color=(128 / 255, 128 / 255, 128 / 255))
    ax.tick_params(axis='x', labelrotation=45, color=(150 / 255, 150 / 255, 150 / 255),
                   labelcolor=(139 / 255, 69 / 255, 19 / 255))
    ax.tick_params(axis='y', color=(150 / 255, 150 / 255, 150 / 255), labelcolor=(139 / 255, 69 / 255, 19 / 255))
    ax.set_ylim(0, 1)  # y 축 범위 설정

    # x 축 눈금 설정
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=2))  # x 축 눈금 간격을 2로 설정
    # y 축 눈금 설정
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base=0.1))  # y 축 눈금 간격을 0.1로 설정

    # 각 막대 위에 성공률 값 표시
    for bar, rate in zip(bars.patches, group['Success Rate']):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, f'{rate:.2f}',
                ha='center', va='bottom', fontsize=8, color=(255/255, 100/255, 203/255))


# 서브플롯 간 간격 조절

plt.tight_layout()
plt.show()


###########
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 열 이름과 해당 열의 값
# columns_and_values = {
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.24,
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.22
# }
# columns_and_values = {
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.24,
#     'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.22
# }
#
# # 데이터프레임 생성
# result_df = pd.DataFrame(columns_and_values.items(), columns=['Preprocessing Method', 'Success Rate'])
#
# # 한글 폰트 설정
# import matplotlib.font_manager as fm
# font_path = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# for font in font_path:
#     if 'malgun' in font.lower():
#         plt.rcParams['font.family'] = 'Malgun Gothic'
#         break
#
# # 막대 그래프 시각화
# plt.figure(figsize=(10, 6))  # 그래프의 크기 조정
# bars = plt.bar(result_df['Preprocessing Method'], result_df['Success Rate'])
#
# # 성공률에 따라 색상 지정
# # 'orange'는 RGB 값으로 (255, 165, 0)이고, 'skyblue'는 (135, 206, 235)
# colors = ['orange' if rate == max(result_df['Success Rate']) else 'skyblue' for rate in result_df['Success Rate']]
# colors = [(255/255, 165/255, 0/255) if rate == max(result_df['Success Rate']) else (135/255, 206/255, 235/255) for rate in result_df['Success Rate']]
# for bar, color in zip(bars, colors):
#     bar.set_color(color)
#
# # 각 막대 위에 성공률 값 표
# # 주황색에 대비가 잘 되는 보라색의 RGB 값은 (128, 0, 128)
# # (0, 128/255, 0)  # 어두운 녹색 계통
# # text_color = (1, 0, 0)  # 밝은 빨간색 계통
# for bar, rate in zip(bars, result_df['Success Rate']):
#     # plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, str(rate),
#     #          ha='center', va='bottom', fontsize=10, color='black')
#     # plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.002, str(rate),
#     #          ha='center', va='bottom', fontsize=10, color='black')
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0001, str(rate),
#              ha='center', va='bottom', fontsize=10, color=(1, 0, 0))
#
# # x 축과 y 축 라벨 설정
# plt.xlabel('전처리 방법', fontsize=12, color=(128/255, 128/255, 128/255))
# plt.ylabel('성공률', fontsize=12, color=(128/255, 128/255, 128/255))
#
# # 그래프 제목 설정
# #plt.title('vi_white_background_1410_1110 * 4_filter_kernel_3 전처리 방법별 성공률', fontsize=14, color='black')
# plt.title('vi_white_background_1800_760 * 2_kernel_3 전처리 방법별 성공률', fontsize=14, color=(150/255, 150/255, 150/255))
#
#
# # x 축 라벨을 사선으로 기울여 표시
# # plt.xticks(rotation=45, fontsize=10, color='black')
# # plt.yticks(fontsize=10, color='black')
# # plt.xticks(rotation=10)
# # text_color = (139/255, 69/255, 19/255)  # 어두운 갈색 계통
# # plt.xticks(rotation=45, fontsize=10, color=(128/255, 128/255, 128/255))
# # plt.yticks(fontsize=10, color=(128/255, 128/255, 128/255))
# # plt.xticks(rotation=10)
# plt.xticks(rotation=45, fontsize=10, color=(139/255, 69/255, 19/255))
# plt.yticks(fontsize=10, color=(139/255, 69/255, 19/255))
# plt.xticks(rotation=10)
#
# # 그래프 출력
# plt.tight_layout()
# plt.show()



#############