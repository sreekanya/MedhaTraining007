import json
import sys 
from pprint import pprint
import os
import filecmp


with open('config.json') as data_file:    
    data = json.load(data_file)

def getSize(data):
 count = 0 
 for i in data:
  count = count+1
 return count
print getSize(data)
for i in range(0,5):
	print data[i]["ipaddress"]
 # this prints only ip addresses from json file
	f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u")
for i in f.readlines():
 print "ip address list",i
 print f
file1=open(winelist2.csv)
filecmp.cmp(winelist2.csv,ipaddress.json)