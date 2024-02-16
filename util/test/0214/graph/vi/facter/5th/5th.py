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
loaded_df['Rect'] = loaded_df['Column1'].apply(lambda x: 1 if x == 'O' else 0)

# 데이터 시각화
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = loaded_df['Width']
y = loaded_df['Height']
z = loaded_df['Kernel']
c = loaded_df['Background']  # Color
s = loaded_df['Rect'] * 100  # Size

# Scatter plot 그리기
scatter = ax.scatter(x, y, z, c=c, s=s, cmap='viridis', alpha=0.8)

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
