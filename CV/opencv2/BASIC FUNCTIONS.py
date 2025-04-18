import cv2
print ("cv2 is imported")

img=cv2.imread("D:\course\AIDEPIAMIT\project\pythonProject\dd4.png")

## convert to gray
imgGray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
cv2.imshow("GRAY IMAGE",imgGray)


# make it Blur
imgBlur=cv2.GaussianBlur(imgGray,(11,11),0)
cv2.imshow("BlurGray IMAGE",imgBlur)
imgBlur=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("Blur IMAGE",imgBlur)


imgCanny=cv2.Canny(img,255,240)
cv2.imshow("Canny IMAGE",imgCanny)
cv2.waitKey(0)


