#  opencv_video_motion.py

import cv2

cap = cv2.VideoCapture("opencv_study/videos/video3.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int( 1000/fps)

pre_frame = None  #  이전 프레임 저장용 - 비교를 위해 

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (480,640) )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #첫번째 프레임은 비교대상이 없으니까 저장만 해두기
    if pre_frame is None:
        pre_frame = gray
        continue

    # 두번째 프레임 부터 이전 프레임과 차이 구하기 
    diff = cv2.absdiff(pre_frame, gray) # 두이미지의 차이를 절대값으로반환
    
    # 두 프레임의 차이를 구해서 차이가 큰부분만 흰색으로 변경하기
    _, thresh = cv2.threshold(
        diff, 80, 255, cv2.THRESH_BINARY
    )
    # 흩어진 영역을 모아주는 과정 (흰색 영역 확장)
    thresh = cv2.dilate( thresh, None, iterations=2)

    #움직임 영역의 외곽선 
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = frame.copy()
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
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
    cv2.imshow("diff",diff)
    cv2.imshow("box",result)

    if cv2.waitKey(delay) == 27:
        break

    # 현재 프레임을 다음 프레임과 비교해야되니까 저장
    pre_frame = gray


cap.release()
cv2.destroyAllWindows()