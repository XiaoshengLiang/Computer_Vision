from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im=array(Image.open('test.jpg').convert('L'))
im1=ndimage.gaussian_filter(im,3)

plt.figure(figsize=(9,6))

plt.subplot(221)
plt.imshow(im1,cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(222)
plt.imshow(im-im1,cmap=plt.cm.gray)
plt.axis('off')

im2=array(Image.open('test.jpg'))
im3=ndimage.gaussian_filter(im,3)

plt.subplot(223)
plt.imshow(im3)
plt.axis('off')


plt.subplot(224)
plt.imshow(im-im3)
plt.axis('off')

show()
