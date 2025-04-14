# Porównanie metod dodawania
# a. Wczytaj obraz i zwiększ jego jasność o 50 przy użyciu zarówno NumPy,
# jak i OpenCV.
# b. Sprawdź, jak różnią się wyniki.

import cv2
import numpy as np

image = cv2.imread("image.png")
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 50
added_cv2 = cv2.add(image, M)
added_np = image + M
cv2.imshow("cv2", added_cv2)
cv2.imshow("np", added_np)
cv2.waitKey(0)