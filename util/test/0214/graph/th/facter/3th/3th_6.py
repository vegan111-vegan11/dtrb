import numpy as np
import pandas as pd

lan = 'th'
# 데이터 생성
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
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

# 엑셀 파일에 저장
excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\{lan}\facter_{lan}.xlsx'
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
excel_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\{lan}\facter_{lan}.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(excel_file_path)

# 데이터프레임 생성
#df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

# 중복을 제거하여 유일한 레이블 가져오기
unique_labels = df['Rect'].unique()

# 마커 정보 딕셔너리 생성
markers = {'O': 'o', 'X': 'x'}

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 배경 색상 설정
ax.set_facecolor('navy')

# 데이터 포인트 설정
# x = df['Width'] + np.random.normal(0, 300, size=len(df))
# y = df['Height']
x = df['Width'] + np.random.normal(0, 300, size=len(df))
y = df['Width'] + np.random.normal(0, 300, size=len(df))
# x = df['Height'] + np.random.normal(0, 500, size=len(df))
# y = df['Height'] + np.random.normal(0, 500, size=len(df))
z = df['Kernel']
c = df['Color']
m = df['Rect']
s = df['Success Rate'] * 1000
#s = df['Success Rate'] * 2000

# 산점도 그래프 그리기
for xi, yi, zi, ci, mi, si in zip(x, y, z, c, m, s):
    marker = markers.get(mi, 'o')  # 해당하는 마커가 없으면 기본값인 'o'를 사용합니다.
    ax.scatter(xi, yi, zi, s=si, c=ci, marker=marker)

# 각 데이터 포인트에 숫자 표시
for i in range(len(data)):
    ax.text(x[i], y[i], z[i], f'{data[i][6]:.2f}', color='orange')

# 축 레이블과 눈금 색상 설정
ax.set_xlabel('Width', color='grey')
ax.set_ylabel('Height', color='grey')
ax.set_zlabel('Kernel', color='grey')
ax.tick_params(axis='x', colors='brown')
ax.tick_params(axis='y', colors='brown')
ax.tick_params(axis='z', colors='brown')

# 범례 표시
for label in unique_labels:
    marker = markers.get(label, 'o')  # 해당하는 마커가 없으면 기본값인 'o'를 사용합니다.
    ax.scatter([], [], [], marker=marker, label=f'Rect: {label}')  # 범례에 해당 마커를 표시합니다.

ax.legend()

plt.show()
