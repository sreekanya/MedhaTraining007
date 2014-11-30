# finding id and displaying all ids of response table
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

p = re.compile("\s*\"_id\":\s*\"[a-z|A-Z|0-9]*\"")
pat = re.compile("\s*\"[a-z]+\":\s*\"[a-|A-Z|0-9]*\"")
rf = open('response.txt','r')
count = 0
temp=0
datalist={}
for i in rf:
	i=i.strip()
	match=pat.match(i)
	if (match!=None):
		#print i
		data=i.split(':')
		print data[0]
		#print data[1]
		#datalist[temp]=data[1]
		#temp=temp+1
		#print datalist		
		
			
		
		