# from PIL import Image
# import os
#pip install Pillow

font_dict = {'검정': 'Black', '굵게': 'Bold', '아주 굵게': 'ExtraBold',
             '아주 가늘게': 'ExtraLight', '가늘게': 'Light', '중간': 'Medium',
             '보통': 'Regular', '약간 굵게': 'SemiBold', '가늘게': 'Thin'
             }

font_list = ['가늘게', '아주 가늘게', '보통', '중간', '약간 굵게', '굵게', '아주 굵게', '검정']

# for font in font_list:
#     if font in font_dict:
#         font_value = font_dict[font]
#         print(f"font = '{font_value}'")
#     else:
#         print(f"font = '{font}'일 때, 딕셔너리에 대응하는 값이 없습니다.")

# 메모장에 Thin 없음
# font = 'Thin'
# font = 'ExtraLight'
# font = 'Regular'
# font = 'Medium'
# font = 'SemiBold'
# font = 'Bold'
# font = 'ExtraBold'
# font = 'Black'

# font = '가늘게'
# font = '아주 가늘게'
# font = '보통'
# font = '중간'
# font = '약간 굵게'
# #font = '굵게'
# #font = '아주 굵게'
# #font = '검정'


# 원본 이미지가 있는 경로
original_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf10\train\img\0\태국어'
original_path = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf10\train\img\{font}\태국어'

# 새로운 이미지를 저장할 경로
output_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf10\train\img\0\태국어'
output_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\ttf11\train\img\0\태국어'

# 좌우 및 위아래에 추가할 여백 크기
padding_size = 3000

# 원본 경로의 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(original_path) if f.endswith('.png') or f.endswith('.jpg')]

# 새로운 경로가 없으면 생성
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 각 이미지에 대해 처리
for image_file in image_files:
    # 이미지 열기
    image_path = os.path.join(original_path, image_file)
    img = Image.open(image_path)

    # 이미지에 좌우 및 위아래 여백 추가
    img_with_padding = Image.new('RGB', (img.width + 2 * padding_size, img.height + 2 * padding_size), (255, 255, 255))
    img_with_padding.paste(img, (padding_size, padding_size))

    # 새로운 이미지 저장
    output_file = os.path.join(output_path, image_file)
    img_with_padding.save(output_file)

print("이미지에 여백을 추가하여 저장되었습니다.")
