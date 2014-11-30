import re
import sys
import time
import calendar
import datetime
from datetime import date
from datetime import datetime
import random
import MySQLdb
import collections
import calendar
dbvar = MySQLdb.connect("localhost","root","admin","test")
tablepointer = dbvar.cursor()


def setWeek(aptDateEpo):

	d=datetime.fromtimestamp(aptDateEpo).strftime('%m/%d/%Y')
	
	month, day, year = (int(x) for x in d.split('/')) 
	ans = date(year, month,day)
	h=ans.weekday()
	weekend=h
	#if weekend==5:
	#	print "Oops! Its Saturday. We are not open on weekends so, please choose some other day."
	#	break
	#	w=0
	#elif weekend==6:
	#	print "Oops! Its Sunday. We are not open on weekends so, please choose some other day."
	#	break
	#	w=0
	#print  "no of the day" , h
	month=ans.strftime("%B")
		#ans = datetime.date(year, whichMonth,dt)

	dd = ans.strftime("%A")

	print dd
	epodayBefore=aptDateEpo-86400
	epotwoDaysBefore=epodayBefore-86400
	epodayAfter=aptDateEpo+86400
	epotwoDaysAfter=epodayAfter+86400
	if h==0:
		epodayBefore=aptDateEpo-86400*3
		epotwoDaysBefore=epodayBefore-86400
		epodayAfter=aptDateEpo+86400
		epotwoDaysAfter=epodayAfter+86400
	elif h==1:
		epodayBefore=aptDateEpo-86400
		epotwoDaysBefore=epodayBefore-86400*3
		epodayAfter=aptDateEpo+86400
		epotwoDaysAfter=epodayAfter+86400
	elif h==2:
		epodayBefore=aptDateEpo-86400
		epotwoDaysBefore=epodayBefore-86400
		epodayAfter=aptDateEpo+86400
		epotwoDaysAfter=epodayAfter+86400
	elif h==3:
		epodayBefore=aptDateEpo-86400
		epotwoDaysBefore=epodayBefore-86400
		epodayAfter=aptDateEpo+86400
		epotwoDaysAfter=epodayAfter+86400*3
	elif h==4:
		epodayBefore=aptDateEpo-86400
		epotwoDaysBefore=epodayBefore-86400
		epodayAfter=aptDateEpo+86400*3
		epotwoDaysAfter=epodayAfter+86400
	elif h==5:
		print "You have chosen Saturday. We don't work on weekends. Please choose the day and time from available appointments displayed below."
		epodayBefore=aptDateEpo-86400*2
		epotwoDaysBefore=epodayBefore-86400
		aptDateEpo=aptDateEpo-86400
		epodayAfter=aptDateEpo+86400*4
		epotwoDaysAfter=epodayAfter+86400

	elif h==6:
		print "You have chosen Sunday. We don't work on weekends. Please choose the day and time from available appointments displayed below."
		epodayBefore=aptDateEpo-86400*3
		epotwoDaysBefore=epodayBefore-86400
		aptDateEpo=aptDateEpo-86400*2
		epodayAfter=aptDateEpo+86400*3
		epotwoDaysAfter=epodayAfter+86400
	


	
	myweek=[epotwoDaysBefore,epodayBefore,aptDateEpo,epodayAfter,epotwoDaysAfter]
	timeSlots=["9:00","9:30","10:00","10:30","11:00","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"]
	
	for i in myweek:
	
		slots=collections.OrderedDict()
		aptday=datetime.fromtimestamp(i).strftime('%m/%d/%Y')
		month, day, year = (int(x) for x in aptday.split('/')) 
		ans = date(year, month,day)
		month=ans.strftime("%B")
		whichDay = ans.strftime("%A") 
		print whichDay
		print aptday
		#return aptday
		tablepointer = dbvar.cursor()
		tablepointer.execute("select time from availabilitycalendar where date like (%s)",(aptday))
		scheduledApts = tablepointer.fetchall()
		#print len(scheduledApts)
		for slot in timeSlots:
			if(len(scheduledApts) == 0):
				slots[slot] = 1
			for i in scheduledApts:
				#print slot, i[0], '\n'
				if slot == i[0]:
					if slot in slots.keys():
						del slots[slot]	
					break
				else:
					slots[slot]=1
		for key in slots:
			print key
				
					

