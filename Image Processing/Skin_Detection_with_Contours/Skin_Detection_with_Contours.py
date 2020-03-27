#!/usr/bin/env python
# coding: utf-8

# In[ ]:

  
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

#Changing the input image to black and white image
img_gray = cv2.cvtColor(skinYCrCb, cv2.COLOR_BGR2GRAY)

#using threshold function 
ret, thresh = cv2.threshold(img_gray,20,255,0)

#obtaining contours on the image
contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#drawing contours on the image
cv2.drawContours(skinYCrCb, contours, -1, (0,255,0), 1)

#showing the output of the image with contours
cv2.imshow('Skin_7_detected.jpg', np.hstack([image,skinYCrCb]))

#saving the skin detected file in the directory
cv2.imwrite("skin_7_detected.jpg",np.hstack([image,skinYCrCb]))


