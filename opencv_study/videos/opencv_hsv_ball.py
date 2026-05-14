# opencv_hsv_ball.py

import cv2
import numpy as np

cap = cv2.VideoCapture("opencv_study/videos/ball.mp4")



while True:
    r , fr = cap.read()
    if not r: break
    fr = cv2.resize(fr, (480,640))
    hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array( [0,100,100]  )
    up_red1 = np.array( [ 10, 255, 255])

    lower_red2 = np.array( [150, 80,80])
    up_red2 = np.array( [179,255,255] )

    mask1 = cv2.inRange( hsv, lower_red1, up_red1)
    mask2 = cv2.inRange( hsv, lower_red2, up_red2)

    mask = mask1 + mask2

    kernel = np.ones( (5,5) , np.uint8)

    mask = cv2.morphologyEx( mask , cv2.MORPH_OPEN,
                            kernel, iterations=1)
    # mask = cv2.morphologyEx(
    #      mask, cv2.MORPH_CLOSE, kernel,iterations=2
    # )
    # contours, _ =cv2.findContours(
    #     mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    # )

    # fr_copy = fr.copy()
    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     if area < 200: continue

    #     x,y,w,h = cv2.boundingRect(cnt)
    #     cv2.rectangle(
    #         fr_copy , (x,y), (x+w, y+h) ,
    #         (0,255,0) , 2
    #     )
    #     cv2.putText( fr_copy, f"{w},{h}",(x,y-10),
    #                 cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    color_layer = np.zeros_like(fr)
    color_layer[:, :] = (0, 255, 0) 

    # 전체를 검정색으로 하고 빨간색 영억만 남기고 거기에 녹색을 넣는다. 
    colored_object = cv2.bitwise_and(color_layer, color_layer, mask=mask)

    background = cv2.bitwise_and(fr, fr, mask=cv2.bitwise_not(mask)) #빨간거 지우기

    result = cv2.add(background, colored_object) #녹색 붙이기

    cv2.imshow("org", fr)
    cv2.imshow("hsv",hsv)
    cv2.imshow("box",result)

    #cv2.imshow("box",fr_copy)
    if cv2.waitKey(30) == 27: break
cap.release()
cv2.destroyAllWindows()