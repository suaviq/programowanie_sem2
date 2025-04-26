# Wyświetlenie pojedynczych kanałów na obrazie
# a. Wczytaj dowolny obraz.
# b. Rozdziel kanały B, G, R i wyświetl je osobno.
# c. Zapisz te kanały jako osobne obrazy.

import cv2

image = cv2.imread("image.png")
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imwrite('red.png', R)
cv2.imshow("Green", G)
cv2.imwrite('green.png', G)
cv2.imshow("Blue", B)
cv2.imwrite('blue.png', B)
cv2.waitKey(0)