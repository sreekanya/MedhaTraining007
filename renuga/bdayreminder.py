from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
current=time.strftime("%m/%d")
file=open("mini1.csv",'r')
print "Todays date is" + current
br=webdriver.Firefox()
br.get("http://gmail.com")
br.maximize_window()
today={}

def opengmail():
	el=br.find_element_by_id("Email")
	el.send_keys("*****")
	pawd=br.find_element_by_id("Passwd")
	pawd.send_keys("*****")
	check=br.find_element_by_id("PersistentCookie")
	check.click()
	button=br.find_element_by_id("signIn")
	button.click()
	br.implicitly_wait(20)
def compare():
	print "Birthday list with mailid"
	for ln in file:
		ln=ln.rstrip()
		day=ln.split(',')
		if (current==day[1]):
			today[day[0]]=day[2]
	print today
	print "Sending mail to ids in dictionary"
	return today
			
def sendmail(today):
	for key in today:
		print "Happy birthday"+key
		try:
			cmp=br.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div")
			cmp.click()
		except:
			print "Compose not found"
		try:
			br.implicitly_wait(30)
			toadd=br.find_element_by_name("to")
			toadd.send_keys(today[key])
			subject=br.find_element_by_name("subjectbox")
			subject.send_keys("Happy birthday"+key)
				
		except:
			print "sub not found"
		try:
			msg=br.find_element_by_css_selector("div[class='Am Al editable LW-avf']")
			msg.send_keys("Many more happy returns of the day")
		except:
			print "No Message found"
				
		try:
			#msg.send_keys("Mohit")
			br.implicitly_wait(20)
			sen=br.find_element_by_css_selector("div[class='T-I J-J5-Ji aoO T-I-atl L3']")
			sen.click()
		except:
			print "element not found"
		else:
				print "element found"
		br.implicitly_wait(30)
		print "Mail sent sucessfully"

compare()
opengmail()
br.implicitly_wait(30)
sendmail(today)

