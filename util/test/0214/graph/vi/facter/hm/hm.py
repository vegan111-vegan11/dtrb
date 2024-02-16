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

# 문자열 데이터를 포함하지 않는 열 선택
numerical_df = df.select_dtypes(include=['int64', 'float64'])

# 상관관계 계산
corr = numerical_df.corr()

# 상관관계 히트맵 그리기
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
