# Liczenie i raportowanie kostek
# a. Na końcu całego procesu wyświetl w terminalu:
# i. liczbę wykrytych kostek
# ii. ich średnią szerokość i wysokość
# iii. minimalny i maksymalny rozmiar

import cv2
import imutils
import numpy as np

image = cv2.imread("kostka.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

widths = []
heights = []

for c in cnts:
    c = (c * ratio).astype("int")
    x, y, w, h = cv2.boundingRect(c)
    widths.append(w)
    heights.append(h)

print(f"Liczba wykrytych kostek: {len(cnts)}")
print(f"Średnia szerokość: {np.mean(widths):.2f}px, wysokość: {np.mean(heights):.2f}px")
print(f"Min. rozmiar: {min(widths)}x{min(heights)}px, Max: {max(widths)}x{max(heights)}px")
