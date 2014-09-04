fh=open("file2.csv",'r')

for i in fh:

	newi = i.rstrip()

	data=newi.split(',')

	totalmarks =int(data[1])+ int(data[2])

print "total marks of:",data[0],totalmarks

print i

print data[0]

