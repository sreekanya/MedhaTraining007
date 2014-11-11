import json
import sys
import os
import smtplib
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
def capip():
        f=os.popen("netstat -an | grep tcp | awk '{print $5}' | sort -u ")
        #iplist=[]
        for i in f.readlines():
                #print "ip address list",i
                i=i.rstrip()
                j=i.split(':')
                iplist.append(j[0])
        return iplist
def sendmail():
        from_add='renu1suresh@gmail.com'
        to_add='naninice2000@gmail.com'
        subject="Alert mail for server"

        text="The following unknown ip address are connected to server ALERT !!!"+str(alertlist)+"Known IpAddress"+str(known)
        msg='Subject: %s\n\n%s'%(subject,text)
        username='renu1suresh@gmail.com'
        password='$urmohit1'
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        print "connecting server"
        print"Logging in to the account with Credentials"
        server.login(username,password)
        print "Sending mail"
        server.sendmail(from_add,to_add,msg)
        print "Succesfully sent mail"
        print "Quiting server"
        server.quit()

print getSize(data)
val=getSize(data)

capip()
print "Ip connected to server"
print iplist
flag=0
alertlist=[]
known=[]
for k in range(1,len(iplist)):
        for i in range(0,val):
                if (iplist[k]==data[i]["ipaddress"]):
                       # print "safe and known ip address"
                        known.append(iplist[k])
                        flag=1
                        break
                else:
                        flag=0
        if (flag==0):
                print "Unknown ip address Alert!!!"+iplist[k]
                alertlist.append(iplist[k])
print "Alert list who are unknown working on server"
alertlist=list(set(alertlist))
print alertlist
print "Who is known ips working on the server"
print known
sendmail()
