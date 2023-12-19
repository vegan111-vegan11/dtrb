from PIL import Image
import os
from IPython.display import display

# 이미지 파일 경로
input_image_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-18\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black\log\_resized_7.png'

# 출력 디렉토리
output_directory = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-18\skew_angle(0.0)\distorsion(0)\distorsion_orientation(0)\resize_orientation(0)\background(3)\background_rgb(0)\alignment(0)\blur(0.0)\NotoSansThaiLooped-Black\log'

# 디렉토리가 없으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

print(f'output_directory : {output_directory}')

# 이미지 열기
image = Image.open(input_image_path)

# 여백 크기 설정 (예: 20 픽셀)
margin_top = 20
margin_bottom = 20
margin_left = 20
margin_right = 20

# 새로운 이미지 크기 계산
new_width = image.width + margin_left + margin_right
new_height = image.height + margin_top + margin_bottom

new_width = image.width + margin_left + margin_right
new_height = image.height + margin_top + margin_bottom

# 새로운 이미지 생성 (검은 배경)
new_image = Image.new("RGB", (new_width, new_height), "black")
display(new_image)
# 원래 이미지를 새로운 이미지에 중앙에 배치
new_image.paste(image, (margin_left, margin_top))

# 저장할 파일 경로
output_image_path = os.path.join(output_directory, 'output_image_with_margin.png')
output_image_path = os.path.join(output_directory, 't.png')
display(new_image)
# 이미지 저장
new_image.save(output_image_path)

print(f"새로운 이미지가 {output_image_path}에 저장되었습니다.")
