#open yahoo loging page login and signout
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Firefox()
br.get("https://login.yahoo.com")

uname=br.find_element_by_id("username")
uname.send_keys("geeta_245")

password=br.find_element_by_id("passwd")
password.send_keys("Year1976")

signinbutton=br.find_element_by_id(".save")
signinbutton.click()	

br.implicitly_wait(20)
try:
	geeta=br.find_element_by_partial_link_text("Hi, Geeta")
except:
	print "not able to find"
else:
	actions=ActionChains(br)
	actions.move_to_element(geeta)
	actions.perform()
	
try:
	signout=br.find_element_by_link_text("Sign Out")
except:
	print "not able to find signout sub menu option"
else:
	print "able to find signout sub menu"
# signout is not working..
		