import cv2
import numpy as np
import sys,os
import glob
from create_txt_all_png import create_missed_txt
#from main_vahan_test import string_match


rgb=cv2.imread(sys.argv[1])
rgb=cv2.resize(rgb,(1500,2500), interpolation = cv2.INTER_CUBIC)
cv2.imwrite("out/input.jpg",rgb)
os.system('ocropus-nlbin out/input.jpg -n')
rgb=cv2.imread('out/input.bin.png')
#(h, w) = rgb1.shape[:2]
#center = (w / 2, h / 2)
#M = cv2.getRotationMatrix2D(center, -90, 1.0)
#rgb = cv2.warpAffine(rgb1, M, (w, h))
image=rgb.copy()

large=rgb.copy()
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
morphKernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, morphKernel)
cv2.imwrite("out/morph_ellipse.jpg",grad)


bw=cv2.adaptiveThreshold(grad,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,7)

morphKernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (int(sys.argv[2]), 1))
connected1=cv2.morphologyEx(bw,cv2.MORPH_CLOSE, morphKernel2)
kernel = np.ones((5,5),np.uint8)
connected = cv2.dilate(connected1,kernel,iterations = 1) # dilation output
#cv2.namedWindow("bw",cv2.WINDOW_NORMAL)
#cv2.imshow("bw",connected)


mask=np.zeros(bw.shape,dtype=np.uint8)
_,contours, hierarchy = cv2.findContours(connected,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
idx=0
k=1000
print len(contours)
file_open=open("out/file_in.txt",'w')
#idx=0
for idx in range(len(contours)):
	x,y,w,h=cv2.boundingRect(contours[idx])
	#maskROI=mask[y:y+h,x:x+w]
	#maskROI[:]=0
	cv2.drawContours(mask,contours,idx,(255,255,255),-1)
	r=np.count_nonzero(mask[y:y+h,x:x+w])/(w*h*1.0)
	
	if r>0.45 and w>30 and h>20:
		if h<w and h<50:
			cv2.rectangle(large,(x,y),(x+w,y+h),(0,255,0),2)
			ROI_rect=image[y:y+h,x:x+w]
			file_open.write(str(x)+" "+str(y)+" "+ str(w)+" "+str(h)+"\n")
			#file_open.write(str(x)+" "+str(y)+" "+ str(w)+" "+str(h))
			#print 'x and y coordinates',x,y,x+w,y+h
			cv2.imwrite('book/'+str(k)+'.png', ROI_rect)
			k=k+1

				
		elif h<w and h>50:
			cv2.rectangle(large,(x,y),(x+w,y+(h/2)-2),(255,0,0),2)
			ROI_rect=image[y:y+(h/2)-2,x:x+w]
			#ROI_rect=image[y:y+h,x:x+w]
			cv2.imwrite('book/'+str(k)+'.png', ROI_rect)
			k=k+1
			file_open.write(str(x)+" "+str(y)+" "+ str(w)+" "+str(h/2-2)+"\n")
			cv2.rectangle(large,(x,y+(h/2)+2),(x+w,y+h),(0,0,255),2)
			ROI_rect1=image[y+(h/2)+2:y+h,x:x+w]
			cv2.imwrite('book/'+str(k)+'.png', ROI_rect1)
			k=k+1
			file_open.write(str(x)+" "+str(y+(h/2)+2)+" "+ str(w)+" "+str(h)+"\n")


model='/home/narmatha/Documents/ocr/vahan_proj/datasetsamplenarmatha/b5b6/final_vahan-00114000.pyrnn.gz'
os.system('ocropus-rpred -m '+model+' book/*.png')
list_png=[]
for f in sorted(glob.glob("book/*.png")):
	list_png.append(f)
#print list_png[1]
#print 'list of png images',len(list_png)
txt_file=[]
for f in sorted(glob.glob("book/*.txt")):
	txt_file.append(f)
 
create_missed_txt(list_png,txt_file)

#os.system('ocropus-rpred -m vahan.pyrnn.gz-00027000.pyrnn.gz book5/*.png')
#cv2.namedWindow('output',cv2.WINDOW_NORMAL)
cv2.imwrite('out/data.jpg',large)
cv2.imwrite('out/image.jpg',image)
'''#------------------------------------------------------call string match----------------------
s1=[]
s1=['no','name','financers','chassis no','engine no','marker model','company','manufacturer','validity','body type']
#s1=str(raw_input('Enter the string : '))
#string_match(s1)

#for i in range(0,len(s1)):
#	string_match(s1[i])
'''

