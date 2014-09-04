
fh=open("doc1.csv",'r')

for i in fh:

 newi = i.rstrip()

 data=newi.split(',')

 totalmarks =int(data[1])+ int(data[2])+ int (data[3])+int(data[4])

 print "total marks of:",data[0],totalmarks

 print i
 
 fh= open("doc1.csv",'r')
 for i in fh:
 
 