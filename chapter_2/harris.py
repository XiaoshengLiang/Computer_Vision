from PIL import Image
from scipy import *
from pylab import *
from scipy.ndimage import filters


def compute_harris_response(im,sigma=300):
	imx=zeros(im.shape)
	filters.gaussian_filter(im,(sigma,sigma),(0,1),imx)
	imy=zeros(im.shape)
	filters.gaussian_filter(im,(sigma,sigma),(1,0),imy)

	Wxx=filters.gaussian_filter(imx*imx,sigma)
	Wxy=filters.gaussian_filter(imx*imy,sigma)
	Wyy=filters.gaussian_filter(imy*imy,sigma)

	Wdet = Wxx*Wyy - Wxy**2
	Wtr = Wxx + Wyy

	return Wdet / Wtr



def get_harris_points(harrisim,max_dist=10000,threshold=0.1):
	corner_threshold=harrisim.max()*threshold
	harrisim_t=(harrisim>corner_threshold)*1

	coords=array(harrisim_t.nonzero()).T
	candidate_values=[harrisim[c[0],c[1]] for c in coords ]

	index=argsort(candidate_values)

	allowed_locations=zeros(harrisim.shape)
	allowed_locations[max_dist:-max_dist,max_dist:-max_dist]=1

	filtered_coords=[]
	for i in index:
		if allowed_locations[coords[i,0],coords[i,1]]==1:
			filtered_coords.append(coords[i])
			allowed_locations[(max_dist-coords[i,0]):(coords[i,0]+max_dist),(max_dist-coords[i,1]):(coords[i,1]+max_dist)]=0
	return filtered_coords



def plot_harris_points(image,filtered_coords):
	figure()
	gray()
	imshow(image)
	plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],'*')
	axis('off')
	show()
