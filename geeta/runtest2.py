import urllib2
import re
import json
import sys
from pprint import pprint 
import os
import requests

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

postlist=[]
f=open('post.csv','r')
for i in f:
	i=i.rstrip()
	postdata=i.split(',')
	postlist.append(postdata)
print postlist[0][0]
print postlist[0][1]





url= server+":"+port+path

#print baseURL

data= {"name":postlist[0][0],"merchantId":postlist[0][1]}
r = requests.post(url,data=data)


#baseURL1=baseURL+"?"+"categoryname="+postlist[0][0]+"&"+"merchant="+postlist[0][1]
#print baseURL1
#getURL = baseURL+
f = urllib2.urlopen(url)
responsedata =  f.read()




fh = open('response1.txt','w')
fh.write(responsedata)
fh.close()

print responsedata




 