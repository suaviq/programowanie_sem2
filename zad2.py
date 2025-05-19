# Eksperymentuj z metodą cv2.findContours
# a. Na progowanym obrazie znajdź kontury przy użyciu funkcji cv2.findContours.
# Narysuj wszystkie wykryte kontury na oryginalnym obrazie w kolorze
# czerwonym o grubości 2px.
# b. Zmieniaj tryby (parametr mode w funkcji findContours), przetestuj
# cv2.RETR_EXTERNAL, cv2.RETR_TREE i cv2.RETR_LIST i opisz różnice w komentarzu.

import cv2
import imutils

image = cv2.imread('kostka.png')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1] 

# RETR_EXTERNAL - zwraca tylko zewnętrzne kontury (bez hierarchii)
# RETR_TREE - zwraca wszystkie kontury z pełną hierarchią
# RETR_LIST - zwraca wszystkie kontury bez hierarchii
# w moim przypadku najlepiej dzialalo zwracanie wszystkich konturow
cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

cv2.imshow('thresh', thresh)
cv2.imshow('gray', gray)
cv2.imshow("Image with contours", image)
cv2.waitKey(0)