import cv2
import numpy as np

img = cv2.imread('circulos.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 1, 20,
param1=10, param2=16, minRadius=1, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Resultado', img)
cv2.imwrite('circulos_detectados.png', img)
cv2.waitKey()