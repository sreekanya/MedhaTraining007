import json
import os
import sys
from pprint import pprint
#a=os.popen("netstat -an | grep 22 | awk '{print $5}' | cut -d: -f1 | sort -u")
#for ips in a.readlines():
#       print "IP Address List", ips


with open('ip.json') as data_file:
    data = json.load(data_file)

def getSize(data):
        count = 0
        for i in data:
                count = count+1
                return count
#returnMatches(a,data)

#print getSize(data)
#for i in range(0,5):
#       #print data[i]["ipaddress"]
#       a=os.popen("netstat -an | grep 22 | awk '{print $5}' | cut -d: -f1 | sort -u")
#       for ips in a.readlines():
#               ips= ips.strip("\n")
#               print  ips, data[i]["ipaddress"]
#               if ips == data[i]["ipaddress"]:
#                       print "All is well"
#               else:
#                       print "New IP found", ips
#       a.close()

def myvarIP():
        myD = {}
        a=os.popen("netstat -an | grep 22 | awk '{print $5}' | cut -d: -f1 | sort -u")
        for ips in a.readlines():
                ips = ips.strip("\n")
                for i in range(0, getSize(data)):
                        if(ips == data[i]["ipaddress"]):
                                myD[ips] = "Matched"
                                break
                        else:
                                myD[ips] = "Unmatched"
        for key in myD:
                if(myD[key] == "Unmatched"):
                        print "Something Wrong Unknown IP Address", key
                else:
                        print key

myvarIP()
