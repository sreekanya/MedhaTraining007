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
getlist=[]
fh=open('get.csv','r')
for i in fh:
 i=i.rstrip()
 getdata=i.split(',')
 print getdata
 getlist.append(getdata)
print getlist[0][0]

baseURL = server+":"+port+path

print baseURL
baseURL1=baseURL+"?"+"categoryname="+getlist[0][0]+"&"+"merchant="+getlist[0][1]
print baseURL1
#getURL = baseURL+
f = urllib2.urlopen(baseURL1)
responsedata =  f.read()




fh = open('response1.txt','w')
fh.write(responsedata)
fh.close()

print responsedata