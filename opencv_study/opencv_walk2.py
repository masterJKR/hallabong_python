#  opencv_walk2.py

import cv2
import numpy as np

cap = cv2.VideoCapture("opencv_study/videos/motion_car.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int( 1000/fps)

pre_frame = None  

# 배경 제거기 만들기 
bgdelete = cv2.createBackgroundSubtractorMOG2(
    history=300,  #  배경을 학습할 프레임 수 
    varThreshold=40,  # 얼마나 달라 져야 움직임으로 판단하나? 
    detectShadows=True  # 그림자 처리 여부 
)


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (480,640) )

    #배경 제거
    fmask = bgdelete.apply(frame, learningRate=0.005)


    _, thresh = cv2.threshold(
        fmask, 200 , 255, cv2.THRESH_BINARY 
    )

    kernel = np.ones((3,3), np.uint8)

    #모폴로지 노이즈 제거
    mask = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, 
        kernel, iterations=1 
    )

    #모폴로지 연결
    mask = cv2.morphologyEx(
        mask , cv2.MORPH_CLOSE,
        kernel, iterations=5
    )
    #영역 확장 
    mask = cv2.dilate( mask, kernel, iterations=2)
    
    contours, _ = cv2.findContours(
        mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    result = frame.copy()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        # if h < w:
        #     continue

        cv2.rectangle(
            result,
            (x,y),
            (x+w, y+h),
            (0,0,255),
            2
        )
        cv2.putText(
            result,
            "motion",
            (x,y-10) ,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, 
            (0,255,0), 2
        )
    cv2.imshow("original", frame)
    cv2.imshow("morph",mask)
    cv2.imshow("thresh",thresh)
    cv2.imshow("diff",fmask)
    cv2.imshow("box",result)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()