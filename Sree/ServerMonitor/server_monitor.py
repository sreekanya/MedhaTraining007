#! /usr/bin/python

import json
import time
import re
import os
import smtplib

data=[]
ip_list=[]
nonauth_ip=[]
ips=[]
ip_json=[]
ip_final=[]

def send_mail():
	newlist=set(nonauth_ip)
	non_ip=list(newlist)
	alert=non_ip[0]
	for i in non_ip[1:]:
	  alert=alert+", "+i
	
	test_msg = "Some UnAuthorized ips are accessing the server  "+alert
	print test_msg
	Sub="Server Access"
	message='Subject: %s\n\n%s' %(Sub,test_msg)
	from_add = 'einfoteam@gmail.com'
	to_add = 'naninice200@gmail.com'

	uname = 'einfoteam@gmail.com'
	pword = 'einfoteam123'

	server = smtplib.SMTP_SSL("smtp.gmail.com",465)
	print "starting ssl server"
	#server.startssl()
	print "logging in with user name & password"
	server.login(uname,pword)
	print "sending email..."
	server.sendmail(from_add,to_add,message)
	print "stopping server.."
	server.quit()

def read_file():
	try:
		fh=open("serverip.log",'r')
	except:
		print "File not present"
	else:
		for line in fh:
			line=line.rstrip()
			ip_list.append(line)
	fh.close()

def read_json():
	with open("config.json") as data_file: 
		data = json.load(data_file)
	print data
	
	for i in range(0,6):
		ip_json.append(data[i]["IP"])
#		print list[i]
		
read_json()
#f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u")
os.system("netstat -an |grep tcp|awk '{print $5}' | sort -u > serverip.log")
#os.system("cut -d ':' serverip.log >serverips.log")
read_file()

for i in ip_list:
	ips.append(i.split(':'))

for i in ips:
	ip_final.append(i[0])	

print ip_final

for i in ip_final:
	count=0
#	print i
	for j in ip_json:
		if(i==j):
		  count=1
		  break
	if (count==0):
	  nonauth_ip.append(i)

print "Non authorized ips",nonauth_ip
	  
if(len(nonauth_ip)>0):
	send_mail()	  
