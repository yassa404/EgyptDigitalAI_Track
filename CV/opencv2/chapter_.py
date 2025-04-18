import cv2
print('package imported')

## read image
img=cv2.imread("D:\course\AIDEPIAMIT\project\cv\dd4.png")
cv2.imshow("output",img)
cv2.waitKey(1000)             ## 1sec

## read videocapture
cap =cv2.VideoCapture("D:\course\AIDEPIAMIT\project\cv\dask_2_labview.mp4")
while True:
    succes, img=cap.read()
    cv2.imshow("video",img)
    key = cv2.waitKey(1) & 0xFF  #wait 1 sec on key
    if key == ord('q') or key == ord('Q'):
        break

cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,1000)
while True:
    succes, img=cap.read()
    cv2.imshow("video",img)
    key = cv2.waitKey(1) & 0xFF  #wait 1 sec on key
    if key == ord('q') or key == ord('Q'):
        break