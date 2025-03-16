# Dynamiczne przesunięcie na podstawie parametrów użytkownika
# a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
# poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
# b. Sprawdź, jak działa przesunięcie dla różnych wartości.
import numpy as np
import cv2
import imutils

image = cv2.imread("image.jpg")
# cv2.imshow("Original", image)
width = image.shape[1]
height = image.shape[0]
print(f"Wielkosc obrazka: {width}, {height}")

x = 0
y = 0

try:
    x = int(input('Wybierz przesuniecie na osi X (prawo - dodatnie, lewo - ujemne wartosci): '))
    y = int(input('Wybierz przesuniecie na osi Y (dol - dodatnie, gora - ujemne wartosci): '))
except ValueError:
    print('Napisz liczbe!!!!( ｡ •̀ ⤙ •́ ｡ )')
    exit(1)

shifted = imutils.translate(image, x, y)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)