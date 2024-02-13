vi_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\vi\vi.txt'
vi_removed_empty_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\vi\vi_빈문자열 제거_수동.txt'

# 파일 읽기
with open(vi_path, 'r', encoding='utf-8') as f1, open(vi_removed_empty_path, 'r', encoding='utf-8') as f2:
    # 각 파일의 라인 읽기
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# 두 파일 비교
for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
    # 라인이 다르면 출력
    if line1.strip() != line2.strip():
        print(f'Difference at line {line_num}:')
        print(f'vi.txt: {line1.strip()}')
        print(f'vi_빈문자열제거_수동.txt: {line2.strip()}')
        print('-' * 40)

print('Comparison complete.')
