import re
import sys
import time
import calender
import datetime
from datetime import date
from datetime import datetime
import random
import MySQLdb
dbvar = MySQLdb.connect("localhost","root","admin","test")
tablepointer = dbvar.cursor()

def check():
	dbvar = MySQLdb.connect("localhost","root","admin","test")
	tablepointer = dbvar.cursor()
	print "Welcome to the office Dr. Hooper"
	c=1
	while c==1:
		check = raw_input("Please enter your email ID: ")
		match = tablepointer.execute("select emailID from profile where emailID like (%s)", (check))
		print match
		data = tablepointer.fetchall()
		if match:
			action = raw_input("Do you want to schedule a new appointment or reschedule or cancel existing appointment?: ")
			#while :
			#	pass
			
		else:
			createNewProfile()
			c=0	
	else:
		findCust()

def scheduleRequest():
	pass

def requestProcess():
	action = raw_input("Do you want to schedule a new appointment or reschedule or cancel existing appointment?: ")
	c=0
	while action!= '':
		if action=="schedule":

			pass
		elif action=="reschedule":
			pass
		elif action == "cancel":
			pass
	else:
		pass


def validDate(dateInput):
	dateprocess = datetime.strptime(dateInput, '%m/%d/%Y').date()
	makeDate = dateprocess.date()
	print makeDate
	return makeDate

def findCust():
	dateInput =  raw_input("Please enter your date of birth: ")
	validDate(dateInput)
	#bdate=findbyDOB.split('/')
	#year= bdate[2]
	#month=bdate[0]
	#bd=bdate[1]				
	#year=int(year)
	#month=int(month)
	#bd=int(bd)
	#birthdate = date(year, month, bd)
	#print birthdate	
	match = tablepointer.execute("select DOB from profile where DOB like (%s)", (makeDate))
	if match:
		verifyName = raw_input("Please enter your name: ")
		splitName= verifyName.split(' ')
		#splitName= str(splitName[0])+' ' + str(splitName[1])
		#print splitName
	 	matchName = tablepointer.execute("select name from profile where name like (%s)", (splitName[0]))
	 	if matchName:
	 		print "We found you."
	 		tablepointer.execute("select * from profile where DOB like (%s)",(birthdate))
	 		data = tablepointer.fetchall()
	 		print data
	 	else:
	 		print "We are sorry. We are unable to find your record."
	 		createNewProfile()


	else:	
		print ("Your birthdate does not match with our record. You need to create a new profile.")
		createNewProfile()

def createNewProfile():
	newCustomer = raw_input("Are you a new customer? please answer Yes/ No: ")
	if newCustomer == "Yes":
		#dbvar = MySQLdb.connect("localhost","root","admin","test")
		tablepointer = dbvar.cursor()
		tablepointer.execute("insert into profile (name,lastname,DOB,emailID,address,contactNo,emergencyContactName,emergencyContactNo) values (%s,%s,%s,%s,%s,%s,%s,%s)",(getName(),getlastName(),getdOb(),getemailId(),getAddress(),setContactNum(),setEnergencyContactName(),setEmergencyContactNo()))
		dbvar.commit()
		
	elif newCustomer=="No" or newCustomer=='':
		print ("Thanks for your time.")
		sys.quit()
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
		dt = raw_input ("Please enter your date of birth in mm/dd/yyyy format: ")
		try:
			validDate=time.strptime(dt, '%m/%d/%Y')
			check = 0
		except ValueError:	
			print "invalid date"
		else:
			bdate=dt.split('/')
			year= bdate[2]
			month=bdate[0]
			bd=bdate[1]
			year=int(year)
			month=int(month)
			bd=int(bd)
			print year,month,bd
			birthdate = date(year, month, bd)		
			print birthdate
			return birthdate
		
			
def	getemailId(): #email id becomes username
	check=1
	
	while check==1:
		email=raw_input("Please type in your e-mail ID: ")
		pt=re.compile('^[a-z|A-Z]+[a-z|A-z|0-9]+\.*[a-z|A-Z|0-9]@[a-z|A-Z|0-9]+\.[com|biz|org|edu|co|au|uk]+$')
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
		emergencyContactName = raw_input("Please enter the name of your emergency contact person: ")
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
	
	
	
