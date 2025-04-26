# Wykorzystanie maski do ekstrakcji koloru
# a. Wczytaj kolorowy obraz (np. kwiaty, samochód).
# b. Stwórz maskę w taki sposób, aby pozostawić tylko jeden wybrany kolor, a
# resztę obrazu zaciemnić.
# c. Wskazówka: użyj konwersji obrazu do przestrzeni barw HSV i maskowania
# na podstawie zakresu kolorów.

import cv2
import numpy as np

image = cv2.imread("pepper.bmp")
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

mask = cv2.inRange(hsv_img, lower_green, upper_green)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("HSV", hsv_img)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", result)
cv2.waitKey(0)