# trying calendeer for proj1..
import calendar
import time

cal=calendar.calendar(2014,w=2,l=1,c=6)

#print cal

pat=calendar.firstweekday()
#print pat

calMonth=calendar.month(2014,8,w=2,l=1)
print calMonth
# this prints august month calender of 2014

cm=calendar.monthcalendar(2014,8)
#print cm
# this gives weeks in list of ints,
cr=calendar.monthrange(2014,6)
#print cr
cs=calendar.setfirstweekday(4)

#print cs
# not understanding what it prints

cw=calendar.weekday(2014,8,9)

print cw