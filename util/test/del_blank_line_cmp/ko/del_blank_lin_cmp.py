lan = 'ko'

man_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\ko\ko_man.txt'
auto_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\ko\ko_auto.txt'

with open(man_file_path, 'r', encoding='utf-8') as man_file:
    man_lines = man_file.readlines()

with open(auto_file_path, 'r', encoding='utf-8') as auto_file:
    auto_lines = auto_file.readlines()

# Find lines that are different
different_lines = []
print(fr'different_lines 1 : {different_lines}')

for i, (man_line, auto_line) in enumerate(zip(man_lines, auto_lines)):
    if man_line != auto_line:
        print(fr'man_line : {man_line}')
        print(fr'auto_line : {auto_line}')
        print('===================')

        different_lines.append(f"Line {i+1}: Manual - {man_line.strip()}, Auto - {auto_line.strip()}")

#print(fr'different_lines : {different_lines}')

# Write different lines to ko_diff.txt
diff_file_path = fr'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\{lan}\{lan}_diff.txt'
with open(diff_file_path, 'w', encoding='utf-8') as diff_file:
    for line in different_lines:
        #print(fr'line : {line}')
        diff_file.write(line + '\n')

print("차이가 발견된 라인은 ko_diff.txt 파일에 저장되었습니다.")
