#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#applying gaussian filter
im = array(Image.open('image_6.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)

#finding out x-derivative
imx = zeros(im2.shape)
filters.sobel(im,1,imx)

#finding out y-derivative
imy = zeros(im.shape)
filters.sobel(im,0,imy)

#find out the resultant image
magnitude = sqrt(imx**2+imy**2)

#getting image from image array
U = Image.fromarray(uint8(magnitude))

#saving the image
U.save('object_6_detected.jpg')
