# Obrót w pętli
# a. Wykonaj pętlę, która obraca obraz co 15 stopni od 0 do 360 i wyświetla
# każdą wersję na ekranie.
# b. Dodaj opóźnienie cv2.waitKey(500) , aby obserwować zmiany.

import cv2 
import imutils 

image = cv2.imread("image.jpg")

for i in range(0, 361, 15):
    rotated = imutils.rotate(image, i)
    cv2.imshow("Rotating", rotated)
    cv2.waitKey(500)