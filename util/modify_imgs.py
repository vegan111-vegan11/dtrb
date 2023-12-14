gt_file_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\gt\th\gt.txt'
target_line_numbers = [1, 5, 8, 28, 34]
modify_imgs = []

# 파일 읽기
with open(gt_file_path, 'r', encoding='utf-8') as gt_file:
    gt_lines = gt_file.readlines()

# 지정된 라인 넘버에 해당하는 라인을 출력
for line_number in target_line_numbers:
    try:
        line = gt_lines[line_number]
        elements = line.strip().split('\t')  # 탭으로 분리
        first_element = elements[0]
        print(f"라인 {line_number}의 첫 번째 요소: {first_element}")
        modify_imgs.append(first_element)

    except IndexError:
        print(f"라인 {line_number}을 찾을 수 없습니다.")

print(f"modify_imgs : {modify_imgs}")