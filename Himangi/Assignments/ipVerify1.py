import json
import os
import sys
from pprint import pprint
import smtplib

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
def sendEmail():
    from_add = 'pythonclass14@gmail.com'
    to_add = 'naninice2000@gmail.com'

    test_msg = a

    uname = 'pythonclass14@gmail.com'
    pword = 'python2014'

    server = smtplib.SMTP_SSL("smtp.gmail.com",465,)
    print "starting ssl server"
    #server.startssl()
    print "logging in with user name & password"
    server.login(uname,pword)
    print "sending email..."
    server.sendmail(from_add,to_add,test_msg)
    print "stopping server.."
    server.quit()     
    # a.close()

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
                        a="Something Wrong Unknown IP Address", key
                        sendEmail(a)
                else:
                        print key

myVarIP()
