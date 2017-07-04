import os, sys
from PIL import Image
import cv2
import numpy as np

size = (64, 64)
inpath = './input/'
outpath = './val/'
repath = './re/'
white = './white.jpg'

l = os.listdir(inpath)
for infile in l:
	try:
		image = cv2.imread(inpath+infile)
		resized_image = cv2.resize(image, (64, 64))
		cv2.imwrite(repath + infile, resized_image)
	except IOError:
		print "cannot create thumbnail for '%s'" % infile
	
	inn = cv2.imread(repath+infile)
	out = cv2.imread(white)
	vis = np.concatenate((out, inn), axis=1)
	cv2.imwrite(outpath + infile, vis)
	
