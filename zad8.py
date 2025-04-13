# Animacja przesuwającego się ROI
# a. Wczytaj obraz i dynamicznie przesuwaj ROI w poziomie (np. przesunięcie
# co 10 pikseli), aby stworzyć efekt „przesuwania kamery”.
# b. Wyświetlaj na ekranie kolejne wycinki ROI po kliknięciu w klawiature.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)
h = image.shape[0] 
w = image.shape[1] 

move_window = 10
for x in range(0, w//move_window):
    cropped = image[:, x * move_window : (x+1) * move_window]
    cv2.imshow(f"{x}", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()