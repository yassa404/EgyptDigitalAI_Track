import cv2
import numpy as np

print('lib is installed')

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
cv2.imshow("image", img)

# img[:] = 255, 0, 0                          # blue image
# cv2.imshow("blue image", img)

# drow  line
cv2.line(img, (0, 0), (0, 300), (255, 0, 0), 10)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.rectangle(img, (250, 350), (280, 380), (0, 0, 255), cv2.FILLED)
# circle
cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 30, (255, 200, 0), 5)
# text
cv2.putText(img, "yassa", (130, 490), cv2.FONT_HERSHEY_COMPLEX, 3, [150, 150, 150], 3)

cv2.imshow("image", img)
cv2.waitKey(0)
