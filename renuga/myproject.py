import sys
from selenium import webdriver
input=sys.argv
if (len(input)<1):
	print "please check number of inputs"
	sys.exit()
else :
	br=sys.argv[0]
	data=sys.argv[1]
	brw=webdriver.Firefox()
	brw.get(br)
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
opengmail()
	
	