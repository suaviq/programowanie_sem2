# Zapis przyciętego obrazu
# a. Przytnij obraz do obszaru o wymiarach 300x300 pikseli.
# b. Zapisz wynik jako nowy plik cropped_image.jpg .

import cv2

image = cv2.imread("face_image.jpg")
cv2.imshow("Original", image)

cropped = image[:300, :300]
cv2.imwrite('cropped.jpg', cropped)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)