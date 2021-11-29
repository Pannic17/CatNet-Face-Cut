import os

import cv2
import math

filename = 'H://Study/Year G/unity_python/std/cat_face_cut/cat_test_9.jpg'


def detect(filename):
    # detect the cat face by opencv haarcascade
    # return the coordinates of cat face
    # cv2级联分类器CascadeClassifier,xml文件为训练数据
    face_cascade = cv2.CascadeClassifier(
        'H://Study/Year G/unity_python/std/cat_face_cut/haarcascade_frontalcatface.xml')
    # 读取图片
    img = cv2.imread(filename)
    # 转灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.02,
                                          minNeighbors=5)
    # 绘制人脸矩形框
    for (x, y, w, h) in faces:
        w_delta = math.ceil(w * 0.1)
        h_delta = math.ceil(h * 0.1)
        print(w_delta, h_delta)
        print(x, y)

        # change the coordinate, increase the rectangle by 10% for each side and move up to include the ears
        x1 = x - w_delta
        y1 = y - h_delta * 2
        x2 = x + w + w_delta
        y2 = y + h

        # draw the cat face, originate and cut
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        # return x1, y1, x2, y2
    # 命名显示窗口
    cv2.namedWindow('cat')
    # 显示图片
    cv2.imshow('cat', img)
    # 保存图片
    cv2.imwrite('cxks.png', img)
    # 设置显示时间,0表示一直显示
    cv2.waitKey(0)
    return x1, y1, x2, y2


def cut(filename):
    # cut the cat face out according to the coordinates given by detection
    # return the image for saving
    nx1, ny1, nx2, ny2 = detect(filename)
    print(nx1, ny1, nx2, ny2)
    img = cv2.imread(filename)
    new = img[ny1:ny2, nx1:nx2]
    cv2.imshow('cut', new)
    cv2.waitKey(0)
    # return new

cut(filename)