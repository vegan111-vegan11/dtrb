import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 경로
excel_file = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0110\vi\vi_전처리_with_result_updated_test7_white_background_1800_760_2_kernel_3_원본_0.24.xlsx'

# 엑셀 파일 읽기
result_df = pd.read_excel(excel_file)

# 'result'로 끝나는 열을 필터링하여 해당 열의 이름을 x 축에, 각 열의 마지막 행 값의 성공률을 y 축에 설정하여 시각화
for col in result_df.columns:
    if col.endswith('result'):
        plt.bar(col, result_df[col].iloc[-1])  # 각 열의 마지막 행 값만을 사용하여 성공률을 가져옴

# x 축과 y 축 라벨 설정
plt.xlabel('전처리 방법')
plt.ylabel('성공률')

# 그래프 제목 설정
plt.title('전처리 방법별 성공률')

# x 축 눈금 라벨 회전
plt.xticks(rotation=90)

# 그래프 출력
plt.tight_layout()
plt.show()
