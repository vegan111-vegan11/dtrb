import numpy as np
import pandas as pd

# 데이터 생성
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18],
    ['white', 1410 * 2, 1110 * 2, 3, 'X', 'X', 0.22],
    ['white', 1410 * 4, 1110 * 4, 3, 'O', 'X', 0.08],
    ['white', 1410 * 4, 1110 * 4, 3, 'X', 'X', 0.34],
    ['white', 1410 * 8, 1110 * 8, 3, 'X', 'X', 0.18]
]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

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
