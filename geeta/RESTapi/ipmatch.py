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
for i in range(0,5):
	print data[i]["ipaddress"]
 # this prints only ip addresses from json file
	f=os.popen("netstat -tn 2>/dev/null | grep :22 | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head")
for i in f.readlines():
 print "ip address list",i
 print f

