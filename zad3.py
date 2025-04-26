# Rekonstrukcja obrazu po manipulacji kanałami
# a. Zamień wartości kanałów miejscami, np. wyświetl obraz w kolejności R, B,
# G.
# b. Ustaw wartość jednego z kanałów na zero i zobacz, jak zmienia się wygląd
# obrazu.
import cv2

image = cv2.imread("parrot.png")
(B, G, R) = cv2.split(image)

new_image = cv2.merge([R, B, G])

cv2.imshow("BGR", image)
cv2.imshow("RGB", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()