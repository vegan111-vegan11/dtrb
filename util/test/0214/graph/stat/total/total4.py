import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 4개의 엑셀 파일 경로 리스트
file_paths = [
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_1.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_2.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_3.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_4.xlsx'
]

# 4개의 데이터프레임 생성
dfs = [pd.read_excel(file_path) for file_path in file_paths]

# 서브플롯 생성
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12), subplot_kw={'projection': '3d'})

# 각 서브플롯에 데이터 그래프 그리기
for i, (df, ax) in enumerate(zip(dfs, axes.flat)):
    used_markers = df['lan_of_training_images'].unique()
    used_batch_ratios = df['batch_ratio'].unique()
    cmap = plt.cm.get_cmap('coolwarm')
    markers = {'vi': 'o', 'la': '^', 'vi_all': 's', 'vi_all + la': 'D'}

    for marker in used_markers:
        marker_data = df[df['lan_of_training_images'] == marker]
        for batch_ratio in used_batch_ratios:
            batch_data = marker_data[marker_data['batch_ratio'] == batch_ratio]
            if not batch_data.empty:
                color = cmap(batch_ratio)
                ax.scatter(batch_data['epoch'], batch_data['number_of_training_images'], batch_data['result'],
                           label=f'Marker: {marker}, Color: Batch Ratio',
                           marker=markers[marker], color=color, edgecolor='none')  # 테두리 색을 없앰

                for xi, yi, zi in zip(batch_data['epoch'], batch_data['number_of_training_images'],
                                      batch_data['result']):
                    ax.text(xi, yi, zi, f'{zi:.2f}', color='red', fontsize=8, zorder=1)

    ax.set_xlabel('Epoch')
    ax.set_ylabel('Number of Training Images (vi)')
    ax.set_zlabel('Result')
    ax.set_title(f'Subplot {i+1}: Result over Epoch with Number of Training Images (vi) and Total Data Usage Ratio')

    ax.legend()

    # 컬러바 추가
    sc = ax.scatter([], [], [], c=[], cmap=cmap)
    cbar = fig.colorbar(sc, ax=ax, shrink=0.5, aspect=5)
    cbar.set_label('Batch Ratio')

    # 컬러바 라벨과 타이틀 색상 변경
    cbar.ax.yaxis.label.set_color('gray')
    cbar.ax.set_title('Batch Ratio', color='gray')

    # 라벨 색상 변경
    ax.xaxis.label.set_color('gray')
    ax.yaxis.label.set_color('gray')
    ax.zaxis.label.set_color('gray')

    # 라벨 눈금 색상 변경
    ax.tick_params(axis='x', colors='dimgray')
    ax.tick_params(axis='y', colors='dimgray')
    ax.tick_params(axis='z', colors='dimgray')

    # 라벨 눈금 크기 변경 (선택 사항)
    ax.xaxis.set_tick_params(labelsize=10)
    ax.yaxis.set_tick_params(labelsize=10)
    ax.zaxis.set_tick_params(labelsize=10)

plt.tight_layout()
plt.show()
