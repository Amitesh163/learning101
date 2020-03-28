#required modules
from PIL import Image
from numpy import *
from scipy.ndimage import filters

#accessing the image
im = array(Image.open('image.jpg'))
im2 = zeros(im.shape)

#applying Gaussian blurring to each colour
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],1)

#sharpened = original + (original - blurred) x amount
sharpened = (im - im2)*1 + im

#obtaining image from the image array
im2 = Image.fromarray(uint8(sharpened))

#saving the image
im2.save('Unsharp_masking_Coloured_1.jpg')
