import os, sys
import Image

size = 128, 128
p='./datasets/pokemon/val2/'
p2='./datasets/pokemon/val/'
l=os.listdir(p)
for infile in l:
    print infile
    outfile = os.path.splitext(infile)[0] + "c.jpg"
    print(outfile) 
    if infile != outfile:
        try:
            im = Image.open(p+infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(p2+outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile

'''
for i in f:
s='python tes.py '+i
os.system(s)
 
'''
