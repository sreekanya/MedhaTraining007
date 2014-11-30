# take name inputs from user,check already exists or no,if not make a new profile.

#connect to mysql
import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
 #matching only first name 

FN=raw_input("Pls enter your first name:")
#LN=raw_input("Pls enter your last name:")

tablepointer=dbvar.cursor()
tablepointer.execute("select FirstName from profile where FirstName like (%s)",(FN))
data=tablepointer.fetchall()
data1= data[0][0]
print data1,

if (FN==data1):
	print "match",FN,data1
else:
	print"no match",FN,data1
#tablepointer.execute("insert into profile1 (FirstName) values('shoba')")
#dbvar.commit()
