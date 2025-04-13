# Podział obrazu na siatkę
# a. Podziel obraz na 9 równych części (3x3).
# b. Wyświetl wszystkie części osobno.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)
h = image.shape[0] // 3
w = image.shape[1] // 3

for y in range(0, 3):
    for x in range(0, 3):
        cropped = image[y*h:(y+1)*h, x*w:(x+1)*w]
        cv2.imshow(f"x = {x+1}, y = {y+1}", cropped)

cv2.waitKey(0)
