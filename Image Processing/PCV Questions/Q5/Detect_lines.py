# Python program to illustrate HoughLine
# method for line detection 
#import required modules
import cv2
import numpy as np

# Reading the required image in 
# which operations are to be done.
img = cv2.imread('image_1.jpg')

# Convert the img to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply edge detection method on the image
edges = cv2.Canny(gray,100,200,apertureSize = 3)

#setting the values
minLineLength = 1
maxLineGap = 1

# This returns an array of r and theta values
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)

# The below for loop runs till r and theta values 
# are in the range of the 2d array 
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
            # (0,0,255) denotes the colour of the line to be 
            #drawn. In this case, it is red.

# All the changes made in the input image are finally 
# written on a new image houghlines.jpg 
cv2.imshow('houghlines',img)

#saving the image with lines
cv2.imwrite('houghlines_1.jpg',img)
cv2.waitKey(0)




