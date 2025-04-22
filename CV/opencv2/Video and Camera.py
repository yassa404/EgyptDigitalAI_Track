import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 1000)
while True:
    # resize the frame
    succes, frame = cap.read()
    frameresiaze = cv2.resize(frame, (533, 300))

    # horizontal flip
    frameresiaze = cv2.flip(frameresiaze, 1)

    # gray
    frameresiaze = cv2.cvtColor(frameresiaze, cv2.COLOR_BGRA2GRAY)

    cv2.imshow("video", frameresiaze)
    key = cv2.waitKey(1) & 0xFF  # wait 1 sec on key
    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()

print('orignal frame size = ', frame.shape)
print("resized frame = ", frameresiaze.shape)
