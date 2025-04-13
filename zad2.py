# Przycięcie dolnej połowy obrazu
# a. Podziel obraz na dwie równe części (górną i dolną).
# b. Wyświetl tylko dolną połowę.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
upper_image = image[w//2:, :]
cv2.imshow("Bottom", upper_image)
cv2.waitKey(0)