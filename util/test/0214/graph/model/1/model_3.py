import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 데이터 파일 경로
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_1.xlsx'

# 엑셀 파일 읽어오기
df = pd.read_excel(file_path)

# 3차원 그래프 생성
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 마커 및 색상 설정
markers = ['o', 's']  # 모델에 따라 다른 마커 설정
colors = ['blue', 'red']  # 배치 비율에 따라 다른 색상 설정

# 데이터 시각화
for i, row in df.iterrows():
    ax.scatter(row['total_data_uwage_ratio'], row['number_of_training_images'], row['result'],
               marker=markers[i], color=colors[i], label=row['model'])

# 축 및 라벨 설정
ax.set_xlabel('total_data_uwage_ratio')
ax.set_ylabel('Nnumber_of_training_images')
ax.set_zlabel('result')
ax.set_title('3D Visualization')
ax.legend()

# 마커와 색상이 의미하는 바 표시
for marker, model in zip(markers, df['model']):
    ax.text(0, 0, 0, model, color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

for color, batch_ratio in zip(colors, df['batch_ratio']):
    ax.text(0, 0, 0, f'Batch Ratio: {batch_ratio}', color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

# 그래프 출력
plt.show()
