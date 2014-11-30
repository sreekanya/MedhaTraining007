import MySQLdb
dbvar=MySQLdb.connect("localhost","root","admin","test")
FN=raw_input("Pls enter your first name:")
LN=raw_input("Pls enter your last name:")

tablepointer=dbvar.cursor()
tablepointer.execute("select * from profile where FirstName=('Geeta')")
data=tablepointer.fetchall()
print data

tablepointer.execute(IF EXISTS SELECT * FROM profile WHERE FirstName = Geeta
BEGIN
--do what needs to be done if exists
print "found"
END
ELSE
BEGIN
--do what needs to be done if not
print "not found"
END)
#tablepointer.execute("insert into profile1 (FirstName) values('shoba')")
#dbvar.commit()
# script not working...did in project2.py
