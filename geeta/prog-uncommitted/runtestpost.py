# posting data...runtest...

import urllib2
import re
import json
import sys
from pprint import pprint 
import os
import requests

with open('config1.json') as data_file:
 	data = json.load(data_file)
print data
server=data[0]["server"]
path=data[0]["path"]
port=data[0]["port"]

print "server :",server
print "path :", path
print "port : ",port

postlist=[]
fh=open('post.csv','r')
for i in fh:
	i=i.rstrip()
	postdata=i.split(',')
	print postdata
	postlist.append(postdata)
print postlist[0][0]
print postlist[0][1]

baseURL = server+":"+port+path

print baseURL
baseURL1=baseURL+"?"+"categoryname="+postlist[0][0]+"&"+"merchant="+postlist[0][1]
print baseURL1
f1=requests.post(baseURL1)
f = urllib2.urlopen(f1)
resdata =  f.read()
print resdata
