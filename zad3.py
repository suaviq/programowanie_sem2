# Przycięcie prawej połowy obrazu
# a. Przycięcie prawej połowy obrazu
# b. Wyświetl tylko prawą połowę.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
right_image = image[:, h//2:]
cv2.imshow("Right image", right_image)
cv2.waitKey(0)