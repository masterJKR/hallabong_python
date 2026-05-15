#  opencv_ROI_car.py

import cv2 

cap = cv2.VideoCapture("opencv_study/videos/motion_car.mp4")

paused = False  # 영상 일시 정지용
roi_point = [] # 좌표 저장용
current_frame = None
display = None
sel_roi=None

def mouse_pos(event, x, y, flag, param):
    global roi_point , current_frame, display, sel_roi

    if event == cv2.EVENT_LBUTTONDOWN:
        roi_point.append( (x,y) ) # 마우스 클릭 좌표 저장
        cv2.circle( display , (x,y) , 5, (0,255,150), -1)

        if len(roi_point) == 2: #좌표 두번 클릭했다면
            x1,y1 = roi_point[0]
            x2,y2 = roi_point[1]

            start_x = min(x1,x2)
            end_x = max(x1,x2)
            start_y = min(y1,y2)
            end_y = max(y1,y2)
            
            sel_roi = (start_x, start_y, end_x, end_y)

            cv2.rectangle( display, (start_x,start_y), 
                          (end_x,end_y), (255,0,0) ,2 )
            roi = current_frame[ start_y:end_y , start_x:end_x ]
            cv2.imshow("roi",roi)


cv2.namedWindow("org")
cv2.setMouseCallback( "org" , mouse_pos )

while True:
    if not paused:  # 일시 정지가 아니면 다음 프레임 읽기
        r, frame = cap.read()
        if not r : break
        frame = cv2.resize(frame, (480 ,640))

        current_frame = frame.copy()
        display = frame.copy()
        if sel_roi is not None:
            x1,y1,x2,y2 = sel_roi
            roi = current_frame[y1:y2, x1:x2]
            cv2.imshow("ROI",roi)

    cv2.imshow("org", display)
    k = cv2.waitKey(30)
    if k == 27: break
    elif k == 32:  #  스페이스바 키 값은 32 - 일시정지용으로 사용할꺼 
        paused = not paused
    elif k == ord('r'):
        roi_point= []
        if current_frame is not None:
            display = current_frame.copy()
        

cap.release()
cv2.destroyAllWindows()