# Obrót i zapis obrazu
# a. Obróć obraz o 75 stopni i zapisz wynik do pliku rotated_output.jpg .
import cv2 
import imutils 

image = cv2.imread("image.jpg")
rotated = imutils.rotate(image, 30)
cv2.imwrite("rotated_output.jpg", rotated)