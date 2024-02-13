import os
import cv2
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg


folder_path = r'C:\Users\TAMSystech\yjh\img\라인명6\태국어'
base_src_path = r'C:\Users\TAMSystech\yjh\img\라인명7\태국어'
base_src_path = r'D:\img\line\vi'


base_dest_path = r'C:\Users\TAMSystech\yjh\img\라인명8\태국어'
base_src_path = r'D:\img\line\vi'
base_dest_path = r'C:\Users\TAMSystech\yjh\img\line9\th'
base_dest_path = r'C:\Users\TAMSystech\yjh\img\line10\th'
base_dest_path = r'D:\img\line\vi'
base_dest_path = r'D:\img\line_invert\vi'
base_src_path = r'D:\img\vi\rect'
base_dest_path = r'D:\img\vi\rect_invert'
base_src_path = r'D:\img\la\rect'
base_dest_path = r'D:\img\la\rect_invert'
base_dest_path = r'D:\deep-text-recognition-benchmark\data\la\rect_invert\train\img'
# 목적지 디렉토리가 없으면 생성
# if not os.path.exists(base_dest_path):
#     os.makedirs(base_dest_path)

# 폴더 내 모든 파일에 대해 반복
for src_font_dir in os.listdir(base_src_path):
    src_font_folder_path = os.path.join(base_src_path, src_font_dir)

    dest_font_folder_path = os.path.join(base_dest_path, src_font_dir)

    if not os.path.exists(dest_font_folder_path):
        os.makedirs(dest_font_folder_path)

    # 디렉토리인지 확인
    if os.path.isdir(src_font_folder_path):
        print(f"Processing font: {src_font_folder_path}")

        # 폰트 폴더 내 모든 파일에 대해 반복
        for file_name in os.listdir(src_font_folder_path):
            _, file_extension = os.path.splitext(file_name)
            if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
                image_path = os.path.join(src_font_folder_path, file_name)
                print(f'image_path : {image_path}')
                try:
                    # image_path = r'C:\Users\TAMSystech\yjh\img\test\image-000000000.jpg'
                    #                     image_path = r'C:\Users\TAMSystech\yjh\img\라인명7\태국어\Black\image-000000000.jpg'
                    #                     image_path = r'C:\Users\TAMSystech\yjh\img\test\image-000000000.jpg'
                    #                     image_path = r'C:\Users\TAMSystech\yjh\img\line8\th\Black\image-000000000.jpg'
                    #                     image_path = r'C:\Users\TAMSystech\yjh\img\라인명7\태국어\Black\image-000000000.jpg'
                    image = cv2.imread(image_path)
                    if image is not None:
                        # 색상 반전
                        #inverted_image = cv2.bitwise_not(image)
                        inverted_image = cv2.bitwise_not(image)
                        # 전체 이미지에 블러 처리
                        #blurred_image = cv2.GaussianBlur(inverted_image, (15, 15), 0)
                        # blurred_image = cv2.GaussianBlur(inverted_image, (15, 15), 0)

                        # 색상 반전 및 검은색 부분만 약간 밝게 만든 이미지 표시
                        #plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
                        #plt.axis('off')
                        #plt.show()

                        # 파일명 생성 (원본 파일명에 _blurred 추가)
                        #                         file_name = os.path.basename(image_path)
                        #                         file_name_without_extension, file_extension = os.path.splitext(file_name)
                        #                         dest_file_name = f"{file_name_without_extension}_blurred{file_extension}"

                        # 저장할 경로 생성
                        #dest_path = os.path.join(base_dest_path, file_name)
                        dest_path = os.path.join(dest_font_folder_path, file_name)

                        # 이미지 저장
                        #cv2.imwrite(dest_path, blurred_image)
                        cv2.imwrite(dest_path, inverted_image)

                    else:
                        print("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
                        # Continue with image processing...
                except Exception as e:
                    print(f"Error processing image {image_path}: {e}")
