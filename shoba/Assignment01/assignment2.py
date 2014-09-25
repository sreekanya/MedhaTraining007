import sys
import calendar
import datetime
from datetime import date
today = date.today()
print today
print today.year
from datetime import datetime

my_date = raw_input("Enter B'date in mm/dd/yyyy format:")

b_date = datetime.strptime(my_date, '%m/%d/%Y')
print "Age : %d" % ((datetime.today() - b_date).days/365)
age =((datetime.today() - b_date).days/365)
if age > 18 :
	print "your are age is above 18"
else:
    print "your age is below 18	"
# i got this from internet can u please explain wht is %d "

#dob = (raw_input("enter the year u are born in format of mm/dd/yyyt"))
#print dob.year
#ur_age =t2y - dob.year
#print ur_age
