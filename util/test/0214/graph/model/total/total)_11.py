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

# 데이터 시각화
for model, group in df.groupby('model'):
    sc = ax.scatter(group['total_data_uwage_ratio'], group['number_of_training_images'], group['result'],
                    label=model, cmap='coolwarm')

# 축 및 라벨 설정
ax.set_xlabel('Total Data Uwage Ratio')
ax.set_ylabel('Number of Training Images')
ax.set_zlabel('Result')
ax.set_title('3D Visualization')

# 마커와 색상이 의미하는 바 표시
for i, txt in enumerate(df['model']):
    ax.text(df['total_data_uwage_ratio'][i], df['number_of_training_images'][i], df['result'][i],
            txt, color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

# 컬러바 설정
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label('Batch Ratio')

# 그래프 출력
plt.show()
