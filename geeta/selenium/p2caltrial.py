# try only day and month
from datetime import datetime
now=datetime.now()
mm=str(now.month)
dd=str(now.day)


thisday= mm+"/"+dd
enterdate=raw_input(%s,"pls enter todays date mm/dd:")
if (enterdate>=thisday):
	print "you entered valid"
else:
	print" please enter todays or more date,u entered wrong date"
	
