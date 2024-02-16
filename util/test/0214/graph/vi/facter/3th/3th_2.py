import pandas as pd

# 데이터 생성
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18],
    ['white', 1410 * 2,	1110 * 2, 3, 'X', 'X',	0.22],
    ['white', 1410 * 4,	1110 * 4, 3, 'O', 'X',	0.08],
    ['white', 1410 * 4,	1110 * 4, 3, 'X', 'X',	0.34],
    ['white', 1410 * 8,	1110 * 8, 3, 'X', 'X',	0.18]
]

# 데이터프레임 생성
#df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Column1', 'Column2', 'Success Rate'])
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

# 엑셀 파일에 저장
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\vi\facter_vi.xlsx'
df.to_excel(excel_file_path, index=False)

# 엑셀 파일 불러오기
loaded_df = pd.read_excel(excel_file_path)

# 불러온 데이터 출력
print(loaded_df)

# 데이터만 출력
data = loaded_df.values.tolist()
print(data)

import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

x = [entry[1] for entry in data]
y = [entry[2] for entry in data]
z = [entry[6] for entry in data]

######################
# 데이터 불러오기
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\vi\facter_vi.xlsx'
loaded_df = pd.read_excel(excel_file_path)

# 데이터 전처리
background_mapping = {'white': 0, 'black': 1}
loaded_df['Background'] = loaded_df['Color'].map(background_mapping)
#loaded_df['Rect'] = loaded_df['Column1'].apply(lambda x: 'o' if x == 'O' else '^')  # 세모 또는 동그라미로 마커 지정
loaded_df['Rect'] = loaded_df['Rect'].apply(lambda x: 'O' if x == 'O' else '^')  # 세모 또는 동그라미로 마커 지정

# 데이터 시각화
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = loaded_df['Width']
y = loaded_df['Height']
z = loaded_df['Kernel']
c = loaded_df['Background']  # Color

s = loaded_df['Success Rate'] * 1000  # Success Rate 값을 기반으로 점의 크기 조절
s = loaded_df['Success Rate'] * 1000   # Success Rate 값을 기반으로 점의 크기 조절
m = [marker for marker in loaded_df['Rect']]  # 세모 또는 동그라미로 마커 지정
print(fr's : {s}')
print(fr'type(s) : {type(s)}')
print(fr'm : {m}')
print(fr'type(m) : {type(m)}')

# Scatter plot 그리기
#scatter = ax.scatter(x, y, z, c=c, s=100, marker='o', cmap='viridis', alpha=0.8)  # 일단 기본적으로 동그라미로 마커 설정
#scatter = ax.scatter(x, y, z, c=c, s=s,   cmap='viridis', alpha=0.8)  # 일단 기본적으로 동그라미로 마커 설정
scatter = ax.scatter(x, y, z, c=c, s=100,   cmap='viridis', alpha=0.5)  # 일단 기본적으로 동그라미로 마커 설정

ax.scatter(x, y, z)

ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Kernel')

plt.show()
