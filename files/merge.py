import cv2
import numpy as np
import os

p1='/media/muthu/A4C84712C846E262/project/bag64/bag64_1/train/'
l = os.listdir(p1)
l1=[]
for i in l:
	l1.append(p1+i)
p2='/media/muthu/A4C84712C846E262/project/bag64/bag64_2/train/'
p3='/media/muthu/A4C84712C846E262/project/bag64/bag64_AB/train/'
l = os.listdir(p2)
l2=[]
for i in l:
	l2.append(p2+i)

for i,j,k in zip(l1,l2,range(1,len(l1)+1)):
	inn = cv2.imread(i)
	out = cv2.imread(j)
	vis = np.concatenate((out, inn), axis=1)
	cv2.imwrite(p3 + str(k)+'.jpg', vis)
