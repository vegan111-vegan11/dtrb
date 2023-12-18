# 되는거
import cv2
import matplotlib.pyplot as plt
from PIL import Image
image_path = r'C:\Users\TAMSystech\yjh\img\test\image-000000000.jpg'
# image_path = r'C:\Users\TAMSystech\yjh\img'
dest_path = r'C:\Users\TAMSystech\yjh\img\\test3'

image = Image.open(image_path)
# image.show()
# 이미지를 그레이스케일로 읽어옵니다.
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 이미지가 제대로 로드되었는지 확인합니다.
if image is None:
    print("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
else:
    # 색상 반전
    inverted_image = cv2.bitwise_not(image)

    # 반전된 이미지를 화면에 표시
    # plt.imshow(inverted_image, cmap='gray')
    # plt.show()

    # 검은색 픽셀만 찾아서 전체 이미지에 20만큼 밝게 만들기
    inverted_image[inverted_image == 0] += 20

    plt.imshow(inverted_image, cmap='gray')
    #plt.imshow(inverted_image)
    plt.show()

    # 전체 이미지에 블러 처리
    # blurred_image = cv2.GaussianBlur(inverted_image, (15, 15), 0)
    #
    # # 색상 반전 및 검은색 부분만 약간 밝게 만든 이미지 표시
    # plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    # plt.axis('off')
    # plt.show()


    # # 검은색 부분만 약간 밝게 만들기 위한 값
    # brightness_value = 20
    #
    # # 검은색 픽셀만 약간 밝게 만들기
    # black_pixels = (inverted_image == 0)
    # inverted_image[black_pixels] += brightness_value
    #
    # # 픽셀값이 255를 넘어가지 않도록 클리핑
    # #nverted_image[inverted_image > 255] = 255
    #
    # # 반전된 이미지를 화면에 표시
    # plt.imshow(inverted_image, cmap='gray')
    # plt.show()

