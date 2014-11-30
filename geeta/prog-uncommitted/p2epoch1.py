# epoch conversion 
# given date time is converted to epoch
import time 
#first, then
#dt=int(time.mktime(time.strptime('2014-11-14 11:30:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone
#print dt

dateInput=raw_input("pls enter date in yyyy-mm-dd H:M:S format:")
date_time = reqDate + ' 00:00:00'
patern = '%m/%d/%Y %H:%M:%S'
print reqDate
dt=int(time.mktime(time.strptime(date_time, '%Y/%m/%d %H:%M:%S'))) - time.timezone
print dt



#dateInput = raw_input("Please enter date in mm/dd/yyyy format: ")
#if validDate(dateInput)==1:
date_time = dateInput + ' 00:00:00'
patern = '%m/%d/%Y %H:%M:%S'
aptDateEpo = int(time.mktime(time.strptime(date_time, patern)))
print aptDateEpo