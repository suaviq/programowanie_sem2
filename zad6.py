# Filtrowanie konturów po wielkości
# a. Zaimplementuj filtrację konturów – usuwaj bardzo małe lub bardzo duże
# kontury (np. te o powierzchni < 500 lub > 5000 pikseli).
# b. Zastosowanie: Eliminacja szumu lub niepożądanych obiektów.

import cv2
import imutils

image = cv2.imread("kostka.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

filtered_cnts = [c for c in cnts if 500 < cv2.contourArea(c) < 5000]
clone = image.copy()
for c in filtered_cnts:
    c = (c * ratio).astype("int")
    cv2.drawContours(clone, [c], -1, (255, 0, 0), 2)

cv2.imshow("Filtered contours", clone)
cv2.waitKey(0)
cv2.destroyAllWindows()
