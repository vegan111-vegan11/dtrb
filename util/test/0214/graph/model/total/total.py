import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 데이터 파일 경로
file_paths = [
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_2.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_3.xlsx'
]

# 데이터 불러오기
dfs = [pd.read_excel(file) for file in file_paths]

# 3차원 그래프 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 마커 및 색깔 설정
markers = ['o', 's']  # 모델에 따라 다른 마커 설정
colors = ['blue', 'red']  # 배치 비율에 따라 다른 색상 설정
label_text = ['None-VGG-BiLSTM-CTC-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111']  # 모델에 따른 범례 텍스트

# 데이터 시각화
for df, marker, color, label in zip(dfs, markers, colors, label_text):
    ax.scatter(df['epoch'], df['number_of_training_images'], df['train_loss'], marker=marker, color=color, label=label)

# 축 및 라벨 설정
ax.set_xlabel('Epoch')
ax.set_ylabel('Number of Training Images')
ax.set_zlabel('Train Loss')
ax.set_title('3D Visualization of Training Loss over Epochs and Number of Training Images')
ax.legend()

# 컬러바 설정
cbar = plt.colorbar(ax.scatter([], [], [], c=[], cmap='coolwarm'), ax=ax)
cbar.set_label('Batch Ratio')

# 그래프 저장
plt.savefig(r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\3d_visualization.png')
plt.show()
