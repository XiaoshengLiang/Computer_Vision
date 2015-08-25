from PIL import Image
from scipy import *
from pylab import * 
import harris

im=array(Image.open('test.jpg').convert('L'))
harrisim=harris.compute_harris_response(im)
filtered_coords=harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im,filtered_coords)
