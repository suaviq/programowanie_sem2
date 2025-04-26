# Ukrywanie określonego obszaru twarzy
# a. Wczytaj zdjęcie osoby.
# b. Stwórz maskę zasłaniającą oczy (np. prostokąt lub elipsa).
# c. Zastosuj maskę na obrazie i wyświetl wynik.

import cv2
import numpy as np

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (200, 400), (800, 500), 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)