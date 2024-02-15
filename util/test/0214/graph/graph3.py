import matplotlib.pyplot as plt

# 데이터
data = [
    ['white', 1800, 760, 3, 'O', 'X', 0.08],
    ['white', 1800, 760, 3, 'X', 'X', 0.22],
    ['white', 1800 * 4, 760 * 4, 3, 'X', 'X', 0.34],
    ['white', 1800 * 8, 760 * 8, 3, 'X', 'X', 0.18]
]

# background를 숫자로 변환
background_mapping = {'white': 0, 'black': 1}  # 예를 들어 'black'이 추가된 경우에 대비하여 추가
background = [background_mapping[entry[0]] for entry in data]
width = [entry[1] for entry in data]
height = [entry[2] for entry in data]
kernel = [entry[3] for entry in data]
rect = [entry[4] for entry in data]
ft = [entry[5] for entry in data]
result = [entry[6] for entry in data]

# 각 요인에 대한 scatter plot 생성
factors = [background, width, height, kernel, rect, ft]
factor_names = ['Background', 'Width', 'Height', 'Kernel', 'Rect', 'FT']

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i, (factor, factor_name) in enumerate(zip(factors, factor_names)):
    ax = axs[i // 3, i % 3]
    ax.scatter(factor, result, c=result, cmap='viridis', s=100)
    ax.set_xlabel(factor_name)
    ax.set_ylabel('Result')
    ax.set_title('Effect of {} on Result'.format(factor_name))

plt.tight_layout()
plt.show()
