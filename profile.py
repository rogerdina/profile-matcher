import cv2
import numpy as np

img1 = cv2.imread("./media/img/face.png");
img2 = cv2.imread("./media/img/faceass.png");

weight1 = 0.5
weight2 = 0.5
gamma_weight = 0

dst = cv2.addWeighted(img1, weight1, img2, weight2, gamma_weight)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
