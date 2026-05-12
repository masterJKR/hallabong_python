#  opencv_cars.py

import cv2

img = cv2.imread("opencv_study/images/cars.png")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur( gray , (5,5), 0) 

_,thresh = cv2.threshold(
    blur, 120,255, cv2.THRESH_BINARY_INV
)
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()
count = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 200:
        count += 1

print("차량 수 :", count)
cv2.imshow("thresh" ,thresh )
cv2.waitKey(0)
cv2.destroyAllWindows()