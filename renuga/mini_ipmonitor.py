import json
import sys
import os

from pprint import pprint
import os
with open('clientjson.json') as data_file:
    data = json.load(data_file)
iplist=[]

def getSize(data):
        count = 0
        for i in data:
                count = count+1
        return count
# To capture Iplist 
def capip():
        f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u ")
        #iplist=[]
        for i in f.readlines():
                #print "ip address list",i
                i=i.rstrip()
                j=i.split(':')
				iplist.append(j[0])
		return iplist


print getSize(data)
val=getSize(data)
#To compare the IPlist with json file.
capip()
print iplist
flag=0
for k in range(1,len(iplist)):
        for i in range(0,val):
             if (iplist[k]==data[i]["ipaddress"]):
                print "safe and known ip address"
				flag=1
				break
             else:
					flag=0
		if flag==0:
			print "alert"+iplist[k]
 # Instead of alert we need to write script using smtplib and call here.                         