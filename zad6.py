# Eksperymentowanie z logiem OpenCV
# a. Pobierz logo OpenCV i rozdziel jego kanały.
# b. Spróbuj zamienić kolory tak, aby wyglądało inaczej, np. zamienić niebieski
# z czerwonym.
# c. Spróbuj usunąć jeden kanał całkowicie i sprawdź, jak wpłynie to na wygląd
# loga.
import cv2 
import numpy as np

image = cv2.imread("opencv.png")
(B, G, R) = cv2.split(image)
swapped = cv2.merge([R, G, B])

G_empty = np.zeros_like(G)  

no_green = cv2.merge([B, G_empty, R])

cv2.imshow("Original", image)
cv2.imshow("Swapped", swapped)
cv2.imshow("No green", no_green)

cv2.waitKey(0)