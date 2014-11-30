
# trying to use try block for matching 

# take name inputs from user,check already exists or no,if not make a new profile.

#connect to mysql
import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
 #matching only first name 

FN=raw_input("Pls enter your first name:")
#LN=raw_input("Pls enter your last name:")
# try  the try block for this further

tablepointer=dbvar.cursor()

try :
	tablepointer.execute("select FirstName from profile where FirstName like (%s)",(FN))

	data=tablepointer.fetchall()
	data1= data[0][0]
except:
	print FN , "NOT THERE"
	
else:	
	
    print data1 ,"is there"
# script is working checking name and matching there or not


#take user input


#if (FN==data1):
#	print "match",FN,data1
#else:
	#print"no match",FN,data1
#tablepointer.execute("insert into profile1 (FirstName) values('shoba')")
#dbvar.commit()