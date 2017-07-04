import os
p='/media/muthu/A4C84712C846E262/project/bag64/bag64_2/train/'
l = os.listdir(p)
j=1
for i in l:
	os.rename(p+i,p+'train'+str(j)+'.jpg')
	j+=1
