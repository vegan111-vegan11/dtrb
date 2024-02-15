import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE

# 데이터
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18]
]

# 문자열 데이터를 숫자로 변환
factor_mapping = {
    'white': 0,
    'O': 0,
    'X': 1
}

factors = []
for entry in data:
    factors.append([factor_mapping[entry[i]] if isinstance(entry[i], str) else entry[i] for i in range(6)])
results = [entry[6] for entry in data]

# t-SNE를 사용하여 6차원 요인을 3차원으로 축소
tsne = TSNE(n_components=3, random_state=0)
embedded_factors = tsne.fit_transform(factors)

# 시각화
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# embedded_factors의 각 행은 3차원 좌표를 나타냄
x, y, z = embedded_factors[:, 0], embedded_factors[:, 1], embedded_factors[:, 2]

# 결과 값을 색상으로 표시
sc = ax.scatter(x, y, z, c=results, cmap='viridis', s=100)

# 축 레이블 설정
ax.set_xlabel('Dimension 1')
ax.set_ylabel('Dimension 2')
ax.set_zlabel('Dimension 3')
ax.set_title('t-SNE Visualization of Factors')

# 컬러 바 추가
cbar = fig.colorbar(sc)
cbar.set_label('Result')

# 그래프 표시
plt.show()
