# try only day and month...in string format
import time
import calendar
from datetime import date
from datetime import datetime
now=datetime.now()
mm=str(now.month)
dd=str(now.day)
yy=str(now.year)
# this is same as str(dd)
xtime=int(dd)
print xtime
#print yy
#print mm
print dd
# getting epoch for current time

samay=int(time.time())
print samay
# this also gives currenttime eopoch

x=time.mktime(now.timetuple())
print x

#y=datetime.datetime(2014,11,13,0,0).strftime('%s')
#print y
#aptDate=raw_input("Which day would you like to come?:")

#reqDate=datetime.fromtimestamp(aptDate).strftime('%m/%d/%y')
#print reqDate
# below code converts given date time into epoch

dt = datetime.strptime("14/11/14 16:30", "%d/%m/%y %H:%M")
print dt
#import time first, then 
vel=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch)) 
#Replace time.localtime with time.gmtime for GMT time
print vel


dateInput = raw_input("Please enter date in mm/dd/yyyy format: ")
#if validDate(dateInput)==1:
date_time = dateInput + ' 00:00:00'
patern = '%m/%d/%Y %H:%M:%S'
aptDateEpo = int(time.mktime(time.strptime(date_time, patern)))
print aptDateEpo