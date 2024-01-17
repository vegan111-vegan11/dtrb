import cv2
import os

def resize_and_save(image_path, output_path, scale_factor=2.0):
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

    # 이미지 크기 조정
    resized_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)

    # 저장 경로 생성
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 파일 이름 추출
    file_name = os.path.basename(image_path)

    # 크기가 조정된 이미지 저장
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, resized_img)
    print(f"크기가 조정된 이미지 저장 완료: {output_file_path}")

# 주어진 디렉토리 설정
lan = 'vi'
lan = 'test'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_2\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_2\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black_resized'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_1410_1110_2\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_1410_1110_2\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black_resized'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_2\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\test7_white_background_4\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black_resized'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}_rect\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}_rect_{2}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}_rect_{2}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}_rect_{4}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{2}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{4}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{4}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test7_white_background_1800_760_{8}\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\0115\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\0115\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

lan = 'th'
input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\val\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\val\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\val\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0116\val\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0115\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\0116\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

input_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\ttf13\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'
output_directory = fr'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\data\{lan}\test\ttf13\train\img\skew_angle(0.0)\blur(0.0)\NotoSansThaiLooped-Black'

# 디렉토리 내의 모든 이미지 파일에 대해 크기 조정 적용
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_directory, filename)
        #resize_and_save(image_path, output_directory, scale_factor=2.0)
        resize_and_save(image_path, output_directory, scale_factor=2.0)

print("크기 조정이 완료되었습니다.")
