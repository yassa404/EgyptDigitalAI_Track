import cv2
import numpy as np

def empty(a):
    pass

path = "D:\course\AIDEPIAMIT\project\DETECTION_COLOR\Screenshot 2025-04-18 192036.png"
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 43, 179, empty)
cv2.createTrackbar("saturation Min", "Trackbar", 39, 255, empty)
cv2.createTrackbar("saturation Max", "Trackbar", 250, 255, empty)
cv2.createTrackbar("value Min", "Trackbar", 111, 255, empty)
cv2.createTrackbar("value Max", "Trackbar", 255, 255, empty)


while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("saturation Min", "Trackbar")
    s_max = cv2.getTrackbarPos("saturation Max", "Trackbar")
    v_min = cv2.getTrackbarPos("value Min", "Trackbar")
    v_max = cv2.getTrackbarPos("value Max", "Trackbar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    higher = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, higher)
    imgresult = cv2.bitwise_and(img, img, mask=mask)

    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    combined = cv2.hconcat([img, mask_bgr, imgresult])
    cv2.imshow("Combined View", combined)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc key to break
        break

    #cv2.imshow("image", img)
    #cv2.imshow("imgHSV", imgHSV)
    #cv2.imshow("MaskImage", mask)

    cv2.waitKey(10)
