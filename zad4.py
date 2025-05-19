# Numeryzacja kostek
# a. Zmodyfikuj pętlę iterującą po konturach tak, by na każdej kostce (nad jej
# środkiem) narysować numer porządkowy ( cv2.putText ).
# b. Dodaj zapisywanie każdej wyciętej kostki do osobnego pliku kostka_01.png ,
# kostka_02.png , itd.
import cv2
import imutils
import numpy as np
import os

image = cv2.imread("kostka.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

os.makedirs("kostki", exist_ok=True)

for i, c in enumerate(cnts):
    c = (c * ratio).astype("int")
    x, y, w, h = cv2.boundingRect(c)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    segmented = cv2.bitwise_and(image, image, mask=mask)
    roi = segmented[y:y+h, x:x+w]
    center = (x + w//2, y + h//2)

    cv2.putText(image, f"{i+1}", center, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
    cv2.imwrite(f"kostki/kostka_{i+1:02}.png", roi)

cv2.imshow("Numbered", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
