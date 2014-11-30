# check apt time avvailable or not

import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
#display appt times from 
tablepointer.execute("select time from appointment")
data=tablepointer.fetchall()
#data1=data[0][0]
print data
print data[0][0],data[1][0],
print data[2][0]
# asking desired appt time and matching with appt table
appt=raw_input("what time you want the appt?:")
if appt==data[0][0]:
	print "booked"
elif appt==data[1][0]:
	print "is taken"
else:
	print "available"
# trying to print available appt
	tablepointer.execute("select time from appointment where FirstName=('')")
	avail=tablepointer.fetchall()
	print avail[0][0]
	print avail[1][0]
	print avail[2][0]
	print avail[3][0]
	print avail[4][0]
# now the new appt taken should update in appt table ..write in table