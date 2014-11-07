#hello Venkat,
#sorry i am sendingthe code now , as i lost connection to unix server and my code was there.
#this code does the comparing the ip_adress match only with the first element from newlist(ip got from server connection)after first match comes out from the loop.
import sys
import os
import json
from pprint import pprint
#getting ip address connected to the server using netstat command and appending it to  list "iplist"
f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u ")
for i in f.readlines():
        iplist=[]
        iplist.append(i)
        iplist.sort()
       # print iplist
#opening the json file and getting the valid ip address that can connect to server and loadin it to variable "data"
with open('confi.json') as data_file:
    data = json.load(data_file)
#calculating the length of the "data" futher can be used to iterate through the elements
def getSize(data):
 count = 0
 for i in data:
  count = count+1
 return count
datalist=[]

print getSize(data)
#building a list "datalist" that hold all the VALUES of the "ipaddress"
for i in range(0,getSize(data)):
        datalist.append(data[i]["ipaddress"])

for ipadd in  datalist:
        print ipadd
from pprint import pprint
f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u ")
fh = f.readlines()
for i in fh:
        iplist=[]
        iplist.append(i)
 #       print iplist
        for i in iplist:
                i=i.rstrip()
                ip = i.split(':')
                newlist=[]
                newlist.append(ip[0])
                ipdatalist=[]
                for ipls in newlist:
                        print ipls
alertlist=[]
#newlist and "datalist" are the list got from server and json . here we check if ip address match or not
def compare(newlist,datalist):
        count =0
        newlist.sort()
        datalist.sort()
        nl= getSize(newlist)
        dl=getSize(datalist)
#       for i in range(nl,dl):
        for ip in newlist: #here this is an error it iterates throuh this for loop only for one element not all element in the newlist
			for ip in newlist:
                for ipadd in datalist:
                        print ip,ipadd
                        if(ip==ipadd):
                                count =0
                                print count
                                break

                else:
                        count = 1
                        print count
                #               break
        if(count!=0):
                print "making alert list",ip
                alertlist.append(ip)

        print"this is first loop"

compare(newlist,datalist)



