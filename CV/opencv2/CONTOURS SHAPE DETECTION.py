import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            abjcor = len(approx)
            x, y, w, h, =cv2.boundingRect(approx)

            if abjcor ==3: objectType= "tri"
            elif abjcor == 4:
                aspRetio=w/float(h)
                if aspRetio>0.95 and aspRetio<1.05:objectType= "square"
                else :objectType= "rectangle"
            elif abjcor > 4:objectType= "cir"
            else: objectType="NONE"


            cv2.rectangle(imgcontour, (x,y), (x+w, y+h), (0 , 255, 0), 2)
            cv2.putText(imgcontour,objectType,(x+(w//2)-10,y+(h//2)), cv2.FONT_HERSHEY_COMPLEX ,0.5, (0 , 0, 0), 2)






path = 'D:\course\AIDEPIAMIT\project\CONTOURS SHAPE DETECTION\Screenshot 2025-04-18 231845.png'
img = cv2.imread(path)

imgblack = np.zeros_like(img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgcanny = cv2.Canny(imgblur, 50, 50)
imgcontour = img.copy()
getContours(imgcanny)

imdstack = stackImages(0.8, ([img, imgGray, imgblur],
                             [imgcanny, imgcontour, imgblack]))
cv2.imshow("imdstack", imdstack)
cv2.waitKey(0)