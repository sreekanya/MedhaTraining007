import sys
import os
import json
from pprint import pprint
import smtplib, socket
import ssl

json_list=[]
server_ip=[]
iplist=[]
invalid_ip=[]
valid_ip=[]
alert_list=[]

# function to send email alert using smtp module

def sendmail():
                ip=set(invalid_ip)
                newip=list(ip)
                non_auth = newip[0]
                for i in newip[1: ]:
                        non_auth =non_auth + "  " +i
                from_add= 'shobasrinath.s@gmail.com'
				 to_add='pythonclass14@gmail.com'
                test_msg = "hello class, This is Shoba ..these  are the list of invalid ip address found connected to server "+non_auth
                Subject="these ip are unknown"
                usname='pythonclass14@gmail.com'
                pword='python2014'
                server = smtplib.SMTP_SSL('smtp.gmail.com',465)
                print "starting ssl server"
                #server.startssl()
                print "logging in with user name & password"
                server.login(usname,pword)
                print "sendin email...."
                server.sendmail(from_add,to_add,test_msg,Subject)
                print"stopping server."
                server.quit()




#opening the json file and getting the valid ip address that can connect to server and loadin it to variable "data"
def open_json_file():
        with open('confi.json') as data_file:
		data = json.load(data_file)
        for i in range(0,len(data)):
            json_list.append(data[i]["ipaddress"])
#       print"this ip from json file " , json_list
open_json_file()


f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u ")
fh = f.readlines()
for i in fh:
        server_ip.append(i)
for i in server_ip:
        i=i.rstrip()
        ip = i.split(':')
        iplist.append(ip[0])
#print "this is server ip",iplist

for i in iplist:
    count=0
    for j in json_list:
#       print "this is ip from server", i
#       print "this is ip from lson",j
        if(i==j):
		 count=1
            break
        if (count==0):
                invalid_ip.append(i)

#       print "Non authorized ips",invalid_ip

if(len(invalid_ip)>0):
    sendmail()

                                                              67,1          70%

                                                              44,1-8        35%

"ip_check.py" 85L, 1871C                                      1,1           Top
