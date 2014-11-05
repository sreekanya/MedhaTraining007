# ipaddress match project...taking one same ip address in both files and trying to match that one value first
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
iplist=[]
f="newips.txt"
newip=open(f,'r')
for i in newip.readlines():
	#ip=i.rstrip()
	#iplist1=iplist.append(ip);
	print i

	if (i==data[1]['ipaddress']):
		print "there"
	else:
		print "not there",i,data[1]['ipaddress']
# its not matching both values though they are same
