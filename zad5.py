# Kadrowanie twarzy
# a. Znajdź zdjęcie z twarzą.
# b. Znajdź obszar, w którym się znajduje, i przytnij obraz tak, aby pozostała
# tylko twarz.

import cv2

image = cv2.imread("face_image.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
print(h, w)

cropped = image[100:1500, 1000:2200]
cv2.imshow("Face image", cropped)
cv2.waitKey(0)