def cancelRequest(result):
	c=0
	while c==0:
		dateInput = raw_input("What is your appointment date? Please enter date in mm/dd/yyyy format: ")
		if validDate(dateInput)==1:
			timeInput=raw_input("Please enter appointment time: ")
			pattern= re.compile('[1-5]\:00|[1-5]\:30|(9|10|11\:00)|(9|10|11\:30)')
			matchTm=pattern.match(timeInput)
			if(matchTm):
				tablepointer = dbvar.cursor()
				profile=tablepointer.execute("select accountNum from availabilitycalendar where (date) like (%s)", (dateInput)) 
				accountNum=tablepointer.fetchone()
				tablepointer.execute("select * from profile where accountNum like (%s)",(accountNum))
	 			data = tablepointer.fetchall()
	 			print data
	 			#del = tablepointer.execute("delete from profile where accountNum = %saccountNum")
	 			tablepointer.execute("delete from availabilitycalendar where accountNum = %s", accountNum)

	 			print "Your appointment has been successfully canceled."

	 			c=1
	 	else:
	 		c=0
	else:
	 	c=0





def scheduleRequest(result):
	myEpo=int(time.time())
	c=0
	while c==0:
		dateInput = raw_input("When would you like to come in? Please enter date in mm/dd/yyyy format: ")
		if validDate(dateInput)==1:
			date_time = dateInput + ' 00:00:00'
			patern = '%m/%d/%Y %H:%M:%S'
			aptDateEpo = int(time.mktime(time.strptime(date_time, patern)))
			timeLimitEpo=aptDateEpo - myEpo
			if timeLimitEpo<10518976 and aptDateEpo>myEpo:

				setWeek(aptDateEpo) 
				
				decide = raw_input("Do you want to finalise any of the dates displayed above? Yes or No:  ")
				if decide=="Yes":
					dateInput1 = raw_input("Please enter the date: ")
					print "Our work hours are from 9.00 AM to 11:30 AM and 1:00 PM to 5:30 PM"
					print "Appointments are scheduled on half hour intervals. ie: 9:00 AM, 9:30 AM" 
					validation = True
					while validation:
						timeInput = raw_input("Please enter the time, use hour-mins.format : ")
						pattern= re.compile('[1-5]\:00|[1-5]\:30|(9|10|11\:00)|(9|10|11\:30)')
						matchTm=pattern.match(timeInput)
						if(matchTm):
							dateInput=str(dateInput1)
							timeInput=str(timeInput)
							tablepointer.execute("insert into availabilitycalendar (accountNum,date,time) values (%s,%s,%s)", (result, dateInput1, timeInput))
							dbvar.commit()
							print "Thank you! Your appointment is scheduled on " + dateInput1 + " at " + timeInput+'/n'
						
							validation= False
							quitRequest(result)
							c=1
				#else:
				#	c = 0			
			elif aptDateEpo<myEpo:
				print "Sorry, We can not schedule an appointment for a date which has already been passed."
				c=0		
			elif timeLimitEpo>10518976:
				print "You can schedule an appointment only 4 months ahead of appointment date. "
				c=0 
		else:
			print "Here!!Invalid date. Please enter date again!"
			c=0
		#c=1

def quitRequest(result):
	m=0
	while m==0:
		more = raw_input("Is there anything we can do for you today? enter schedule to schedule, cancel to cancel or reschedule to reschedule and No to quit.:  ")
		if more!=' ' or more!='':
			if more=="schedule":
				scheduleRequest(result)
				m=1
			elif more=="cancel":
				cancelRequest(result)
				m=1
			elif more=="reschedule":
				cancelRequest(result)
				scheduleRequest(result)
				m=1
			elif more=="quit":
				exit()
				m=1
		else:
			m=0



						


def fetchCustData(check):
	tablepointer = dbvar.cursor()
	profile=tablepointer.execute("select accountNum from profile where emailID like (%s)", (check)) 
	fetchprofile=tablepointer.fetchone()
	#print fetchprofile[0]
	return fetchprofile[0]
	

