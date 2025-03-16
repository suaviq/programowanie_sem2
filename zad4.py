# Wykorzystanie funkcji imutils.translate
# a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
# imutils.translate .
# b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
# Czy zauważyłeś różnice?

import numpy as np
import cv2
import imutils 

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)