import cv2
import numpy as np
def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.color_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5), 8)
    canny_edges = cv2.canny(img_gray_blur , 10 , 70)
    ret , mask = cv2.threshold(canny_edges , 70 , 255 , cv2.THRESH_BINARY_iNV)
    return mask

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    cv2.imshow('our Live sketcher', sketch(frame))
    if cv2.waitkey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()