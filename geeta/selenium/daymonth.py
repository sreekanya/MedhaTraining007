# try only day and month
from datetime import datetime
now=datetime.now()
mm=str(now.month)
dd=str(now.day)


thisday= mm+"/"+dd
enterdate=raw_input("pls enter todays date mm/dd:")
if (thisday==enterdate):
	print "you enter todays date"
else:
	print" please enter todays date,u entered wrong date"