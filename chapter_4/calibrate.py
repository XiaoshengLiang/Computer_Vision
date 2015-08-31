import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS,100,0.0001)

objpoint=np.zeros((9*5,3),np.float32)
objpoint[:,:2]=np.mgrid[0:9,0:5].T.reshape(-1,2)

objpoints=[]
imgpoints=[]

images=glob.glob('*.JPG')
for frame in images:
	img=cv2.imread(frame)
	imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,corners=cv2.findChessboardCorners(imgGray,(9,5),None)

	if ret==True:
		objpoints.append(objpoint)
		cv2.cornerSubPix(imgGray,corners,(11,11),(-1,-1),criteria)
		imgpoints.append(corners)

	cv2.drawChessboardCorners(img,(9,5),corners,ret)
	cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
	cv2.imshow('Image',img)
	cv2.waitKey(0)

print 'camera matrix'    
ret, camMat, distortCoffs, rotVects, transVects = cv2.calibrateCamera(objpoints, imgpoints, imgGray.shape[::-1],None,None)  
print camMat

cv2.destroyAllWindows()
