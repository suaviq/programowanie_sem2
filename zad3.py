# 3. Przyciemnianie obrazu
# a. Zmniejsz jasność obrazu o 80 jednostek.
# b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.

import cv2
import numpy as np

image = cv2.imread("image.png")
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 80
added_cv2 = cv2.subtract(image, M)
added_np = image - M
cv2.imshow("cv2", added_cv2)
cv2.imshow("np", added_np)
cv2.waitKey(0)