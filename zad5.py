# Zastosowanie maski do selektywnej modyfikacji kanałów
# a. czytaj obraz i stwórz maskę obejmującą tylko wybrany obiekt (np.
# czerwony samochód).
# b. Wykorzystując maskę, zwiększ nasycenie koloru czerwonego tylko w tej
# części obrazu.

import cv2
import numpy as np

image = cv2.imread('red_sunflower.jpg')
cv2.imshow("Original Image", image)

mask = np.zeros(image.shape[:2], dtype="uint8") 
cv2.circle(mask, (250, 250), 200, 255, -1)  
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)

(B, G, R) = cv2.split(image)
R = cv2.add(R, 50)
new_image = cv2.merge([B, G, R])

cv2.imshow("Boosted Red Channel", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
