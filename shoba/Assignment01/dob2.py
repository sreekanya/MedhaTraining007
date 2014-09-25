import sys
import datetime
from datetime import date
from datetime import datetime
today = date.today()
my_date = raw_input("Enter B'date in mm/dd/yyyy format:")
dateinfo = my_date.split('/')
b_date=date(int(dateinfo[2]),int(dateinfo[0]),int(dateinfo[1])) #.format('YYYY-MM-DD')
newdate = b_date.month
print "given date birth is : " ,b_date," today is ",today
if today == b_date:
	print "its today"
else:
	print "its not today"
