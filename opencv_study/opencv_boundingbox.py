#  opencv_boundingbox.py


import cv2

img = cv2.imread("opencv_study/images/coin.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur( gray , (5,5) ,0 )

_, thresh = cv2.threshold(
    blur , 131, 255, cv2.THRESH_BINARY_INV
)

contours , hier = cv2.findContours(
    thresh , 
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 2500: continue

    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(
        result,
        (x,y),
        (x+w , y+h),
        (0,0,255), 2
    )

cv2.imshow("box",result)
cv2.waitKey(0)
cv2.destroyAllWindows()