import cv2
import numpy as np

print('lib is installed')
img = cv2.imread('D:\course\AIDEPIAMIT\project\WARP RESPECTIVE\Q1_resized.jpg')
print(img.shape)

width, height = 683, 512
pts1 = np.float32([[305, 116], [205, 334], [399, 398], [487, 170]])
pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutPut = cv2.warpPerspective(img, matrix, (width, height))
print(imgOutPut.shape)

for i, point in enumerate(pts1):
    x, y = int(point[0]), int(point[1])
    cv2.circle(img, (x, y), 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(i+1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

for i, point in enumerate(pts2):
    x, y = int(point[0]), int(point[1])
    cv2.circle(img, (x, y), 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(i+1), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.imshow("imageOutPut", imgOutPut)

cv2.waitKey(0)
cv2.destroyAllWindows()

