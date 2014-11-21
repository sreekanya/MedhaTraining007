import urllib2
import requests
import json
import re

geturl="http://medhaws.cloudapp.net:3000/wines"
f=urllib2.urlopen(geturl)
responsedata=f.read()

fh=('response.txt','w')
fh.write(responsedata)
fh.close()
datalist={}
rf=open('response.txt','r')

for i in rf:
	i=i.strip()
	print data[0]
# getting data from get method





