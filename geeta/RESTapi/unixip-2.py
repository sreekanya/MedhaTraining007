import json
import sys 
from pprint import pprint
import os

with open('config.json') as data_file:    
    data = json.load(data_file)

def getSize(data):
 count = 0 
 for i in data:
  count = count+1
 return count
knownip=[]
#print getSize(data)
for i in range(0,5):
	#print data[i]["ipaddress"]
	knownip=data[i]['ipaddress']
	#print knownip
	print data[1]['ipaddress']
 # this prints only ip addresses from json file
 # store known ip addresses extract from json in knownip
 # match ipaddress from knownip with ip5-1
ips={}
f="newips.txt"
newip=open(f,'r')
ips={newip}
print data[0]

for i in ips:
	#i=rstrip.newip()
	#newi=isplit.i(',')
	if(i==knownip[1]):
 		print "there"
	else:
 		print "no match"
 	#print i
# if condition is failing


	#f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u")
#for i in f.readlines():
 #print "ip address list",i
 #print f

