# Wzmocnienie jednego z kanałów
# a. Zwiększ intensywność jednego z kanałów (np. kanału czerwonego) i
# zaobserwuj, jak wpływa to na końcowy wygląd obrazu.
# b. Możesz to zrobić poprzez dodanie stałej wartości do danego kanału, np. R= cv2.add(R, 50) .

import cv2

image = cv2.imread("parrot.png")
(B, G, R) = cv2.split(image)
R = cv2.add(R, 100)
new_image = cv2.merge([B, G, R])

cv2.imshow("Original", image)
cv2.imshow("R+100", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()