# Eksperymentowanie z dużymi wartościami przesunięcia
# a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
# b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
# oryginalnego obrazu.

import numpy as np
import cv2

image = cv2.imread("image.jpg")
width = image.shape[1]
height = image.shape[0]
cv2.imshow("Original", image)

M = np.float32([[1, 0, width//2], [0, 1, height//2]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Left and Up", shifted)
cv2.waitKey(0) 