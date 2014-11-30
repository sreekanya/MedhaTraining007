
import re
import datetime
from datetime import date
from datetime import datetime
today = date.today()
print today
month=today.month
day= today.day
dat= str(month)+'/'+ str(day)
print dat



getDt=raw_input("Please enter your birth date in mm-yy format: ")
pattern= re.compile('[-\/]')
getDt= re.sub(pattern, ',', getDt)
#print getDt

myDate=getDt.split(',')
#print myDate[0]
correctDate=0
try: 
	bd=datetime(int(myDate[0]),int(myDate[1]),int(myDate[2]))
	correctDate=1
except:
	print "not a valid date"
else:

	birthday = myDate[1]+'/'+myDate[2]

#birthDate = str(validDate.month)+'/'+str(validDate.day)
#	print birthDate
	
if(dat == birthday):
	print"Happy Birthday!"
else:
	print "oops! not your birthday"