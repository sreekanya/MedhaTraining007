# keys from list of list(dict)
import json

klist=[]
listoflist=[]
#fh=open('keylistsub.json','r')
#for i in fh:
#	i=i.strip()
#	i=i.split('][')
#	k=[i][0]
#	print k[0]
	
	
# this gives list having dicts

# trying to extract 2 dict and print their keys
	
with open('keylistsub.json') as data1_file:
 	data1 = json.load(data1_file)
print data1[0].keys()
for i in data1[0]:
	print i
print"trying second set", data1[1]
print data1[1].keys()
for i in data1[1]:
	print i

# this gives keys of both dict