import matplotlib.pyplot as plt

# 데이터 준비
categories = ['ThinQ', 'thina', 'fail', 'thino', 'สวัสดี', 'ภาษา', 'อาบา', 'เครื่องจ่ายน้ำยา', 'ลิ้นชักเครื่องจ่ายน้ำยา', 'ไอน้ำ']
success_rates = [0.33, 0, 0.34, 0, 1, 1, 0, 0, 1, 0]

# 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, success_rates, color=['lightblue', 'lightcoral', 'lightgreen', 'lightskyblue', 'lightpink', 'lightseagreen', 'lightgrey', 'lightgoldenrodyellow', 'lightcyan', 'lightsteelblue'])
plt.title('Success Rates by Category', fontsize=16)
plt.xlabel('Categories', fontsize=14)
plt.ylabel('Success Rate', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.ylim(0, 1)  # y 축 범위를 0에서 1로 설정

# 그리드 추가
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 각 바에 성공률 표시
for bar, rate in zip(bars, success_rates):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{rate:.2f}', ha='center', va='bottom', fontsize=10)

# 그래프 표시
plt.tight_layout()
plt.show()
