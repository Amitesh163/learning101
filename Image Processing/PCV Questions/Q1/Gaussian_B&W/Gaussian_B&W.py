#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#applying gaussian filter
im = array(Image.open('image.jpg').convert('L'))
im2 = filters.gaussian_filter(im,20)

#getting image from image array
U = Image.fromarray(uint8(im2))

#saving the image
U.save('gaussian(sigma=20).jpg')




