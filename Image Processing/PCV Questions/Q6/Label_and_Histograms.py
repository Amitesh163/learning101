#import required modules
from PIL import Image
from pylab import *
from scipy.ndimage import measurements,morphology

# load image and threshold to make sure it is binary
im = array(Image.open('image_1.jpg').convert('L'))

#binary thresholding
im = 1*(im<128)

#obtaining the image after using label() option
labels, nbr_objects = measurements.label(im)

#figure for showing labelled image
figure()
imshow(labels)
show()

#figure showing the histogram
figure()
hist(labels.flatten(),128)
show()

