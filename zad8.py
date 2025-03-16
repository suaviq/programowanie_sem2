# Obrót sekwencyjny
# a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
# końcowy.
# b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.


import cv2 
import imutils 

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

rotated_1 = imutils.rotate(image, 30)
rotated_2 = imutils.rotate(rotated_1, 30)
rotated_3 = imutils.rotate(rotated_2, 30)
cv2.imshow("Rotated three times", rotated_3)
cv2.waitKey(0)