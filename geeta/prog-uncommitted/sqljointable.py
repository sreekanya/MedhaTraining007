# trying to update appointment wit h join tables
# ask patient name and appt time 
name=raw_input("pls enter your name:")
appointment1=raw_input("enter time:")
#connect to sql 
import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
#insert into app2 name and time 
tablepointer.execute("insert into app3 (patientname,time) values(%s,%s)",(name,appointment1))
dbvar.commit()

 
