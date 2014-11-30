# trying to do hash table...using postman....json...
import urllib2
import json
import re
baseURL = "http://medhaws.cloudapp.net:3000"
getURL = baseURL+'/wines'
fh = open('response.txt','w')
responsedata =  f.read()
fh.write(responsedata)
fh.close()
#f = urllib2.urlopen(getURL)

rf=open('response.txt','r')
datalist={}
temp=0
for i in rf:
	i=i.rstrip()
pat = re.compile("\s*\"_id\":\s*\"[a-z|A-Z|0-9]*\"")
re=pat.match(i)
if (re!=None):
	print re
else:
	print "failed"

