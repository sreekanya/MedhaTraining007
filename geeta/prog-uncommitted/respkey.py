# keys from list of list(dict)
import json


import urllib2
import re
import json
import sys
from pprint import pprint 
import os

# open config.json and read it and save it in list


with open('config1.json') as data_file:
 	data = json.load(data_file)
print data
server=data[0]["server"]
path=data[0]["path"]
port=data[0]["port"]

print "server :",server
print "path :", path
print "port : ",port
baseURL = server+":"+port+path


klist=[]
listoflist=[]
#fh=open('keylistsub.json','r')
#for i in fh:
#	i=i.strip()
#	i=i.split('][')
#	k=[i][0]
#	print k[0]


getlist=[]
		
fh=open('get.csv','r')
for i in fh:
	i=i.rstrip()
	getdata=i.split(',')
	print getdata
	getlist.append(getdata)
	print "parameter list : ",len(getlist)
		
for i in range(0,len(getlist)):
	baseURL1=baseURL+"?"+"categoryname="+getlist[i][0]+"&"+"merchant="+getlist[i][1]
	print baseURL1
	f = urllib2.urlopen(baseURL1)
	responsedata = f.read()
	print "Response  ",responsedata
			
			
	fh = open('ResponseDataFile.json','a')
	fh.write(responsedata)
	fh.close()



	
	
# this gives list having dicts

# trying to extract 2 dict and print their keys,from keylistsub....response of one request
	
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