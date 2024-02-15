import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 데이터
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18]
]

# 요인 추출
background = [entry[0] for entry in data]
width = [entry[1] for entry in data]
height = [entry[2] for entry in data]
kernel = [entry[3] for entry in data]
rect = [entry[4] for entry in data]
ft = [entry[5] for entry in data]
result = [entry[6] for entry in data]

# 문자열 데이터를 숫자로 변환
factor_mapping = {
    'white': 0,
    'O': 0,
    'X': 1
}

background = [factor_mapping[item] for item in background]
rect = [factor_mapping[item] for item in rect]
ft = [factor_mapping[item] for item in ft]

# Figure 생성
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 데이터를 3D scatter plot으로 플로팅
scatter = ax.scatter(background, width, result, c=result, cmap='viridis', s=100)

# 축 및 레이블 설정
ax.set_xlabel('Background')
ax.set_ylabel('Width')
ax.set_zlabel('Result')
ax.set_title('Effect of Parameters on Result')

# 컬러 바 추가
cbar = fig.colorbar(scatter)
cbar.set_label('Result')

# 그래프 표시
plt.show()
