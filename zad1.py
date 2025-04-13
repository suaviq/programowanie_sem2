# 1. Wybór ROI na podstawie współrzędnych
# a. Zdefiniuj ROI, który obejmuje lewy górny róg obrazu o wymiarach 100x100
# pikseli.
# b. Wyświetl wynik.


import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)

cropped = image[:100, :100]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)