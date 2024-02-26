import pandas as pd
import matplotlib.pyplot as plt

# 4개의 엑셀 파일 경로 리스트
file_paths = [
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_1.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_2.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_3.xlsx',
    r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat_4.xlsx'
]

# 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

for file_path, ax in zip(file_paths, axes.flat):
    # 엑셀 파일 불러오기
    df = pd.read_excel(file_path)

    # 'epoch'에 따른 'result' 값을 선 그래프로 플롯
    ax.plot(df['epoch'], df['result'])

    # 축 및 타이틀 설정
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Result')
    ax.set_title(f'Epoch vs. Result - {file_path}')

plt.tight_layout()
plt.show()