def requestProcess(result):
	action = raw_input("Do you want to schedule a new appointment or reschedule or cancel existing appointment?: ")
	c=0
	while c==0:
		if action!= '':
			if action=="schedule":
				scheduleRequest(result)
				#sys.quit()
				c=1
				
			elif action=="reschedule":
				cancelRequest(result)
				scheduleRequest(result)
				#sys.quit()
				c=1

			elif action == "cancel":
				cancelRequest(result)
				#sys.quit()
				c=1

		else:
			action = raw_input("Do you want to schedule a new appointment or reschedule or cancel existing appointment?: ")
			c=0


def validDate(dateInput):
	try:
		dateprocess = time.strptime(dateInput, '%m/%d/%Y')
		if dateprocess:
			return 1
	except ValueError:
		#print "Oops! not a valid date try again"
		return 0


	

def findCust(check):
	dateInput =  raw_input("Please enter your date of birth: ")
	if validDate(dateInput)==1:
	
		print "matched"
	#bdate=findbyDOB.split('/')
	#year= bdate[2]
	#month=bdate[0]
	#bd=bdate[1]				
	#year=int(year)
	#month=int(month)
	#bd=int(bd)
	#birthdate = date(year, month, bd)
	#print birthdate	
		match = tablepointer.execute("select DOB from profile where DOB like (%s)", (dateInput))
		if match:
			verifyStreetAdd = raw_input("Please enter your street address: ")
			#splitName= verifyName.split(' ')
			#splitName= str(splitName[0])+' ' + str(splitName[1])
			#print splitName
	 		matchAdd = tablepointer.execute("select address from profile where DOB like (%s)", (dateInput))
	 		if matchAdd:
	 			print "We found you."
	 			#result=fetchCustData(check)
	 			tablepointer.execute("select * from profile where DOB like (%s)",(dateInput))
	 			data = tablepointer.fetchall()
	 			print data
	 			result=raw_input("Please enter email id: ")
	 			requestProcess(result)
	 			### get Date (DD) Get Month in MM format & Get Year YY or YYYY format 
	 			### DATEOFMONTH()
	 			### YEAR()
	 			### MONTH()
	 		
	 		else:
	 			print "We are sorry. We are unable to find your record."
	 			createNewProfile()


	else:	
		print ("Your birthdate does not match with our record. You need to create a new profile.")
		createNewProfile()
def check():
	dbvar = MySQLdb.connect("localhost","root","admin","test")
	tablepointer = dbvar.cursor()
	print "Welcome to the office of Dr. Hooper"
	c=1
	while c==1:
		check = raw_input("Please enter your email ID: ")
		match = tablepointer.execute("select emailID from profile where emailID like (%s)", (check))
		print match
		data = tablepointer.fetchall()
		#print data
		m=1
		while m==1:
			if match:
				result=fetchCustData(check)
				print result
				m=m+1
				requestProcess(result)
			else:
				createNewProfile()

def createNewProfile():
	newCustomer = raw_input("Are you a new customer? please answer Yes/ No: ")
	if newCustomer == "Yes":
		#dbvar = MySQLdb.connect("localhost","root","admin","test")
		tablepointer = dbvar.cursor()
		tablepointer.execute("insert into profile (name,lastname,DOB,emailID,address,contactNo,emergencyContactName,emergencyContactNo) values (%s,%s,%s,%s,%s,%s,%s,%s)",(getName(),getlastName(),getdOb(),getemailId(),getAddress(),setContactNum(),setEnergencyContactName(),setEmergencyContactNo()))
		dbvar.commit()
		print "Thank you"
		result=getemailId()
		requestProcess(result) 
		
	elif newCustomer=="No": 
		findCust(check)
	elif newCustomer==' ':
		newCustomer = raw_input("Are you a new customer? please answer Yes/ No: ")
def getName():
	name = raw_input("Please enter your first name: ")
	while name=='':
		print "Can not lave the field blank"
		name = raw_input("Please enter your first name: ")
	else:
		return name


def getlastName():
	lastName = raw_input("Please enter your last name: ")
	while lastName=='':
		print "Can not lave the field blank"
		lastName = raw_input("Please enter your last name: ")
	else:
		return lastName
		

