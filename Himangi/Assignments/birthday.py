import sys
import re
import datetime
from datetime import date
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

global_greetings = "greetings.csv"

def today():
	today = date.today()
	month = today.month
	day = today.day
	dat = str(month)+'-'+ str(day)
	return dat

br = webdriver.Firefox()
br.get("https://gmail.com")	
def login(br):
    try:
        uname=br.find_element_by_id("Email")
    except:
        print "not able to find the field"
    else:
        uname.send_keys("pythonclass14")
    try:
        pwd=br.find_element_by_id("Passwd")
    except:
        print "not able to find the field", pwd
    else:
        pwd.send_keys("python2014")

    getbut = br.find_element_by_id("signIn")
    getbut.click()
    br.implicitly_wait(15)

#login(br)
def greet():
	fh=open(global_greetings,'r')
	message = fh.read()
	return message


def composeMail(myEmail,myName):

	try:
		composeLink=br.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div")
	except:
		print "not able to find compose link"
	else:
		composeLink.click()
	try:
		emailInput= br.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div/table/tbody/tr/td[2]/div/div/textarea")
	except:
		print "Not able to find email Input"
	else:
		emailInput.send_keys(myEmail)
	try:
		subject= br.find_element_by_name("subjectbox")
	except:
		print "Not able to find subject Input"
	else:
		subject.send_keys("Happy Birthday")
	try:
		textarea = br.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/div[2]/div/div/table/tbody/tr/td[2]/div[2]/div/iframe")
	except:
		print "No textarea found"
	else:
		textarea.send_keys(myName[0].upper()+myName[1:len(myName)])
		textarea.send_keys(greet())
	try:
		send = br.find_element_by_xpath("/html/body/div[13]/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td/div/div[2]")

	except:
		print "No send button"
		
	else:
		send.click()

	


#composeMail()
birthdayMap={}
#getDt=raw_input("Please enter your birth date in mm-yy format: ")
def getBirthdate():
	logincnt = 0
	fh=open("birthday.csv",'r')
	
	for i in fh:
		i=i.rstrip()
		friendInfo= i.split(',')
		birthdayMap[friendInfo[1]]=(friendInfo[0],friendInfo[2])
		#print birthdayMap.values
		greet=0

		if(friendInfo[2]==today()):
			myEmail=friendInfo[1]
			myName=friendInfo[0]
			print myEmail
			if(logincnt == 0):	
				login(br)
				logincnt = 1
			composeMail(myEmail,myName)
			greet=1
		else:
			print "No birthday today"
			greet=0
	
getBirthdate()
def signout():
	try:
		signoutElement = br.find_element_by_partial_link_text("pythonclass14@gmail.com")
		
	except:
		print "i am here"
		print "not able to find Menu item sign out"
	else: # Once after finding Element we are tring to move mouse to that element using ActionChain modules and functionality
		signoutElement.click()
	try:
		signoutBut= br.find_element_by_id("gb_71")
	except:
		print "No element found"
	else:
		signoutBut.click()

signout()



























	#details=birthdayMap.values()
	
	
	

	#if dat==bday:
	#		pickEmail=birthdayMap[1]
	#			print pickEmail, bday 
	#else:
	#	print "nobody's birthday today"

	#print i
	#i= i.rstrip()
	#eachInfo=birthdayMap[i].split(',')
	#print eachInfo
#pattern= re.compile('[-\/]')
#getDt= re.sub(pattern, ',', getDt)
#myDate=getDt.split(',')
#birthday = myDate[1]+'/'+myDate[2]
#print getDt
#if(dat == birthday):
#	print"Happy Birthday!"
#else:
#	print "oops! not your birthday"
