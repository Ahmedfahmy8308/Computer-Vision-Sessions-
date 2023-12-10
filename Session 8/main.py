import cv2
import numpy as np

lower = np.array([110, 150, 0])
upper = np.array([130, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lower, upper)

    mask_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 0:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cv2.imshow("window", frame)

    k = cv2.waitKey(1)
    if k == 27:
        break