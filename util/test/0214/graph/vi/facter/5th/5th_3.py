import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 데이터 불러오기
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\vi\facter_vi.xlsx'
loaded_df = pd.read_excel(excel_file_path)

# 데이터 전처리
background_mapping = {'white': 0, 'black': 1}
loaded_df['Background'] = loaded_df['Color'].map(background_mapping)
#loaded_df['Rect'] = loaded_df['Column1'].apply(lambda x: 'o' if x == 'O' else '^')  # 세모 또는 동그라미로 마커 지정
loaded_df['Rect'] = loaded_df['Rect'].apply(lambda x: 'O' if x == 'O' else '^')  # 세모 또는 동그라미로 마커 지정

# 데이터 시각화
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = loaded_df['Width']
y = loaded_df['Height']
z = loaded_df['Kernel']
c = loaded_df['Background']  # Color
#s = [marker for marker in loaded_df['Rect']]  # 세모 또는 동그라미로 마커 지정
s = loaded_df['Success Rate'] * 1000  # Success Rate 값을 기반으로 점의 크기 조절
s = loaded_df['Success Rate'] * 1000   # Success Rate 값을 기반으로 점의 크기 조절
m = [marker for marker in loaded_df['Rect']]  # 세모 또는 동그라미로 마커 지정
print(fr's : {s}')
print(fr'type(s) : {type(s)}')
print(fr'm : {m}')
print(fr'type(m) : {type(m)}')

# Scatter plot 그리기
#scatter = ax.scatter(x, y, z, c=c, s=100, marker='o', cmap='viridis', alpha=0.8)  # 일단 기본적으로 동그라미로 마커 설정
#scatter = ax.scatter(x, y, z, c=c, s=s,   cmap='viridis', alpha=0.8)  # 일단 기본적으로 동그라미로 마커 설정
scatter = ax.scatter(x, y, z, c=c, s=s,   cmap='viridis', alpha=0.5)  # 일단 기본적으로 동그라미로 마커 설정

# 세모 모양의 마커 지정
# for i in range(len(x)):
#     print(fr'i : {i}')
#     print(fr's[i] : {s[i]}')
#     print(fr'type(s[i]) : {type(s[i])}')
#     print(fr'm[i] : {m[i]}')
#     print(fr'type(m[i]) : {type(m[i])}')
#
#     # if s[i] == '^':
#     #     ax.scatter(x[i], y[i], z[i], c=c[i], s=100, marker='^', cmap='viridis', alpha=0.8)
#     # else:
#     #     s[i] == 'O'
#     #     ax.scatter(x[i], y[i], z[i], c=c[i], s=100, marker='^', cmap='viridis', alpha=0.8)
#     if m[i] == '^':
#         ax.scatter(x[i], y[i], z[i], c=c[i], s=s[i], marker=m[i], cmap='viridis', alpha=0.5)
#     else:
#         print('@@@@@@@@@@@@@ else 임')
#         ax.scatter(x[i], y[i], z[i], c=c[i], s=s[i], marker='2', cmap='viridis', alpha=0.5)
#         #ax.scatter(x[i], y[i], z[i], c=c[i], s=100, marker='o', cmap='viridis', alpha=0.8)

for i in range(len(x)):
    # 각 데이터 포인트의 위치를 약간씩 이동시켜 겹치지 않도록 함
    x_shifted = x[i] + np.random.normal(0, 0.1)
    y_shifted = y[i] + np.random.normal(0, 0.1)
    z_shifted = z[i] + np.random.normal(0, 0.1)

    if m[i] == '^':
        ax.scatter(x_shifted, y_shifted, z_shifted, c=c[i], s=s[i], marker=m[i], cmap='viridis', alpha=0.5)
    else:
        ax.scatter(x_shifted, y_shifted, z_shifted, c=c[i], s=s[i], marker='o', cmap='viridis', alpha=0.5)
# 축 라벨 설정
ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Kernel')

# colorbar 설정
cbar = plt.colorbar(scatter)
cbar.set_label('Background')

# 그래프 제목 설정
plt.title('Effect of Width, Height, and Kernel on Result')

plt.show()
