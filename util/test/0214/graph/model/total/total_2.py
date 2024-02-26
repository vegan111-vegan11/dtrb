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

# 서브플롯 설정
fig, axes = plt.subplots(nrows=1, ncols=len(dfs), subplot_kw={'projection': '3d'}, figsize=(12, 6))

# 마커 설정
markers = ['o', 's']  # 모델에 따라 다른 마커 설정
label_text = ['None-VGG-BiLSTM-CTC-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111']  # 모델에 따른 범례 텍스트

# 각 서브플롯에 데이터 시각화
for df, ax, label in zip(dfs, axes, label_text):
    sc = ax.scatter(df['epoch'], df['number_of_training_images'], df['train_loss'], c=df['batch_ratio'], cmap='coolwarm', marker=markers.pop(0))
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Number of Training Images')
    ax.set_zlabel('Train Loss')
    ax.set_title(label)

# 컬러바 설정
cbar = plt.colorbar(sc, ax=axes.ravel().tolist())
cbar.set_label('Batch Ratio')

# 전체 그래프 저장
plt.savefig(r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\3d_subplots.png')
plt.show()
