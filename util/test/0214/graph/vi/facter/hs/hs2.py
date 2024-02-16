import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    sns.histplot(df[col], kde=True, color='gray')  # 회색 대신 원하는 색상을 선택할 수 있습니다.
    plt.title(f'Histogram of {col}')
plt.tight_layout()
plt.show()

# 산점도 행렬 그리기
sns.pairplot(df.drop(columns=['Color', 'Rect', 'Ft']), hue='Kernel', palette='husl')  # husl 색상 팔레트 사용
plt.suptitle('Pairplot of Variables')
plt.show()
