import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
tablepointer.execute("insert into appointment (time) values('9:30') where FirstName=('Geeta')")
dbvar.commit()
