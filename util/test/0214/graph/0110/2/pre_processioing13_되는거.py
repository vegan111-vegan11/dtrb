import pandas as pd
import matplotlib.pyplot as plt

# 열 이름과 해당 열의 값
columns_and_values = {
    'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result': 0.5,
    'vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_imageProcessing_result': 0.7
}

# 데이터프레임 생성
result_df = pd.DataFrame(columns_and_values.items(), columns=['Preprocessing Method', 'Success Rate'])

# 막대 그래프 시각화
result_df.plot(kind='bar', x='Preprocessing Method', y='Success Rate', color='skyblue')

# x 축과 y 축 라벨 설정
plt.xlabel('전처리 방법')
plt.ylabel('성공률')

# 그래프 제목 설정
plt.title('전처리 방법별 성공률')

# 그래프 출력
plt.tight_layout()
plt.show()
