# Kopiowanie i wklejanie fragmentu obrazu
# a. Przytnij określony fragment obrazu (np. o wymiarach 100x100 pikseli).
# b. Wklej ten fragment w inne miejsce na obrazie.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)
cropped = image[:100, :100]
image[100:200, 100:200] = cropped
cv2.imshow("Inserted image into original", image)
cv2.waitKey(0)