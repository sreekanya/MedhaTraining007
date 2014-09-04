

fh=open("input.csv"''r')
for line in fh:
	print line 
#print line
data=line.split(',')
print data [0]
fh.close