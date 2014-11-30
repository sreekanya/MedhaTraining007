import calendar
import datetime
import time
epochvalue=calendar.timegm(time.gmtime())
print epochvalue

epochlocal=calendar.timegm(time.localtime())
print epochlocal
# getting time in epoch
#x=time.mktime(time.gmtime(0))
#print x

#print time1
# below one gives current epoch time

samay=int(time.time())
print samay