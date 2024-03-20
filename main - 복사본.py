import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import cv2
from logfiles import logger
import re
import torch
import numpy as np
from pororo import Pororo
from pororo.pororo import SUPPORTED_TASKS
from utils.image_util import plt_imshow, put_text
import warnings
import socket, threading
# from easyocr import Reader
from easyocr.easyocr import Reader

import sys
import time

from PIL import Image

# import hunspell
# from pykospacing import Spacing

image_path = "C:/LGE_INSPECTION/"

warnings.filterwarnings('ignore')


# spacing = Spacing()
# hp = hunspell.Hunspell("ko")

class PororoOcr:
    def __init__(self, model: str = "brainocr", lang: str = "ko", **kwargs):
        self.model = model
        self.lang = lang
        self.eomodel = False
        self.coord_list = []

        if lang == "ko":  # wwww
            self._ocr = Pororo(task="ocr", lang=lang, model=model, **kwargs)
            self.eomodel = False
        else:

            # 원본 모델 사용시
            # self._ocr = Reader(["en", lang], gpu=torch.cuda.is_available())
            #self._ocr = Reader(["en", lang], gpu=torch.cuda.is_available())
            self._ocr = Reader([lang], gpu=torch.cuda.is_available())

            # 사용자 정의 모델 사용시
            # self._ocr = Reader(['th', 'en'], recog_network='None_VGG_BiLSTM_CTC_th')
            # self._ocr = Reader(['th', 'en'], recog_network='None_VGG_BiLSTM_CTC_th2')
            # self._ocr = Reader(['vi', 'en'], recog_network='None_VGG_BiLSTM_CTC_vi2')
            print(f'Reaader : {Reader}')

            print('테스트용 start ====================================================================')
            #
            img_path = r'D:\pythonlib\misc\data\img\image-000000001.jpg'

            image = cv2.imread(img_path, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            '''
            se = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            eroded_image = cv2.erode(gray, se)
            '''

            self.ocr_result = self._ocr.readtext(gray, detail=1, beamWidth=40)

            self.coord_list = []

            text_list = []

            for idx, text_result in enumerate(self.ocr_result):
                text = text_result[1]

                text_list.append(text)

                coord = text_result[0]

                self.coord_list.append(coord)

            ocr_text = text_list

            print(f'############### ocr_text: {ocr_text}')
            print('# 테스트용 end ====================================================================')

            self.eomodel = True

        self.img_path = None

        self.ocr_result = {}

    def run_ocr(self, img_path: str, debug: bool = False):

        print(f'img_path : {img_path}')

        self.img_path = img_path

        if self.lang == "ko":  # wwww

            self.ocr_result = self._ocr(img_path, detail=True)
            print(f'self.ocr_result : {self.ocr_result}')

            if self.ocr_result['description']:
                ocr_text = self.ocr_result["description"]
                print(f'ocr_text : {ocr_text}')
            else:
                ocr_text = "No text detected"

            if debug:
                self.show_img_with_ocr()
        else:
            # easyocr 에서의 ocr 결과값을 표현해줘야함

            image = cv2.imread(img_path, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            '''
            se = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            eroded_image = cv2.erode(gray, se)
            '''

            self.ocr_result = self._ocr.readtext(gray, detail=1, beamWidth=40)

            self.coord_list = []

            text_list = []

            for idx, text_result in enumerate(self.ocr_result):
                text = text_result[1]
                text_list.append(text)

                coord = text_result[0]
                self.coord_list.append(coord)

            ocr_text = text_list

            if debug:
                self.show_img_with_ocr()

        return ocr_text

    @staticmethod
    def get_available_langs():
        return SUPPORTED_TASKS["ocr"].get_available_langs()

    @staticmethod
    def get_available_models():
        return SUPPORTED_TASKS["ocr"].get_available_models()

    def get_ocr_result(self):
        return self.ocr_result

    def get_img_path(self):
        return self.img_path

    def show_img(self):
        plt_imshow(img=self.img_path)

    def show_img_with_ocr(self):

        img = cv2.imread(self.img_path)

        roi_img = img.copy()

        comparept = (-10, -10)  # EditedBywww
        intervals = []

        if self.eomodel:

            for idx, text_result in enumerate(self.ocr_result):
                text = text_result[1]

                # pts = ((tlX, tlY), (trX, trY), (brX, brY), (blX, blY))
                pts = self.coord_list[idx]

                pts = [[int(round(x)) for x in pair] for pair in pts]

                topLeft = pts[0]
                topRight = pts[1]
                bottomRight = pts[2]
                bottomLeft = pts[3]

                cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 1)

                cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 1)

                cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 1)

                cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 1)

                roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 35, font_size=25)

            filename = "result.jpg"

            # OpenCV의 BGR 포맷을 Pillow의 RGB 포맷으로 변환
            roi_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2RGB)

            # NumPy 배열을 PIL 이미지 객체로 변환
            pil_img = Image.fromarray(roi_img)

            # 이미지 저장
            pil_img.save(image_path + filename)

            logger.debug("PIL WRITE {} ".format(image_path + filename))

        else:

            for idx, text_result in enumerate(self.ocr_result['bounding_poly']):

                text = text_result['description']
                tlX = text_result['vertices'][0]['x']
                tlY = text_result['vertices'][0]['y']
                trX = text_result['vertices'][1]['x']
                trY = text_result['vertices'][1]['y']
                brX = text_result['vertices'][2]['x']
                brY = text_result['vertices'][2]['y']
                blX = text_result['vertices'][3]['x']
                blY = text_result['vertices'][3]['y']

                pts = ((tlX, tlY), (trX, trY), (brX, brY), (blX, blY))

                pts = [[int(round(x)) for x in pair] for pair in pts]

                logger.debug(pts)

                topLeft = pts[0]
                topRight = pts[1]
                bottomRight = pts[2]
                bottomLeft = pts[3]

                try:

                    cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 1)
                    cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 1)
                    cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 1)
                    cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 1)
                    roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 35, font_size=25)

                except Exception as e:

                    logger.debug(e)

            # plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))
            filename = "result.jpg"

            # OpenCV의 BGR 포맷을 Pillow의 RGB 포맷으로 변환
            roi_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2RGB)

            # NumPy 배열을 PIL 이미지 객체로 변환
            pil_img = Image.fromarray(roi_img)

            # 이미지 저장
            try:

                pil_img.save(image_path + filename)

            except Exception as e:

                logger.debug("Creating Err Result.jpg : {}".format(e))


