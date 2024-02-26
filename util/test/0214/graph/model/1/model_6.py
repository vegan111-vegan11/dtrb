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
sc_list = []  # scatter 플롯을 저장할 리스트
for i, row in df.iterrows():
    sc = ax.scatter(row['total_data_uwage_ratio'], row['number_of_training_images'], row['result'],
                    c=row['batch_ratio'], cmap='coolwarm', marker=markers[i], label=row['model'])
    sc_list.append(sc)  # scatter 플롯을 리스트에 추가

    # 각 데이터 포인트에 batch_ratio 값 표시
    ax.text(row['total_data_uwage_ratio'], row['number_of_training_images'], row['result'],
            f'Batch Ratio: {row["batch_ratio"]}', color='black', fontsize=10,
            bbox=dict(facecolor='white', alpha=0.7))

# 축 및 라벨 설정
ax.set_xlabel('Total Data Uwage Ratio')
ax.set_ylabel('Number of Training Images')
ax.set_zlabel('Result')
ax.set_title('3D Visualization')
ax.legend()

# 컬러바 설정
cbar = fig.colorbar(sc_list[0], ax=ax)  # 첫 번째 scatter 플롯의 컬러바를 사용
cbar.set_label('Batch Ratio')

# 그래프 출력
plt.show()
