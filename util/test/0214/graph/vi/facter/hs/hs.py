import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# 데이터프레임 생성
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 7200, 3040, 3, 'X', 'X', 0.34],
    ['white', 14400, 6080, 3, 'X', 'X', 0.18],
    ['white', 2820, 2220, 3, 'X', 'X', 0.22],
    ['white', 5640, 4440, 3, 'O', 'X', 0.08],
    ['white', 5640, 4440, 3, 'X', 'X', 0.34],
    ['white', 11280, 8880, 3, 'X', 'X', 0.18]
]
df = pd.DataFrame(data, columns=['Color', 'Width', 'Height', 'Kernel', 'Rect', 'Ft', 'Success Rate'])

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
for i, col in enumerate(df.columns[1:]):
    plt.subplot(2, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')
plt.tight_layout()
plt.show()

# 산점도 행렬 그리기
sns.pairplot(df.drop(columns=['Color', 'Rect', 'Ft']), hue='Kernel')
plt.suptitle('Pairplot of Variables')
plt.show()
