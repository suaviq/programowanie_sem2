# Eksperymentuj z rozdzielczością obrazu
# a. Zmieniaj rozmiar obrazu wejściowego przed detekcją konturów. Sprawdź,
# jak zmiana rozdzielczości wpływa na liczbę i jakość wykrytych konturów.
# b. Czy zmniejszenie obrazu może poprawić detekcję?

import cv2
import imutils

def detect_and_draw_contours(image_path, widths):
    image = cv2.imread(image_path)
    
    for width in widths:
        resized = imutils.resize(image, width=width)
        ratio = image.shape[0] / float(resized.shape[0])

        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1] 

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        print(f"Width: {width}px, Liczba konturów: {len(cnts)}")

        output = image.copy()        
        for c in cnts:
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            cv2.drawContours(output, [c], -1, (0, 0, 255), 2)

        cv2.imshow(f"Width {width}px (contours: {len(cnts)})", output)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'kostka.png'
widths_to_test = [100, 200, 300, 400, 500]
detect_and_draw_contours(image_path, widths_to_test)