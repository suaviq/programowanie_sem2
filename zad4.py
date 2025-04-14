# Tworzenie własnego "filtra Instagram":
# a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego
# +10.
# b. Sprawdź, jak zmienia się obraz.

import cv2
import numpy as np


image = cv2.imread("image.png")
cv2.imshow("Original", image)

blue, green, red = cv2.split(image)

red = cv2.add(red, 30)         
green = cv2.subtract(green, 20)    
blue = cv2.add(blue, 10)         

filtered = cv2.merge([blue, green, red])
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()