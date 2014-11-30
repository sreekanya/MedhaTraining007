# trying to do hash table...using postman....json...
import urllib2
import json
import re
baseURL = "http://medhaws.cloudapp.net:3000"
getURL = baseURL+'/wines'

f = urllib2.urlopen(getURL)
responsedata =  f.read()
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



fh = open('response.txt','w')
fh.write(responsedata)
fh.close()
#p = re.compile("\s*\"_id\":\s*\"[a-z|A-Z|0-9]*\"")
re1 =p.match(i)
key=""
if(re1!=None):
	keylist =i.split(':')
	key = keylist[1]
	temp= 0
	print key	
		

	
	

