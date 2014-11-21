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
	knownip.append(data[i]['ipaddress'])
	#print knownip
	#print data[i]['ipaddress']
 # this prints only ip addresses from json file
 # store known ip addresses extract from json in knownip
 # match ipaddress from knownip with newip.txt
iplist=[]
newip=open('newips.txt','r')
for i in newip:
	#print i
	i=i.rstrip()
	ipaddressData=i.split(':')
	#print ipaddressData[0]
	iplist.append(ipaddressData[0])
	#for iplistdata in iplist:
	#print iplistdata
iplist.sort()
#for iplistdata in iplist:
	#print iplist
count=0
alertlist=[]
for ip in iplist:
	#print ip
	for kip in knownip:
		#print kip
		if (kip!=ip):
			#print "unknown ip"
			#count=0
			#print count
			alertlist.append(ip)
			break
			
			#print alertlist[0]
		else:
			count=1
			#print "known ip"
			#print count
			break


if(count==0):
	alertlist.append(ip)
	print alertlist
for aip in alertlist:
	print aip
# alert list is ok...now attach some file
# sending email using smtp
# trying to append list to msg
import smtplib

from_add = 'gitapatel245@gmail.com'
to_add = 'appigeeta@gmail.com'
test_msg=[]
test_msg=test_msg.append(alertlist)

uname = 'gitapatel245@gmail.com'
pword = 'python245'

server = smtplib.SMTP_SSL("smtp.gmail.com",465,)
print "starting ssl server"
#server.startssl()
print "logging in with user name & password"
server.login(uname,pword)
print "sending email..."
server.sendmail(from_add,to_add,test_msg)
print "stopping server.."
server.quit()
# script working
