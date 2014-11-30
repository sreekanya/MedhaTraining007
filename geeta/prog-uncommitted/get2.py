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
pat1 = re.compile("\s*\"[a-z]+\":\s*\"[a-z|A-Z|0-9]*\"")
p = re.compile("\s*\"_id\":\s*\"543e02fa77ed822e0664e75c\"")
rf = open('response.txt','r')
count = 0
for i in rf:
	i=i.rstrip()
	m=p.match(i)
 
	if(m!=None):
		print "able to find ID"
		print i
		count = count+1
		data=i.split(':')

		print data[0]

		


print count