import calendar
import re
import datetime
from datetime import date
from datetime import datetime
patientAptInfo={}
#patientAptInfo[curYear]={}
#patientAptInfo[year][months]={}
#patientAptInfo[year][months][days]={}
#patientAptInfo[year][months][days][time]={}
today= datetime.now()
dat = today.day
curYear= today.year
curMon= today.month
curMon=int(curMon)

def bookApts(year,month,day,matchTm,name):
	myRecord=open("appointments.csv" ,'a')
	myStr=str(year)+str(month)+str(day)+matchTm.group(0)+','+name
	myRecord.write(myStr)
	myRecord.write('\n')
	myRecord.close()

def accessCsv(year,month,day,tm,matchTm): 
	checkStr= str(year)+str(month)+str(day)+matchTm.group(0)
	fh=open("appointments.csv", 'r')
	found = 0
	for i in fh:
		i=i.rstrip()
		eactPatient=i.split(',')
		#print patientAptInfo[year][month][day][matchTm][name]
		#print eactPatient
		if (eactPatient[0] == checkStr):
			print "Sorry, this slot is taken."
			found = 1
			fh.close()
			break
	if(found == 0):				
		name = raw_input("Please enter your first snd last name: ")   
		bookApts(year,month,day,matchTm,name)
		print "Appointment scheduled successfully"
		return 1
	return 0

def chooseYear(curMon,curYear):
	
#print curMon
	year=int(curYear)
#print year

	if curMon>=8:
		nextYear = raw_input("Please enter the year:")
		nextYear=int(nextYear)
		while nextYear!= year or nextYear!=year+1:
			if nextYear>=year+2:
				print "You can schedule an appointment only 4 months ahead of appointment date. "
				nextYear = raw_input("Please enter the year:")
				nextYear=int(nextYear)
			elif nextYear<=year-1:
				print "Sorry, We can not schedule an appointment for a year which has already been passed."	
				nextYear = raw_input("Please enter the year:")
				nextYear=int(nextYear)
			elif nextYear==year+1:
				year=nextYear
				break
			elif nextYear==year: 
				year=nextYear
				break
	
		getMonth(curMon,curYear,year)


#patientAptInfo[year]={}
#year=int(year)

#print year
def getMonth(curMon,curYear,year):
	whichMonth=raw_input("Please enter the number of the month: ")
	whichMonth=int(whichMonth)
	while year==curYear:
		if whichMonth<curMon:
			print "Sorry, We can not schedule an appointment for a month which has already been passed."
			whichMonth=raw_input("Please enter the number of the month: ")
			whichMonth=int(whichMonth)
		else:
			break
	while year==curYear+1:
	
		if whichMonth > 4-(12-curMon):
			print "Sorry, We can not schedule an appointment for more than four months ahead of time."
			whichMonth=raw_input("Please enter the number of the month: ")
			whichMonth=int(whichMonth)
		else:
			break
	cal=calendar.month(year, whichMonth)
	month= whichMonth
	
	print cal
	getDate(year,whichMonth,curMon,month)

x=True
def getDate(year,whichMonth,curMon,month):

	dt=raw_input("Please enter the date: ")
	dt=int(dt)
	def convertDay(year, whichMonth, dt):
	
	
		ans = date(year, whichMonth,dt)
		month=ans.strftime("%B")
		#ans = datetime.date(year, whichMonth,dt)
		whichDay = ans.strftime("%A")
		return whichDay

	while whichMonth==curMon: 
		if dt<=dat:
			print dt, "has already been passed. Plese choose another date."
			dt=raw_input("Please enter the date: ")
			dt=int(dt)
		else:
			break
	while whichMonth==4-(12-curMon): 
		if dt>=dat:
			print "I'm here Sorry, We can not schedule an appointment for more than four months ahead of time." 
			dt=raw_input("Please enter the date: ")
			dt=int(dt)
		else:
			break	
#month=whichMonth
#patientAptInfo[year][months]={}

#print month



	whichDay = convertDay(year,whichMonth,dt)
	while (whichDay=="Saturday" or whichDay=="Sunday"):
		print "Sorry, We don't work on weekend."
		dt=raw_input("Please enter the date: ")
		dt=int(dt)
		whichDay=convertDay(year,month,dt)

		print whichDay	

	else:
		day=str(dt)
		
		x=0
		while x==0:
			x=getTime(year, month, day)

def getTime(year,month,day):  
	booked = 0
	print "Our work hours are from 9.00 AM to 11:30 AM and 1:00 PM to 5:30 PM"
	print "Appointments are scheduled on half hour intervals. ie: 9:00 AM, 9:30 AM" 
	validation = 'True'
	while(validation == 'True'):
		tm = raw_input("Please enter the time, use hour:mins.format : ")
		pattern= re.compile('[1-5]\:00|[1-5]\:30|(9|10|11\:00)|(9|10\:30)')
		matchTm=pattern.match(tm)
		if(matchTm):
			booked = accessCsv(year,month,day,tm,matchTm)
			print "hi"
			validation = 'False'
			break
	return booked
		
#print "please wait, let me check the availability"
	
#if not matchTm in patientAptInfo[year][month][day]:
#patientAptInfo[year][month][day][matchTm] = {} 

#name = raw_input("Please enter your first snd last name: ")		
#bookApts(year,month,day,matchTm,name)
#print "Appointment scheduled successfully"
	#print patientAptInfo.values
	
	#if patientAptInfo[year]!=year:
	#	patientAptInfo[year]={}
	#
	#	if patientAptInfo[year][month]==month:
	#		if patientAptInfo[year][month][day]==day:
	#			if patientAptInfo[year][month][day][matchTm]!=matchTm:
	#				if not matchTm in patientAptInfo[year][month][day]:
	#					patientAptInfo[year][month][day][matchTm] = {} 	
	#				bookApts(year,month,day,matchTm,name)
	#			else:
	#				print "Sorry, This slot is already booked." 

	#slotdict = checkAvailability()
def checkAvailability():
	chooseYear(curMon,curYear)
checkAvailability()		
					
	

def appointmanager():
	pass

def bookappointment():
	pass



