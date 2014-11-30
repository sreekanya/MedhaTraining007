# insert user input values  into tables 

import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
fn=raw_input("pls enter ur name:")
ln=raw_input("pls enter ur last name:")
#print fn
tablepointer=dbvar.cursor()
tablepointer.execute("insert into profile1 (FirstName,LastName) values (%s,%s)",(fn,ln))
dbvar.commit()
# script is working
