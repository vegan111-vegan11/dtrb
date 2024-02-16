import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터프레임 생성
data = [
['black',	1410,	1110,	3,	'O',	'X',	0.01],
['white',	1410,	1110,	3,	'O',	'X',	0.03],
['white',	1410,	1110,	3,	'O',	'X',	0.05],
['white',	1410,	1110,	3,	'X',	'X',	0.03],
['white',	1410 * 2,	1110 * 2,	3,	'X',	'X',	0.34],
['white',	1410 * 2,	1110 * 2,	5,	'X',	'X',	0.21],
['white',	1410 * 2,	1110 * 2,	7,	'X',	'X',	0.1],
['white',	1410 * 2,	1110 * 2,	9,	'X',	'X',	0],
['white',	1410 * 2,	1110 * 2,	3,	'X',	'O',	0.90],

]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Column1', 'Column2', 'Success Rate'])

# 엑셀 파일에 저장
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\th\facter_th.xlsx'
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

# 엑셀 파일 경로
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\th\facter_th.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(excel_file_path)

# 데이터프레임 생성
#df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Column1', 'Column2', 'Success Rate'])
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

# 엑셀 파일에 저장
excel_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\facter\th\facter_th.xlsx'
df.to_excel(excel_file_path, index=False)

# 엑셀 파일 불러오기
loaded_df = pd.read_excel(excel_file_path)

# 불러온 데이터 출력
print(loaded_df)

# 데이터만 출력
data = loaded_df.values.tolist()
print(data)

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
for i, col in enumerate(df.columns[1:]):
    plt.subplot(2, 3, i + 1)
    sns.histplot(df[col], kde=True, color='gray')  # 회색 대신 원하는 색상을 선택할 수 있습니다.
    plt.title(f'Histogram of {col}')
plt.tight_layout()
plt.show()

# 산점도 행렬 그리기
sns.pairplot(df.drop(columns=['Color', 'Rect', 'Ft']), hue='Kernel', palette='husl')  # husl 색상 팔레트 사용
plt.suptitle('Pairplot of Variables')
plt.show()