def compare_answer(correctword, outputword):
    return all(char in outputword for char in correctword)


def imageProcessing(image_path):
    # 이미지를 그레이스케일로 읽어옵니다.
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 이미지가 제대로 로드되었는지 확인합니다.
    if image is None:
        logger.debug("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")
        raise ValueError("이미지를 로드하지 못했습니다. 경로를 확인해 주세요.")

    # Adaptive Thresholding을 적용하여 글자를 더욱 선명하게 합니다.
    sharpened_image = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    # 세로 선을 감지하기 위한 구조 요소를 생성합니다.
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))

    # erode와 dilate를 적용하여 세로 선을 제거합니다.
    # 이로 인해 글자가 더 얇게 보일 것입니다.
    sharpened_image = cv2.erode(sharpened_image, vertical_kernel, iterations=1)
    c = cv2.dilate(sharpened_image, vertical_kernel, iterations=1)

    point = 7

    # Gaussian Blur를 적용합니다.
    blurred_image = cv2.GaussianBlur(sharpened_image, (point, point), 0)

    # 다시 이진화를 적용합니다.
    _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 결과 이미지를 저장합니다.
    cv2.imwrite(image_path, binary_image)

    logger.debug("전처리 변경 완료")


def binder(client_socket, addr, ocr):
    print(f'binder client_socket : {client_socket}')
    print(f'binder addr : {addr}')
    print(f'binder ocr : {ocr}')

    try:
        # 접속 상태에서는 클라이언트로 부터 받을 데이터를 무한 대기한다.
        # 만약 접속이 끊기게 된다면 except가 발생해서 접속이 끊기게 된다.

        # socket의 recv함수는 연결된 소켓으로부터 데이터를 받을 대기하는 함수입니다. 최초 4바이트를 대기합니다.
        data = client_socket.recv(4)

        print(f'binder data : {data}')

        # 최초 4바이트는 전송할 데이터의 크기이다. 그 크기는 big 엔디언으로 byte에서 int형식으로 변환한다.
        # C#의 BitConverter는 big엔디언으로 처리된다.
        length = int.from_bytes(data, "big")
        # 다시 데이터를 수신한다.
        data = client_socket.recv(length)
        # 수신된 데이터를 str형식으로 decode한다.
        msg = data.decode()

        print(f'msg : {msg}')

        # 수신된 메시지를 콘솔에 출력한다.

        split_msg = msg.split('|')

        logger.debug(msg)

        if (split_msg[0] == "start inspection"):

            logger.debug('Received from {0}, {1}'.format(addr, msg))
            # 최종결과
            result = []
            # 문자인식 33
            filename = "inspection_img.jpg"

            img = cv2.imread(image_path + filename)

            # processedIMG = imageProcessing(ocr.lang, img)

            # cv2.imwrite(image_path + "processing_img.jpg", processedIMG)

            text = []

            start_time = time.time()  # 시작 시간 기록

            text = ocr.run_ocr(image_path + filename, debug=True)

            print(f'image_path : {image_path}')
            print(f'filename : {filename}')

            print(f'text : {text}')

            if not text:
                text = "NO TESTS WERE DETECTED"

            elif text == "No text detected":
                pass

            else:
                text = ','.join(text)

            if text.startswith(']'):
                text = "1";

            if "구김 방지 증" in text:
                text = text.replace("구김 방지 증", "구김 방지 중")

            if "케어 증" in text:
                text = text.replace("케어 증", "케어 중")

            if not compare_answer(split_msg[1], text):

                logger.debug("인식된 글씨가 다름, 전처리 변경")

                imageProcessing(image_path + filename)

                text = ocr.run_ocr(image_path + filename, debug=True)

                if not text:
                    text = "NO TESTS WERE DETECTED"

                elif text == "No text detected":
                    pass

                else:
                    text = ','.join(text)

                if text.startswith(']'):
                    text = "1";

                if "구김 방지 증" in text:
                    text = text.replace("구김 방지 증", "구김 방지 중")

                if "케어 증" in text:
                    text = text.replace("케어 증", "케어 중")

            end_time = time.time()  # 종료 시간 기록

            elapsed_time = end_time - start_time  # 걸린 시간 계산

            logger.debug(f"Code executed in {elapsed_time} seconds")

            logger.debug('RESULT TEXT: {0}'.format(text))

            msg = text
            # 바이너리(byte)형식으로 변환한다.
            data = msg.encode("utf-8")
            # 바이너리의 데이터 사이즈를 구한다.
            length = len(data)
            # 데이터 사이즈를 big 엔디언 형식으로 byte로 변환한 다음 전송한다.(※이게 버그인지 big을 써도 little엔디언으로 전송된다.)
            client_socket.sendall(length.to_bytes(4, byteorder='big'));
            # 데이터를 클라이언트로 전송한다.

            client_socket.sendall(data)

    except Exception as e:
        # 접속이 끊기면 except가 발생한다.
        logger.debug("except : {0}".format(e))
    finally:
        # 접속이 끊기면 socket 리소스를 닫는다.
        client_socket.close()


