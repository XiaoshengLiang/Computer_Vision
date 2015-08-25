#-*- coding:utf-8 -*-
from PIL import Image
from pylab import *
from scipy import *
import warp
import homography

# 仿射扭曲im1 到im2 的例子
im1 = array(Image.open('2.JPG').convert('L'))
im2 = array(Image.open('test.jpg').convert('L'))

# 选定一些目标点
#tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
tp=array([[1,50,50,1],[55,52,281,277],[1,1,1,1]])

im3 = warp.image_in_image(im1,im2,tp)

figure()
gray()
imshow(im3)
axis('equal')
#axis('off')
show()
