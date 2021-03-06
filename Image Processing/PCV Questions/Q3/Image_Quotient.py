#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#accessing the image
im = array(Image.open('image_1.jpeg'))
im2 = zeros(im.shape)

#applying Gaussian blurring to each colour
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)

#dividing the input image by the blurred image
im2 = clip(128 * (1.0 *im / (im2 + 0.0001)), 0, 255)

#conversion to uint8 form
im2 = uint8(im2)

#obtaining image from the image array
im2 = Image.fromarray(uint8(im2))

#saving the image
im2.save('Image_Quotient_1.jpg')
