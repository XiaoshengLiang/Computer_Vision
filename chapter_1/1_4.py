from PIL import Image
from scipy import *
from pylab import *
from scipy.ndimage import filters

im=array(Image.open('test.jpg').convert('L'))

sigma=2

imx=zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(0,1),imx)

imy=zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(1,0),imy)

magnitude=sqrt(imx**2+imy**2)

figure(1)
imshow(magnitude,cmap=cm.gray)
axis('off')
axis('equal')

show()
