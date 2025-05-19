# Klasyczne progowanie
# a. Wczytaj obraz z kostką brukową, przeskaluj go do szerokości 300 px i
# zastosuj progowanie klasyczne ( cv2.threshold ) dla różnych wartości
# progowania (np. 100, 140, 180).
# b. Zaobserwuj, jak zmienia się jakość segmentacji kostek. Która wartość
# progowania najlepiej rozdziela kostki od tła?


import cv2
import imutils

image = cv2.imread('kostka.png')
resized = imutils.resize(image, width=300)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(resized, 150, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('thresh', thresh)
cv2.imshow('gray', gray)
cv2.waitKey(0)