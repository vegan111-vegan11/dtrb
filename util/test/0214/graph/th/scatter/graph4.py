import pandas as pd

# 데이터 생성
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18],
    ['white', 1410 * 2,	1110 * 2, 3, 'X', 'X',	0.22],
    ['white', 1410 * 4,	1110 * 4, 3, 'O', 'X',	0.08],
    ['white', 1410 * 4,	1110 * 4, 3, 'X', 'X',	0.34],
    ['white', 1410 * 8,	1110 * 8, 3, 'X', 'X',	0.18]
]

data = [
['black',	1410,	1110,	3,	'O',	'X',	0.01],
['white',	1410,	1110,	3,	'O',	'X',	0.03],
['white',	1410,	1110,	3,	'O',	'X',	0.05],
['white',	1410,	1110,	3,	'X',	'X',	0.03],
['white',	1410 * 2,	1110 * 2,	3,	'X',	'X',	0.34],
['white',	1410 * 2,	1110 * 2,	5,	'X',	'X',	0.21],
['white',	1410 * 2,	1110 * 2,	7,	'X',	'X',	0.1],
['white',	1410 * 2,	1110 * 2,	9,	'X',	'X',	0],
['white',	1410 * 2,	1110 * 2,	3,	'X',	'O',	0.90],

]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Column1', 'Column2', 'Success Rate'])

# 엑셀 파일에 저장
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\vi\facter_vi.xlsx'
df.to_excel(excel_file_path, index=False)

# 엑셀 파일 불러오기
loaded_df = pd.read_excel(excel_file_path)

# 불러온 데이터 출력
print(loaded_df)

# 데이터만 출력
data = loaded_df.values.tolist()
print(data)

import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 경로
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\vi\facter_vi.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(excel_file_path)

# # 그래프 설정
# plt.figure(figsize=(10, 6))  # 그래프 크기 설정
#
# # 막대 그래프 그리기
# bars = plt.bar(df.index, df['Success Rate'], color='skyblue')
#
# # 각 막대 위에 성공률 값 표시
# for bar, rate in zip(bars, df['Success Rate']):
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f'{rate:.2f}',
#              ha='center', va='bottom', fontsize=10)
#
# # x 축과 y 축 라벨 설정
# plt.xlabel('Index', fontsize=12)
# plt.ylabel('Success Rate', fontsize=12)
#
# # 그래프 제목 설정
# plt.title('Success Rate by Index', fontsize=14)
#
# # 그래프 출력
# plt.tight_layout()
# plt.show()


# background를 숫자로 변환
background_mapping = {'white': 0, 'black': 1}  # 예를 들어 'black'이 추가된 경우에 대비하여 추가
background = [background_mapping[entry[0]] for entry in data]
background = [entry[0] for entry in data]
width = [entry[1] for entry in data]
height = [entry[2] for entry in data]
kernel = [entry[3] for entry in data]
rect = [entry[4] for entry in data]
ft = [entry[5] for entry in data]
result = [entry[6] for entry in data]

# 각 요인에 대한 scatter plot 생성
factors = [background, width, height, kernel, rect, ft]
factor_names = ['Background', 'Width', 'Height', 'Kernel', 'Rect', 'FT']

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i, (factor, factor_name) in enumerate(zip(factors, factor_names)):
    ax = axs[i // 3, i % 3]
    ax.scatter(factor, result, c=result, cmap='viridis', s=100)
    ax.set_xlabel(factor_name)
    ax.set_ylabel('Result')
    ax.set_title('Effect of {} on Result Th'.format(factor_name))

plt.tight_layout()
plt.show()
