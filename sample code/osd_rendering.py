#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np
import os
import requests
import threading
from datetime import datetime
from queue import Queue

INPUT_IMG_WIDTH = 1280
INPUT_IMG_HEIGHT = 720
INPUT_FPS = 5

class AlprThread(threading.Thread):
    api_url = 'http://localhost:8080/file/image/recognize?path='

    def __init__(self, host_img_path, container_img_path, img_width, img_height):
        super(AlprThread, self).__init__()
        self.host_img_path = host_img_path
        self.container_img_path = container_img_path
        self.img_width = img_width
        self.img_height = img_height
        self.queue = Queue()
        self.signal = threading.Event()

    def run(self):
        while not self.signal.isSet():
            if self.queue.qsize() > 0:
                frame = self.queue.get()
                self._process_alpr(frame)

    def join(self, timeout=None):
        self.signal.set()
        super(AlprThread, self).join(timeout)

    def _process_alpr(self, frame):
        time = datetime.now()
        tmp_img_name = time.strftime('%Y%m%d-%H%M%S-%f')[:-3] + '.jpg'
        tmp_img_path = os.path.join(self.host_img_path, tmp_img_name)
        cv2.imwrite(tmp_img_path, frame)
        try:
            input_img_path = os.path.join(self.container_img_path, tmp_img_name)
            res = requests.get(self.api_url + input_img_path).json()
            if isinstance(res, list) and len(res) > 0:
                plate = res[0]['plate']
                polygon = res[0]['polygon']
                confidence = res[0]['confidence']
                points = []
                for vertex in polygon:
                    vertex[0] = int(vertex[0] * self.img_width)
                    vertex[1] = int(vertex[1] * self.img_height)
                    points.append(vertex)
                points = np.array(points, np.int32)
                draw_plate(frame, points)
                draw_text(frame, 'Plate:{} Confidence:{:.2f}'.format(plate, confidence))
                cv2.polylines(frame, pts=[points], isClosed=True, color=(0,0,255), thickness=2)

                res_img_name = tmp_img_name.replace('.jpg', '_{}.jpg'.format(plate))
                res_img_path = os.path.join(self.host_img_path, res_img_name)
                cv2.imwrite(res_img_path, frame)
        except Exception as e:
            print(e)
        finally:
            if os.path.isfile(tmp_img_path):
                os.remove(tmp_img_path)

def draw_text(img, text,
          font=cv2.FONT_HERSHEY_COMPLEX,
          pos=(10, 10),
          font_scale=1,
          font_thickness=2,
          text_color=(0, 255, 0),
          text_color_bg=(0, 0, 0)
          ):
    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

def draw_plate(img, src_points):
    src_points = src_points.astype(np.float32)
    dst_points = np.array([[0, 0], [190, 0], [190, 80], [0, 80]],np.float32)
    pmat = cv2.getPerspectiveTransform(src_points, dst_points)
    perspective = cv2.warpPerspective(img, pmat, (190, 80), cv2.INTER_LINEAR)
    img[10:90, 1080:1270] = perspective

def main(args):
    if not os.path.isdir(args.host_path):
        print('folder {} not exists'.format(args.host_path))
        return

    cap = cv2.VideoCapture(args.camera_id, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, INPUT_IMG_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, INPUT_IMG_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, INPUT_FPS)

    frame_num = 0
    alpr_thread = AlprThread(args.host_path, args.container_path, INPUT_IMG_WIDTH, INPUT_IMG_HEIGHT)
    alpr_thread.start()

    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if frame_num % INPUT_FPS == 0:
            alpr_thread.queue.put(frame)
        frame_num += 1

    cap.release()
    alpr_thread.join()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--host-path', type=str, required=True, help='image path on host')
    parser.add_argument('-c', '--container-path', type=str, required=True, help='image path on container')
    parser.add_argument('-i', '--camera-id', type=int, required=True, help='usb camera id')
    args = parser.parse_args()
    main(args)
