import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 데이터 파일 경로
file_paths = [
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_2.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_3.xlsx'
]

# 데이터 불러오기 및 서브플롯 설정
fig, axes = plt.subplots(nrows=1, ncols=len(file_paths), subplot_kw={'projection': '3d'}, figsize=(12, 6))

# 마커 및 색상 설정
markers = ['o', 'x']  # 모델에 따라 다른 마커 설정
label_text = ['None-VGG-BiLSTM-CTC-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111']  # 모델에 따른 범례 텍스트

# 각 엑셀 파일을 서브플롯에 그려주기
for i, file_path in enumerate(file_paths):
    # 엑셀 파일 읽어오기
    df = pd.read_excel(file_path)

    # 배치 비율에 따른 고유한 색상 지정
    unique_batch_ratios = sorted(df['batch_ratio'].unique())
    colors = plt.cm.get_cmap('coolwarm', len(unique_batch_ratios))

    # 서브플롯 설정
    ax = axes[i]

    # 데이터 시각화
    ax.scatter(df['epoch'], df['number_of_training_images'], df['train_loss'], marker=markers[i],
               #c=df['batch_ratio'], cmap='coolwarm', label=label_text[i])
               # c = df['batch_ratio'], cmap = 'coolwarm', label = label_text[i])
                c = df['batch_ratio'], cmap = 'coolwarm', label = label_text[i])


    # 축 및 라벨 설정
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Number of Training Images')
    ax.set_zlabel('Train Loss')
    ax.set_title(f'3D Visualization of {label_text[i]}')
    ax.legend()

    # 컬러바 설정
    cbar = plt.colorbar(ax.scatter([], [], [], c=[], cmap='coolwarm'), ax=ax)
    cbar.set_label('Batch Ratio')

# 전체 그래프 저장
plt.savefig(r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\3d_subplots.png')
plt.show()
