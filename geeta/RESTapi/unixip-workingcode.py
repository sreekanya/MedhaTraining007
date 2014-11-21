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


print getSize(data)
for i in range(0,3):
	print data[i]["ipaddress"]
 # this prints only ip addresses from json file
	f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u")
for i in f.readlines():
 print "ip address list",i
 print f

