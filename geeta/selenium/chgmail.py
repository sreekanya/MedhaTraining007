# open gmail check received  mail from geeta Patil,open reply

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Firefox()
br.get("https://gmail.com")

uname=br.find_element_by_id("Email")
uname.send_keys("pythonclass14")

password=br.find_element_by_id("Passwd")
password.send_keys("python2014")

signinbutton=br.find_element_by_id("signIn")
signinbutton.click()	

br.implicitly_wait(20)

# to find mail from geeta patil
try:
	geetamail= br.find_elements_by_name("Geeta Patil")
except:
	print "Not found any mail from geeta"
else:
	br.implicitly_wait(10)
	geetamail[1].click()#need to understand why[1]
	br.implicitly_wait(15)

	
# locating reply button
	
	
try:
	replybutton=br.find_element_by_xpath("//*[@id=":qa"]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[4]/div[1]")
except:
	print" not able to see area to write"
else:
	print"found it"
# not able to give xpath