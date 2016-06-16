import cv2
import numpy as np

def rotation(rgb,orientation):

	
	angle=orientation
	#rgb=cv2.imread('/home/narmatha/Documents/ocr/prog/template_rotate.jpg')
	#cv2.imshow('input',rgb)
	(h, w) = rgb.shape[:2]
	center = (w / 2, h / 2)
	M = cv2.getRotationMatrix2D(center,angle, 1.0)
	rgb = cv2.warpAffine(rgb, M, (w, h))
	cv2.imwrite('out.jpg',rgb)
	