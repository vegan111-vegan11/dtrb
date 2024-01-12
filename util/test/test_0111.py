import cv2
import os

def invert_image_colors(image_path, output_path):
    # 이미지가 정상적으로 읽혔는지 확인
    if not os.path.isfile(image_path):
        print(f"이미지 파일이 존재하지 않습니다: {image_path}")
        return
    else:
        print(f"이미지 파일이 존재 : {image_path}")
    # 이미지 읽기
    img = cv2.imread(image_path)

    # 이미지가 정상적으로 읽혔는지 확인
    if img is None:
        print(f"이미지를 읽을 수 없습니다: {image_path}")
        return

    # 색상 반전
    inverted_img = cv2.bitwise_not(img)

    # 저장 경로 생성
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 파일 이름 추출
    file_name = os.path.basename(image_path)

    # 반전된 이미지 저장
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, inverted_img)
    print(f"반전된 이미지 저장 완료: {output_file_path}")

# 주어진 디렉토리 설정
input_directory = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black_inverted'

# 디렉토리 내의 모든 이미지 파일에 대해 반전 적용
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_directory, filename)
        invert_image_colors(image_path, output_directory)

print("색상 반전이 완료되었습니다.")
