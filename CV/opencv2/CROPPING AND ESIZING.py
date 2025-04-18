import cv2
import numpy
print('cv2 ias add')

img=cv2.imread('D:\course\AIDEPIAMIT\project\CROPPING AND ESIZING\dd4.png')
cv2.imshow("image",img)
print (img.shape)

imgResize=cv2.resize(img,(507,640))
cv2.imshow("imgResize",imgResize)
print (imgResize.shape)

imgCroped=img[0:100,100:195]
cv2.imshow("imgCroped",imgCroped)
cv2.waitKey(0)

