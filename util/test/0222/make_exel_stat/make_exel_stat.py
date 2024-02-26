import pandas as pd
import matplotlib.pyplot as plt
# 데이터 프레임 생성
data = {
    'result': [0, 0, 0.04, 0.14, 0.25, 0.21, 0.25],
    'epoch': [0, 30000, 60000, 90000, 120000, 150000, 180000],
    'batch_ratio': [0.2] * 7,
    'total_data_usage_ratio': [0.2] * 7,
    'number_of_training_images_vi': [1052] * 7
}

df = pd.DataFrame(data)

# Excel 파일로 저장
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat.xlsx'
df.to_excel(file_path, index=False)

print(fr'저장완료 file_path : {file_path}')

# Excel 파일에서 데이터 읽어오기
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\stat\stat.xlsx'
df = pd.read_excel(file_path)

# 데이터 시각화
plt.figure(figsize=(10, 6))
plt.plot(df['epoch'], df['number_of_training_images_vi'], marker='o', color='b', linestyle='-')
plt.title('Number of Training Images vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Number of Training Images')
plt.grid(True)
plt.show()