import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 데이터 프레임 생성
data = {
    'result': [0, 0, 0.04, 0.14, 0.25, 0.21, 0.25],
    'epoch': [0, 30000, 60000, 90000, 120000, 150000, 180000],
    'batch_ratio': [0.2] * 7,
    'total_data_usage_ratio': [0.2] * 7,
    'number_of_training_images_vi': [1052] * 7,
    'lan_of_training_images': ['vi', 'vi', 'vi', 'vi', 'vi', 'vi', 'vi']
}

df = pd.DataFrame(data)

# 실제 사용된 마커 및 배치 비율 추출
used_markers = df['lan_of_training_images'].unique()
used_batch_ratios = df['batch_ratio'].unique()

# 각 레이블에 따른 마커 스타일 지정
markers = {'vi': ('o', 'blue'), 'la': ('^', 'green'), 'vi_all': ('s', 'red')}

# 그래프 그리기
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 데이터 포인트 설정
for marker in used_markers:
    marker_data = df[df['lan_of_training_images'] == marker]
    for batch_ratio in used_batch_ratios:
        batch_data = marker_data[marker_data['batch_ratio'] == batch_ratio]
        if not batch_data.empty:
            ax.scatter(batch_data['epoch'], batch_data['number_of_training_images_vi'], batch_data['result'],
                       label=f'Marker: {marker}, Batch Ratio: {batch_ratio:.2f}',
                       marker=markers[marker][0], color=markers[marker][1])

            # 결과값을 숫자로 표시 (빨간색)
            for xi, yi, zi in zip(batch_data['epoch'], batch_data['number_of_training_images_vi'], batch_data['result']):
                ax.text(xi, yi, zi, f'{zi:.2f}', color='red', fontsize=8, zorder=1)

# 축 라벨 색상 변경 (회색)
ax.tick_params(axis='x', colors='gray')
ax.tick_params(axis='y', colors='gray')
ax.tick_params(axis='z', colors='gray')

# 축 레이블 설정 (회색)
ax.set_xlabel('Epoch', color='gray')
ax.set_ylabel('Number of Training Images (vi)', color='gray')
ax.set_zlabel('Result', color='gray')

# 타이틀 색상 변경 (파란색)
plt.title('Result over Epoch with Number of Training Images (vi) and Total Data Usage Ratio', color='blue')

# 범례 추가
ax.legend()

plt.show()
