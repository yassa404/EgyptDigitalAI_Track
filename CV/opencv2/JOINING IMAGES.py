import cv2
import numpy as np

print("done")

img = cv2.imread('D:\course\AIDEPIAMIT\project\JOINING IHAGES\dd4.png')

imghor = np.hstack((img, img))
imgver = np.vstack((img, img))

cv2.imshow("horzintal image", imghor)
cv2.imshow("vertical image", imgver)

cv2.waitKey(0)
