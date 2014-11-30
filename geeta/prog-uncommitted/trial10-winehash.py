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

#p = re.compile("\s*\"_id\":\s*\"[a-z|A-Z|0-9]*\"")
pat = re.compile("\s*\"[a-z]+\":\s*\"[a-|A-Z|0-9]*\"")
rf = open('response.txt','r')
count = 0
temp=0
datalist={}
p = re.compile("\s*\"_id\":\s*\"543cb3dc1360bd32079b1f31\"")
rf = open('response.txt','r')
count = 0
for i in rf:
	i=i.rstrip()
	m=p.match(i)
 
	if(m!=None):
		print "able to find ID",m
		count = count+1
for i in rf:
	i=i.strip()
	match=p.match(i)
	if (match!=None):
		print i
		#datai=i.strip('" "')
		#data1=datai.rstrip()
		data=i.split(':')
		
		#print data[0]
		#print data[1]
		datalist[data[0]]=data[1]
		#temp=temp+1
		#for j in datalist:
			#print datalist.keys[0]
		#print datalist.keys()
			#if (datalist.keys[0]=="country"):
				#print "got it"
			
		
			
		