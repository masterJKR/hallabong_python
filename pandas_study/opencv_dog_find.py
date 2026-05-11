import cv2

def resize_ratio_width(original , tw):
    return tw , int(original[0] * tw/original[1] )

def resize_ration_height(original , th):
    return int(original[1] * th/original[0]) , th


img=cv2.imread("opencv_study/images/dog.png")

img_320 = cv2.resize( img, resize_ratio_width(img.shape[:2],320) )

gray = cv2.cvtColor( img_320, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray , 130, 255, cv2.THRESH_BINARY
)
cv2.imwrite('opencv_study/images/dog_result.png',thresh)
cv2.imshow('res',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img_320.shape)