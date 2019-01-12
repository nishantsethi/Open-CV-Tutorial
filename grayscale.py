import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Window', gray)
    cv2.imshow('Color WIndow', frame)
    if cv2.waitKey(20) & 0xFF == ord('s'):
        break
