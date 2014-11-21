#! /usr/bin/python
import urllib2
import requests

#import json

url="http://medhaws.cloudapp.net:3000/wines"
datamap={}
count=0
fh=open("winelist2.csv",'r')
for i in fh:
	i=i.rstrip()
	wdata=i.split(',')
	datamap[wdata[0]]=wdata[1]
	#print datamap
	print wdata[0]
	print wdata[1]

data={wdata[0]:wdata[1]}
count=count+1
#data={"name":"Clos de Tart","Country":"North America","description":"Cognac","Year":"1947"}

r=requests.post(url,data=data)

# posting from csv file,its taking only last row of csv file