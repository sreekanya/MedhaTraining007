#validating user input...names

#connect to mysql
import MySQLdb
import re
dbvar=MySQLdb.connect("localhost","root","admin","test")
 #matching only first name 

FN=raw_input("Pls enter your first name:")

pt=re.compile('^[a-z|A-Z]*$')
result=pt.match(FN)
if (result!=None):
	print "valid name"
else:
	print "invalid entry"
#LN=raw_input("Pls enter your last name:")
# try  the try block for this further

tablepointer=dbvar.cursor()
tablepointer.execute("select FirstName from profile where FirstName like (%s)",(FN))
data=tablepointer.fetchall()
data1= data[0][0]
print data1


#take user input


if (FN==data1):
	print "match",FN,data1
else:
	print"no match",FN,data1