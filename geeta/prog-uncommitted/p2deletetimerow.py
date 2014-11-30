# to delete time chosen from patient from avaialable time table
appt0=raw_input("what time u want:")
print appt0
# connect to toad from table delete that title
import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
tablepointer.execute("select time from app4")

data=tablepointer.fetchall()
print data
tablepointer.execute("delete from app4 where time like(%s)"(appt0))
dbvar.commit()