#  opencv_study3.py

# 엣지 디텍션, 콘투어 , 바운딩박스 
# 엣지 -  이미지에서 색이나 밝기가 갑자기 변경되는 경계선 

#edge detection 사용되는곳 -  차선 인식, 문서 스캔, 얼굴인식
#                       로봇의 눈역할,  공장 검사( 부품균열,  흠집 )

import cv2

#lane.png
# 차선 찾기
img = cv2.imread("opencv_study/images/lane.png")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

#  Canny(이미지값 , 낮은기준값 , 높은 기준값)
#  기준값을  낮추면  edge가 많이 나오고  높이면 진한 edge만 나온다.
edge1 = cv2.Canny(blur , 50, 150)
edge2 = cv2.Canny(blur , 100, 200)

cv2.imshow("lane",gray)
cv2.imshow("edge1",edge1)
cv2.imshow("edge2",edge2)

cv2.waitKey(0)
cv2.destroyAllWindows()