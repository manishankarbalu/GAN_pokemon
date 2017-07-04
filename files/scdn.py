import os, sys
import Image

size = 128, 128

p='/home/shankar/Desktop/facades/train'
p2='/home/shankar/Desktop/scimg/'
i=0
j=0
k=0
l=0
f=os.listdir(p)
for infile in f:
	print infile
	outfile = os.path.splitext(infile)[0] + "c.jpg"
	print outfile
	if infile != outfile:
		k+=1
		try:
			im = Image.open(infile)
			l+=1
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(p2+outfile, "JPEG")
			i+=1
			Image.close(im)
		except IOError:
			#print "cannot create thumbnail for '%s'" % infile
			j+=1
		
print i,j,k,l
