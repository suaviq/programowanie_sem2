# Pomiar wymiarów kostek
# a. Dla każdej wykrytej kostki:
# i. Oblicz jej szerokość i wysokość w pikselach.
# ii. Na oryginalnym obrazie narysuj prostokąt oraz opisz go wymiarami,
# np. „40x40 px”.

import cv2
import imutils
import numpy as np

image = cv2.imread("kostka.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    c = (c * ratio).astype("int")
    x, y, w, h = cv2.boundingRect(c)

    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
    label = f"{w}x{h}px"
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

cv2.imshow("Dimensions", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
