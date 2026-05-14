#  opencv_hsv.py


# h  -  hue(색상)  
# s  -  saturation(채도)
# v -  value(명도)
#  빨강 - 0 쯤
#  노랑 - 35쯤    # 초록 - 80쯤  #  파랑 - 130쯤
import cv2
import numpy as np

img = cv2.imread("opencv_study/images/door.png")

hsv = cv2.cvtColor( img , cv2.COLOR_BGR2HSV)

lower_red1 = np.array( [0,100,100]  )
up_red1 = np.array( [ 10, 255, 255])

lower_red2 = np.array( [170, 100,100])
up_red2 = np.array( [179,255,255] )

mask1 = cv2.inRange( hsv, lower_red1, up_red1)
mask2 = cv2.inRange( hsv, lower_red2, up_red2)

mask = mask1 + mask2

result = cv2.bitwise_and( img, img, mask=mask)

#이미지에서 빨간색 을 찾아 바운딩박스(표시하기)

contours, _ = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

box = img.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 1000: continue
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle( box, (x,y), (x+w, y+h), (0,255,0), 3)


cv2.imshow("original", img)
cv2.imshow("hsv",hsv)
cv2.imshow("result",result)
cv2.imshow("box",box)

cv2.waitKey(0)
cv2.destroyAllWindows()