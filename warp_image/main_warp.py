import cv2
import numpy as np
import sys,os
import statistics # for finding median
import math   #for arctan
from rotate import rotation  

rgb=cv2.imread(sys.argv[1],0)
image=rgb.copy()
cv2.imwrite("rgb.jpg",rgb)
os.system('ocropus-nlbin rgb.jpg -n')
rgb=cv2.imread('rgb.bin.png')
width=rgb.shape[0]
height=rgb.shape[1]/2
#print width,height
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
morphKernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, morphKernel)
#bw=small
bw=cv2.adaptiveThreshold(grad,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,7)
morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(sys.argv[2]), 1))
connected=cv2.morphologyEx(bw,cv2.MORPH_CLOSE, morphKernel)
mask=np.zeros(bw.shape,dtype=np.uint8)
_,contours, hierarchy = cv2.findContours(connected,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
idx=0	
thresh=[]

tot_box=[]

for cnt in contours:
	#print cnt
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	tot_box.append(box.tolist()) 
	cv2.drawContours(rgb,[box],0,(255,0,0),2)

list_slope=[]
j=0
for i in range(0,len(tot_box)):
	if abs(tot_box[i][j][0]-tot_box[i][j+1][0]) > abs(tot_box[i][j+1][0]-tot_box[i][j+2][0]):
			x1=tot_box[i][j][0]
			x2=tot_box[i][j+1][0]
			y1=tot_box[i][j][1]
			y2=tot_box[i][j+1][1]
	else:
			x1=tot_box[i][j][0]
			x2=tot_box[i][j+3][0]
			y1=tot_box[i][j][1]
			y2=tot_box[i][j+3][1]
	#print x1,x2,y1,y2
	#cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
	
	if abs(x2-x1)>0:
		slope=float(y2-y1)/(x2-x1)
	else:
		slope=0

	list_slope.append(slope)

	
sort_slope=sorted(list_slope)
median_slope=statistics.median(sort_slope)
orientation= math.degrees(math.atan(median_slope))
print orientation
rotation(image,orientation)
#cv2.imwrite("rect.jpg",image)

