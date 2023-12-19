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

# OpenCV를 사용하여 이미지 배열로 변환
image_array = np.array(new_image)
#image_array = np.array(new_image)

# 이미지 블러 처리
blurred_image_array = cv2.GaussianBlur(image_array, (15, 15), 0)
#blurred_image_array = cv2.GaussianBlur(image_array, (99, 99), 0)
blurred_image = Image.fromarray(blurred_image_array)

# 저장할 파일 경로
output_image_path = os.path.join(output_directory, 'blur_15.png')

# 이미지 저장
blurred_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")
