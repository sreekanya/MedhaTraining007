import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
tablepointer.execute("select * from profile1")
data=tablepointer.fetchall()
print data