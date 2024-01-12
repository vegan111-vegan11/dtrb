import pandas as pd

# 파일 경로
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0112\vi\ocr_test_vi_전처리_with_result_updated_test7_white_background_1410_1110_4_filter_kernel_3_원본_수정_0.34_최종.xlsx'

# Excel 파일 읽기
df = pd.read_excel(file_path)

# 성공 및 실패 문장 추출
success_sentences = df[df['vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result'] == 'suc']['배트남어 문장'].sample(10)
failure_sentences = df[df['vi_NotoSansThaiLooped-Black_전처리_미디안필터_kernel_3_Sharpening_result'] == 'fail']['배트남어 문장'].sample(10)

# 추출된 문장을 새로운 DataFrame으로 저장
result_df = pd.DataFrame({'성공 문장': success_sentences, '실패 문장': failure_sentences})

# 새로운 Excel 파일로 저장
output_file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\ocr_test\0112\vi\ocr_test_vi_전처리_with_result_updated_test7_white_background_1410_1110_4_filter_kernel_3_원본_수정_0.34_최종_20.xlsx'
result_df.to_excel(output_file_path, index=False)

print(f'새로운 파일이 생성되었습니다: {output_file_path}')