if __name__ == "__main__":

    logger.debug("INIT MSG")

    if len(sys.argv) > 1:

        language = sys.argv[1].lower()

        try:
            portNumber = int(sys.argv[2])

        except Exception as e:

            portNumber = 5199

        logger.debug("PYTHON START BY {0}, {1}".format(sys.argv[1], sys.argv[2]))

        ocr = PororoOcr(lang=language)

        # 소켓을 만든다.
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 소켓 레벨과 데이터 형태를 설정한다.

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 소켓 재사용 코든데 중복 설정을 피하기 위해 주석처리함

        # 서버는 복수 ip를 사용하는 pc의 경우는 ip를 지정하고 그렇지 않으면 None이 아닌 ''로 설정한다.
        # 포트는 pc내에서 비어있는 포트를 사용한다. cmd에서 netstat -an | find "LISTEN"으로 확인할 수 있다.
        try:
            server_socket.bind(('127.0.0.1', portNumber))

            logger.debug("SOCKET CREATED BY {0}".format(portNumber))

        except socket.error as e:

            logger.debug("SOCKET ERROR: {0}".format(e))

            server_socket.close()

            sys.exit(1)
        # server 설정이 완료되면 listen를 시작한다.

        server_socket.listen()

        try:
            while True:
                # client로 접속이 발생하면 accept가 발생한다.
                # 그럼 client 소켓과 addr(주소)를 튜플로 받는다.
                logger.debug("BEFORE ACCEPT")

                client_socket, addr = server_socket.accept()

                print(f'server_socket.accept client_socket : {client_socket}')
                print(f'server_socket.accept addr : {addr}')

                logger.debug("SERVER CREATED ")

                th = threading.Thread(target=binder, args=(client_socket, addr, ocr))
                # 쓰레드를 이용해서 client 접속 대기를 만들고 다시 accept로 넘어가서 다른 client를 대기한다.
                th.start()


        except Exception as ex:
            logger.debug("SERVER ERROR: {0}".format(ex))
        finally:
            # 에러가 발생하면 서버 소켓을 닫는다.
            server_socket.close()
    # TEST MODE
    else:
        portNumber = 51113

        clang = "ko"

        logger.debug("PYTHON START BY {}".format(clang))

        ocr = PororoOcr(lang=clang)

        # 소켓을 만든다.
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 소켓 레벨과 데이터 형태를 설정한다.

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 소켓 재사용 코든데 중복 설정을 피하기 위해 주석처리함

        # 서버는 복수 ip를 사용하는 pc의 경우는 ip를 지정하고 그렇지 않으면 None이 아닌 ''로 설정한다.
        # 포트는 pc내에서 비어있는 포트를 사용한다. cmd에서 netstat -an | find "LISTEN"으로 확인할 수 있다.
        try:
            server_socket.bind(('127.0.0.1', portNumber))

            logger.debug("SOCKET CREATED BY {0}".format(portNumber))

        except socket.error as e:

            logger.debug("SOCKET ERROR: {0}".format(e))

            server_socket.close()

            sys.exit(1)
        # server 설정이 완료되면 listen를 시작한다.

        server_socket.listen()

        try:
            while True:
                # client로 접속이 발생하면 accept가 발생한다.
                # 그럼 client 소켓과 addr(주소)를 튜플로 받는다.
                client_socket, addr = server_socket.accept()

                logger.debug("SERVER CREATED ")

                th = threading.Thread(target=binder, args=(client_socket, addr, ocr))
                # 쓰레드를 이용해서 client 접속 대기를 만들고 다시 accept로 넘어가서 다른 client를 대기한다.
                th.start()
        except Exception as ex:
            logger.debug("SERVER ERROR: {0}".format(ex))
        finally:
            # 에러가 발생하면 서버 소켓을 닫는다.
            server_socket.close()

