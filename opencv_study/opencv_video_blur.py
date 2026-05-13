#  opencv_video_blur.py

import cv2

cap = cv2.VideoCapture("opencv_study/videos/video2.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640,480))

    blur = cv2.GaussianBlur(frame, (5,5) ,0 )

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, 50, 150)

    cv2.imshow("original",frame)
    cv2.imshow("edge",edge)

    if cv2.waitKey(33) == 27: 
        break

cap.release() # 영상 닫기
cv2.destroyAllWindows()