def getdOb():
	check = 1
	while(check == 1):
		dateInput = raw_input ("Please enter your date of birth in mm/dd/yyyy format: ")
		try:
			#myDate=validDate(dateInput)
			myDate=time.strptime(dateInput, '%m/%d/%Y')
			check = 0
		except ValueError:	
			print "invalid date"
			check=1
		else:
			bdate=dateInput.split('/')
			year= bdate[2]
			month=bdate[0]
			bd=bdate[1]
			year=int(year)
			month=int(month)
			bd=int(bd)
			#print year,month,bd
			birthdate = date(year, month, bd)		
			print birthdate
			return dateInput 
		
			
def	getemailId(): #email id becomes username
	check=1
	
	while check==1:
		email=raw_input("Please type in your e-mail ID: ")
		pt=re.compile('^[a-z|A-Z]+[a-z|A-z|0-9]+.*[a-z|A-Z|0-9]@[a-z|A-Z|0-9]+\.[com|biz|org|edu|co|au|uk]+$')
		result = pt.match(email)
		if(result):
			check=0
		else:
			print "Oops! Please enter an E-mail Id"
		
	return email	


def	getAddress():
	check=1
	while check==1:
		stAddress = raw_input("Please enter your street address: ")
		ptSt = re.compile('[0-9]+ \w+ \w+')
		result= ptSt.match(stAddress)
		if(result):
			check = 0
		else:
			print "Oops! invalid street address"
	
	c=1
	while c==1:
		city = raw_input("Please enter the name of city: ")
		ptCity= re.compile('^\w+$')
		resultCity = ptCity.match(city)
		if resultCity:
			c=0
		else:
			print "oops! invalid city name"
	
	z=1
	while z==1:
		Zip = raw_input("Please enter ZIP: ")
		ptZip = re.compile('^(0000[1-9]|000[1-9][0-9]|00[1-9][0-9][0-9]|0[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9])$')
		resultZip = ptZip.match(Zip)
		if resultZip:
			z=0
		else:
			print "Oops! invalid Zip"
	
	s=1
	while s==1:
		state = raw_input("Please enter state: ")
		ptState = re.compile('^[a-z|A-Z][a-z|A-Z]$')
		resultState = ptState.match(state)
		if resultState:
			s=0
		else:
			print "oops! invalid state"
	address = stAddress+city+Zip+state 
	return address	


def setContactNum():
	check=1
	while check==1 :
		contactNo = raw_input("Please enter your phone number starting with area code: ")
		pt = re.compile('^[1-9]\d{2}[1-9]\d{6}$')
		result = pt.match(contactNo)
		if result:
			check=0
		else:
			print "oops! invalid phone number."
	return contactNo

def setEnergencyContactName():
	c=1
	while c==1:
		emergencyContactName = raw_input("Please enter first name and last name of your emergency contact person: ")
		pt = re.compile('^\w+ \w+$')
		result = pt.match(emergencyContactName)
		if result:
			c=0
		else:
			print "oops! invalid person name"
	return emergencyContactName


def setEmergencyContactNo():
	check=1
	while check==1 :
		emergencyContactNo = raw_input("Please enter phone number for your emergency contact, starting with area code: ")
		pt = re.compile('^[1-9]\d{2}[1-9]\d{6}$')
		result = pt.match(emergencyContactNo)
		if result:
			check=0
		else:
			print "oops! invalid phone number."
	return emergencyContactNo



#dbvar = MySQLdb.connect("localhost","root","admin","test")
#tablepointer = dbvar.cursor()
#tablepointer.execute("insert into profile (name,lastname,DOB,emailID,address,contactNo,emergencyContactName,emergencyContactNo) values (%s,%s,%s,%s,%s,%s,%s,%s)",(getName(),getlastName(),getdOb(),getemailId(),getAddress(),setContactNum(),setEnergencyContactName(),setEmergencyContactNo()))
#dbvar.commit()
#tablepointer.execute("select * from logintable where username like 'venkat'")
#data = tablepointer.fetchall()
#print data		

check()

#getlastName()
#getdOb()
#getemailId()
#getAddress()	
#psWord
def createpsWord():
	num = random.random()
	num=num*1000000
	num=int(num)
	return num
createpsWord()
	
	
	
