# Dynamiczny wybór ROI
# a. Napisz skrypt, który pozwala użytkownikowi podać wartości startX , endX ,
# startY , endY z klawiatury.
# b. Przytnij obraz zgodnie z wprowadzonymi wartościami i wyświetl wynik.

import cv2

image = cv2.imread("images.jpg")
cv2.imshow("Original", image)

startX = 0
startY = 0
endX = 0
endY = 0

try:
    print('roi = image[startY:endY, startX:endX]')
    startY = int(input('Start Y: '))
    endY = int(input('End Y: '))
    startX = int(input('Start X: '))
    endX = int(input('End X: '))
except ValueError:
    print('Napisz liczbe!!!!( ｡ •̀ ⤙ •́ ｡ )')
    exit(1)

cropped = image[startY:endY, startX:endX]
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)