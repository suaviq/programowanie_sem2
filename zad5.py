# Zastosowanie arytmetyki do detekcji zmian w obrazach
# a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami (np.
# obiekt przesunięty).
# b. Oblicz ich różnicę ( cv2.absdiff(image1, image2) ).
# c. Zinterpretuj wynik – jakie zmiany są widoczne?

import cv2

image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
diff_image = cv2.absdiff(image1, image2)
cv2.imshow("Diff image", diff_image) # Ciemne obszary oznaczają brak różnicy – piksele mają takie same lub bardzo podobne wartości
cv2.waitKey(0)