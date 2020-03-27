  # Required modules
import cv2
import numpy as np

#Setting ranges for skin color
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

#taking input of the given image
image = cv2.imread("skin_7.jpeg")

#changing BGR to YCrCb
imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)

#masking the given image accordingly
skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

#BITWISE_AND of input image and the masked image
skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)

#output of the skin detected image
cv2.imshow("skin_7.jpg",np.hstack([image,skinYCrCb]))

#saving the skin detected file in the directory
cv2.imwrite("skin_7_detection.jpg",np.hstack([image,skinYCrCb]))


