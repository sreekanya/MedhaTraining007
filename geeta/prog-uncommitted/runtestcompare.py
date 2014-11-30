import urllib2
import re
import json
import sys
from pprint import pprint 
import os

# open config.json and read it and save it in list


with open('config.json') as data_file:
 	data = json.load(data_file)
print data
server=data[0]["server"]
path=data[0]["path"]
port=data[0]["port"]

print "server :",server
print "path :", path
print "port : ",port

with open('ExpectedDataFormat.json') as data1_file:
 	data1 = json.load(data1_file)
print data1
_id=data1[0]["_id"]
category=data1[0]["category"]
merchant=data1[0]["merchantId"]
print _id
print category
print merchant

# getting size of get.csv file





getlist=[]
fh=open('get.csv','r')
for i in fh:
	i=i.rstrip()
	getdata=i.split(',')
	#print getdata
	getlist.append(getdata)
#print getlist[0][0]
o=len(getlist)
print "len trial size", o
filename="get.csv"
s= os.stat(filename).st_size
print s

def getSize():
	count = 0 
 	for i in data:
  		count = count+1
	return count
	print "size of the file",count

baseURL = server+":"+port+path

print baseURL
#baseURL1=baseURL+"?"+"categoryname="+getlist[0][0]+"&"+"merchant="+getlist[0][1]
#print baseURL1
#getURL = baseURL+

baseURL1=baseURL+"?"+"categoryname="+getlist[i][0]+"&"+"merchant="+getlist[i][1]
print baseURL1


f = urllib2.urlopen(baseURL1)
responsedata =  f.read()




fh = open('response1.json','w')
fh.write(responsedata)
fh.close()

print responsedata
res_list=[]
with open ('response1.json') as datafile:
	res_data=json.load(datafile)
	print res_data[0]

	for key in res_data[0]:
		print key 

	k=res_data[0].keys()
	print "response key list",k





# first getting only keys from json str


with open('ExpectedDataFormat.json') as data_file:
 	data = json.load(data_file)

 	print data[0]
 	for key in data[0]:
 		print key
 	y=data[0].keys()

 	print list(data[0].keys())

 	print "expected data key list",y

# both lines above give same result
for key in res_data[0]:
 	if key in data[0]:
 		print "matched"
 	else:
 		print "no match"


# now have to match keys in 2 json structures 





 