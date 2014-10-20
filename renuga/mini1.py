from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
current=time.strftime("%m/%d")
file=open("mini1.csv",'r')
print "Todays date is" + current
br=webdriver.Firefox()
br.get("http://gmail.com")
br.maximize_window()
def opengmail():
	el=br.find_element_by_id("Email")
	el.send_keys("renu1suresh")
	pawd=br.find_element_by_id("Passwd")
	pawd.send_keys("$urmohit1")
	check=br.find_element_by_id("PersistentCookie")
	check.click()
	button=br.find_element_by_id("signIn")
	button.click()
	br.implicitly_wait(20)
def sendmail():
	for line in file:
		line=line.rstrip()
		data=line.split(',')
		if (current==data[1]):
			print "Happy birthday"+data[0]
			try:
				br.switch_to_frame("canvas_frame")
				cmp=br.find_element_by_css_selector("div[class='T-I J-J5-Ji T-I-KE L3']")
				cmp.click()
				br.implicitly_wait(30)
				toadd=br.find_element_by_name("to")
				toadd.send_keys(data[2])
				subject=br.find_element_by_name("subjectbox")
				subject.send_keys("Birthday message")
				msg=br.find_element_by_tag_name("body")
				msg.click()
				msg.send_keys("Many more")
			except:
				print "element found"
			else:
				print "element not found"
opengmail()
sendmail()

