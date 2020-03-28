#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#obatining the input image
x = array(Image.open('image.jpg'))

#converting image to grayscale
im = mean(x, -1)

#applying gaussian filter
im2 = filters.gaussian_filter(im,5)

#sharpened = original + (original − blurred) × amount
sharpened =(im - im2)*2+im

#getting image from image array
U = Image.fromarray(uint8(sharpened))

#saving the image
U.save('unsharp_masking_2.jpg')
