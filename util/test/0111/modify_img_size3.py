import cv2
import os

def invert_colors_and_save(image_path, output_path):
    # 이미지 파일이 존재하는지 확인
    if not os.path.isfile(image_path):
        print(f"이미지 파일이 존재하지 않습니다: {image_path}")
        return

    # 이미지 읽기
    img = cv2.imread(image_path)

    # 이미지가 정상적으로 읽혔는지 확인
    if img is None:
        print(f"이미지를 읽을 수 없습니다: {image_path}")
        return

    # 흰색 글씨가 있는 이미지를 흰 배경에 검은 글씨로 반전
    inverted_img = cv2.bitwise_not(img)

    # 저장 경로 생성
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 파일 이름 추출
    file_name = os.path.basename(image_path)

    # 반전된 이미지 저장
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, inverted_img)
    cv2.imwrite(output_file_path, img)
    print(f"반전된 이미지 저장 완료: {output_file_path}")

lan = 'vi'
lan = 'th'
# 주어진 디렉토리 설정
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_1410_1110\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_1410_1110\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black_inverted'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\ttf13\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\ttf13_{6}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

# 디렉토리 내의 모든 이미지 파일에 대해 반전 적용
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_directory, filename)
        invert_colors_and_save(image_path, output_directory)

print("반전 작업이 완료되었습니다.")
