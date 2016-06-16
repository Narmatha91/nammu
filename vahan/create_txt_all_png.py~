import cv2
import numpy as np 
import re
import sys,os
import glob
import os.path

save_path='book/'

def cutoff(string, pattern):
     idx = string.find(pattern)
     res=string[:idx if idx != -1 else len(string)]
     return res.split('/',100)[1]

l_png=[]
txt=[]

for f in sorted(glob.glob("book/*.png")):
	l_png.append(f)

	#print 'list of png images',len(list_png)


for f in sorted(glob.glob("book/*.txt")):
	txt.append(f)


def create_missed_txt(l_png,txt):

	res_list=[]
	remove_item=[]
	for i in range(0,len(l_png)):	
		res_list.append(cutoff(l_png[i],".png"))
	#print res_list
	filelist=[]

	#--------------------- create txt file for all png------------------------- 
	#count=0
	for i in range(0,len(res_list)):
		if any(res_list[i] in s for s in txt):
			continue
			#print 'true'
		else:
			#print res_list[i]
			name_of_file=res_list[i]
			completeName = os.path.join(save_path, name_of_file+".txt")
			file1 = open(completeName, "w")
			file1.close()
	

		"""else:					#delete png file that does not have txt
			print int(res_list[i])
			remove_item.append((int(res_list[i])-100-count))	
			count=count+1	
			os.remove('book3/'+str(res_list[i])+'.png')
			
	print remove_item
	#---------------------------------------------------
	#remove_item=[4,5,5,67,87,87]
		#sys.path.insert("book3/*.png",1)
		#os.system("rm res_list[i].png")

	with open('sort_coordinates/file_in.txt', 'r') as f:
		coordinates = [line.strip().split(' ') for line in f]
	for i in range(0,len(coordinates)):
		coordinates[i]=[int(x) for x in coordinates[i]]
	print len(coordinates)

	for i in range(0,len(remove_item)):
		coordinates.pop(remove_item[i])
	print len(coordinates)

	"""






