# Obrót o dowolny kąt
# a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
# b. Wyświetl wynik.

import numpy as np
import cv2

x = 0
try:
    x = int(input('Podaj kat: '))
except ValueError:
    print('Napisz liczbe!!!!( ｡ •̀ ⤙ •́ ｡ )')
    exit(1)

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), x, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow(f"Rotated by {x} Degrees", rotated)
cv2.waitKey(0)