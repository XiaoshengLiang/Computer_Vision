from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from scipy import ndimage

im=array(Image.open('test.jpg').convert('L'))
im1=ndimage.gaussian_filter(im,3)
figure(1)
imshow(im/im1)
axis('equal')
axis('off')
show()
