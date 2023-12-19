from PIL import Image
import os
import numpy as np
import cv2

# 이미지 파일 경로
input_image_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\images2\output_image.jpg'

# 출력 디렉토리
output_directory = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\images2\black_background3'

# 디렉토리가 없으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 이미지 열기
image = Image.open(input_image_path)

# 이미지 크기 가져오기
image_size = image.size

# 새로운 이미지 생성 (검은 배경)
new_image = Image.new("RGB", image_size, "black")
new_image = Image.new("RGB", image_size, "pink")

# 저장할 파일 경로
output_image_path = os.path.join(output_directory, 'output_image_with_black_background.jpg')

# 이미지 저장
new_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")


##############

# OpenCV를 사용하여 이미지 배열로 변환
image_array = np.array(image)

# 이미지 블러 처리
blurred_image_array = cv2.GaussianBlur(image_array, (15, 15), 0)
#blurred_image_array = cv2.GaussianBlur(image_array, (333, 333), 0)
blurred_image = Image.fromarray(blurred_image_array)

# 검은색 배경 이미지에 블러 처리된 이미지를 합성
result_image = Image.alpha_composite(new_image.convert("RGBA"), blurred_image.convert("RGBA"))

# 저장할 파일 경로
output_image_path = os.path.join(output_directory, 'output_image_with_black_background_and_blur.png')
#output_image_path = os.path.join(output_directory, 'output_image_with_black_background_and_blur_333.png')

# 이미지 저장
result_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")


new_image = Image.new("RGB", image_size, "pink")


# 이미지 블러 처리
#blurred_image_array = cv2.GaussianBlur(image_array, (15, 15), 0)
blurred_image_array = cv2.GaussianBlur(image_array, (333, 333), 0)
blurred_image = Image.fromarray(blurred_image_array)

# 검은색 배경 이미지에 블러 처리된 이미지를 합성
result_image = Image.alpha_composite(new_image.convert("RGBA"), blurred_image.convert("RGBA"))

# 저장할 파일 경로
#output_image_path = os.path.join(output_directory, 'output_image_with_black_background_and_blur.jpg')
output_image_path = os.path.join(output_directory, 'output_image_with_black_background_and_blur_333.png')



# 이미지 저장
result_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")