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

p = re.compile("\s*\"_id\":\s*\"543cb3dc1360bd32079b1f31\"")
rf = open('response.txt','r')
count = 0
for i in rf:
	i=i.rstrip()
	m=p.match(i)
 
	if(m!=None):
		print "able to find ID"
		print i
		count = count+1

print count