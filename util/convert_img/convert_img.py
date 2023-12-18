import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지를 읽어오기
# image_path = 'path_to_your_image.jpg'  # 이미지 파일 경로로 변경해야 합니다.
image_path = r'C:\Users\TAMSystech\yjh\img\test\image-000000000.jpg'
image = cv2.imread(image_path)

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
else:
    # 색상 반전
    inverted_image = cv2.bitwise_not(image)

    # 검은색 부분만 약간 밝게 만들기 위한 값
    brightness_value = 20

    # 검은색 픽셀만 약간 밝게 만들기
    black_pixels = (inverted_image[:, :, 0] == 0) & (inverted_image[:, :, 1] == 0) & (inverted_image[:, :, 2] == 0)
    inverted_image[black_pixels, 0] += brightness_value  # 파란색 채널
    inverted_image[black_pixels, 1] += brightness_value  # 초록색 채널
    inverted_image[black_pixels, 2] += brightness_value  # 빨간색 채널

    # 픽셀값이 255를 넘어가지 않도록 클리핑
    inverted_image[inverted_image > 255] = 255

    # 색상 반전 및 검은색 부분만 약간 밝게 만든 이미지 표시
    plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # import cv2
    # import numpy as np
    # from matplotlib import pyplot as plt
    #
    # # 이미지를 읽어오기
    # image_path = r'C:\Users\TAMSystech\yjh\img\test\image-000000000.jpg'
    # image = cv2.imread(image_path)
    #
    # # 이미지가 제대로 로드되었는지 확인
    # if image is None:
    #     print("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
    # else:
    #     # 색상 반전
    #     inverted_image = cv2.bitwise_not(image)
    #
    #     # 검은색 픽셀만 찾아서 약간 밝게 만들기
    #     black_pixels = (inverted_image[:, :, 0] == 0) & (inverted_image[:, :, 1] == 0) & (inverted_image[:, :, 2] == 0)
    #     inverted_image[black_pixels] += 20
    #
    #     # 전체 이미지에 블러 처리
    #     blurred_image = cv2.GaussianBlur(inverted_image, (15, 15), 0)
    #
    #     # 색상 반전 및 검은색 부분만 약간 밝게 만든 이미지 표시
    #     plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    #     plt.axis('off')
    #     plt.show()

