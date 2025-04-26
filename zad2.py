# Zastosowanie operacji XOR do wykrywania różnic między obrazami
# a. Wczytaj dwa podobne obrazy z drobnymi różnicami.
# b. Użyj cv2.bitwise_xor , aby uwidocznić różnice między nimi.

import numpy as np
import cv2

circle1 = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle1, (150, 150), 100, 255, -1)
cv2.imshow("Circle1", circle1)

circle2 = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle2, (150, 150), 150, 255, -1)
cv2.imshow("Circle2", circle2)

bitwiseXor = cv2.bitwise_xor(circle1 , circle2)
cv2.imshow("XOR", bitwiseXor)

cv2.waitKey(0)
cv2.destroyAllWindows()