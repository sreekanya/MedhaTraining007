# sending greetings assignment.
# open csv file of email addresses and read and make hash table.
from datetime import datetime
now=datetime.now()
mm=str(now.month)
dd=str(now.day)
thisday= mm+"/"+dd	
print thisday
# now getting data from csv file
DOBMAP={}
fh=open("bday.csv",'r')
for line in fh:
	line=line.rstrip()
	data=line.split(',')
	DOBMAP[data[1]]=data[0]+data[2]
	email=data[1]
	bday=DOBMAP[data[2]]
	print email
	print bday


	if (thisday==bday):
		print "its ur bday",data[0],data[2]
	else:
		print"not ur bday"
#fh1=open("greetings.txt",'r')
#print fh1
listofemails=DOBMAP.keys()	
def sendemail(emailaddress,name):
	toemail.send_keys(emailaddress)
	emailcontent='hi'+name
	emailbody.send_keys(emailcontent)

for eachmail in listofemails:
	print DOBMAP[eachmail]
	#sendemail(eachemail,DOBMAP[eachmail])