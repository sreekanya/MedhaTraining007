import urllib2
import json
import re
baseURL = "http://medhaws.cloudapp.net:3000"
getURL = baseURL+'/wines'

f = urllib2.urlopen(getURL)
responsedata =  f.read()

fh = open('response.txt','w')
fh.write(responsedata)
fh.close()

rf=open('response.txt','r')
datawine={}

for i in rf:
	i=i.strip()
	#print i
	
	data=i.split(': ')

	datawine=i

	data

	print i

	#print data[0]
	print data[0]


	#print data[1]


