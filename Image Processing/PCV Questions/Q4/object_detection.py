#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#taking input of the image and converting to grayscale
im = array(Image.open('image_1.jpg').convert('L'))

def Object_detection(im, blur_am): 

    #applying gaussian filter
    im2 = filters.gaussian_filter(im,blur_am)

    #finding out x-derivative
    imx = zeros(im2.shape)
    filters.sobel(im,1,imx)

    #finding out y-derivative
    imy = zeros(im.shape)
    filters.sobel(im,0,imy)

    #find out the resultant image
    magnitude = sqrt(imx**2+imy**2)

    return magnitude

#calling the function
x = Object_detection(im, 5)

#getting image from image array
U = Image.fromarray(uint8(x))

#saving the image
U.save('object_1_detected.jpg')
