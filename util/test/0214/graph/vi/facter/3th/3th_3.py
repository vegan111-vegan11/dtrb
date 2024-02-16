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
#fig = plt.figure(figsize=(10, 8))
fig = plt.figure(figsize=(40, 40))

#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='3d')
# 배경 색상 설정
ax.set_facecolor('navy')
x = [entry[1] for entry in data]
y = [entry[2] for entry in data]
z = [entry[3] for entry in data]
c = [entry[0] for entry in data]
s = [entry[6] * 1000 for entry in data]
#ax.scatter(x, y, z)
# Scatter plot 그리기
#ax.scatter(x, y, z, color='grey')
#ax.scatter(x, y, z, color='grey')
ax.scatter(x, y, z, s = s,  color=c)
# 각 데이터 포인트에 숫자 표시
for i in range(len(data)):
    ax.text(x[i], y[i], z[i], f'{data[i][6]:.2f}', color=(255/255, 165/255, 0/255))


ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Kernel')
# x, y 축 색상 설정
ax.xaxis.label.set_color('grey')
ax.yaxis.label.set_color('grey')
ax.xaxis.label.set_color('grey')
ax.zaxis.label.set_color('grey')
# x, y 축 눈금 색상 설정
ax.tick_params(axis='x', colors=(139 / 255, 69 / 255, 19 / 255))
ax.tick_params(axis='y', colors=(139 / 255, 69 / 255, 19 / 255))
ax.tick_params(axis='z', colors=(139 / 255, 69 / 255, 19 / 255))
plt.show()
