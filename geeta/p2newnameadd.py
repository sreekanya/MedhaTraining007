# trying to enter new profile which doesnot exists

# trying to use try block for matching 

# take name inputs from user,check already exists or no,if not make a new profile.
# doing all tasks listed above

#connect to mysql
import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
 #matching only first name 

FN=raw_input("Pls enter your first name:")
#LN=raw_input("Pls enter your last name:")
# try  the try block for this further

tablepointer=dbvar.cursor()

# if name not there enter that into table

try :
	
	tablepointer.execute("select FirstName from profile where FirstName like (%s)",(FN))

	data=tablepointer.fetchall()
	data1= data[0][0]
except:
	print FN , "NOT THERE"
	print "You are new patient,give some details to make your profile"
	
	fn=raw_input("pls enter ur name:")
	ln=raw_input("pls enter ur last name:")
	bd=raw_input("Pls enter ur DOB:")
	ct=raw_input("Pls enter the contact no:")
	ad=raw_input("Pls enter your address:")
	ins=raw_input("pls enter the insurance detail:")
	ect=raw_input("pls enter the emergency contact no:")
	em=raw_input("pls enter email:")
	tablepointer=dbvar.cursor()
	tablepointer.execute("insert into profile (FirstName,LastName,DOB,contact,Adress,insurance,emergencycontact,Email) values (%s,%s,%s,%s,%s,%s,%s,%s)",(fn,ln,bd,ct,ad,ins,ect,em))
	dbvar.commit()
	
else:	
	
    print data1 ,"is there"
# now check for apt available time
#display appt times from 
tablepointer.execute("select time from appointment")
data=tablepointer.fetchall()
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
# update(write) appt time entered by patient to appt table
# unable to write name where appt time is the time entered by patient
	tablepointer.execute("update appointment set (FirstName) values(%s)",(FN), where time like (appt))