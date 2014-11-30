import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
tablepointer=dbvar.cursor()
tablepointer.execute("alter TABLE doctorcalender DROP COLUMN slot5")
dbvar.commit()