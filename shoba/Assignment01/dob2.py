import sys
import datetime
from datetime import date
from datetime import datetime
today = date.today()
my_date = raw_input("Enter B'date in mm/dd/yyyy format:")
b_date = datetime.strptime(my_date, '%m/%d/%Y')
print "given date birth is : " ,b_date
if today == b_date:
	print "its today"
else:
	print "its not today"
