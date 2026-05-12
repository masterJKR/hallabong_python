#  opencv_video_bird.py

import cv2

cap = cv2.VideoCapture("opencv_study/videos/bird.mp4")

# 영상정보 
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_cnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print("w:",width ,"  h:",height," fps:",fps, 
      "총 프레임수 : " ,frame_cnt)

# 특정 시간의  영상 캡처하기( 프레임 저장 )
target_sec = 5

target_frame_num = int(fps * target_sec)

cap.set(
    cv2.CAP_PROP_POS_FRAMES, target_frame_num
)
ret , frame =cap.read()
cv2.imwrite("저장 경로와 파일명", frame)


frame_idx = 0 
while True:
    ret , frame = cap.read() # 프레임 잘읽었나?, 이미지한장
    if not ret :
        break
    
    small = cv2.resize( frame, (540, 960))
    # copy_img = small.copy()
    # copy_img[100:200 , 100:200] = [0,0,255]

    gray = cv2.cvtColor( small, cv2.COLOR_BGR2GRAY)

    if frame_idx == target_frame_num:
        cv2.imwrite("opencv_study/images/bird.png",
                    frame)

    cv2.imshow("color",small)
    cv2.imshow("bird",gray)

    #print(frame.shape)
    frame_idx += 1 # 프레임 번호
    w=cv2.waitKey(30) # 현재이미지와 다음 이미지의 출력 간격
    if  w == 27:  # esc키 코드는 27이다.
        break

cap.release()  #  영상 파일이나 카메라 닫기( 메모리 닫기 )
cv2.destroyAllWindows()