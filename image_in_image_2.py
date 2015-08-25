#-*- coding:utf-8 -*-

from PIL import Image
from scipy import *
from pylab import *
from scipy import ndimage

import homography
import warp

im1=array(Image.open('test.jpg').convert('L')) 
im2=array(Image.open('2.JPG').convert('L')) 

tp = array([[130,200,200,130],[40,36,230,230],[1,1,1,1]])

m,n = im1.shape[:2]
fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])

# 第一个三角形
tp2 = tp[:,:3]
fp2 = fp[:,:3]

# 计算H
H = homography.Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
          (H[0,2],H[1,2]),im2.shape[:2])

# 三角形的alpha
alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])
im3 = (1-alpha)*im2 + alpha*im1_t

# 第二个三角形
tp2 = tp[:,[0,2,3]]
fp2 = fp[:,[0,2,3]]

# 计算H
H = homography.Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
          (H[0,2],H[1,2]),im2.shape[:2])

# 三角形的alpha 图像
alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])
im4 = (1-alpha)*im3 + alpha*im1_t

figure()
gray()
imshow(im4)
axis('equal')
#axis('off')
show()
