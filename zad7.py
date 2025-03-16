# Porównanie warpAffine i imutils.rotate
# a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
# imutils.rotate .
# b. Porównaj wyniki i zwróć uwagę na różnice.
import cv2
import imutils

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_w = cv2.warpAffine(image, M, (w, h))
cv2.imshow(f"warpAffine", rotated_w)

rotated = imutils.rotate(image, 60)
cv2.imshow("imutils", rotated)
cv2.waitKey(0)
