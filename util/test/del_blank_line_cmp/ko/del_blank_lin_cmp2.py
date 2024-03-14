man_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\ko\ko_man.txt'
auto_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\ko\ko_auto.txt'

with open(man_file_path, 'r', encoding='utf-8') as man_file:
    man_lines = man_file.readlines()

with open(auto_file_path, 'r', encoding='utf-8') as auto_file:
    auto_lines = auto_file.readlines()

# Find lines that are different
different_lines = []
for i, (man_line, auto_line) in enumerate(zip(man_lines, auto_lines)):
    if man_line != auto_line:
        different_lines.append((i+1, man_line.strip(), auto_line.strip()))

# Print different lines
if different_lines:
    print("다음 라인들이 서로 다릅니다:")
    for line_number, man_line, auto_line in different_lines:
        print(f"라인 {line_number}: 수동 - {man_line}, 자동 - {auto_line}")
else:
    print("두 파일은 완전히 동일합니다.")
