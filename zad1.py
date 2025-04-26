# 1. Kombinacja różnych kształtów i operacji bitowych
# a. Narysuj trójkąt i porównaj go z okręgiem, wykorzystując różne operacje
# bitowe ( AND , OR , XOR , NOT ).
# b. Sprawdź, jak zmieniają się wyniki w zależności od pozycji kształtów.

import numpy as np
import cv2

# triangle
triangle = np.zeros((300, 300), dtype="uint8")
pt1 = (150, 100)
pt2 = (100, 200)
pt3 = (200, 200)
triangle_cnt = np.array([pt1, pt2, pt3])
cv2.drawContours(triangle, [triangle_cnt], 0, (255, 255, 255), -1)
cv2.imshow("image", triangle)

# circle
circle = np.zeros((300, 300), dtype = "uint8")
# cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.circle(circle, (150, 150), 100, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(triangle , circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle , circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(triangle , circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)
cv2.destroyAllWindows()