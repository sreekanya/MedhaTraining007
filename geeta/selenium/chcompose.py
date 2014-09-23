# login inside yahoo mail,find compose click on it.
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
# now find mail link and click on it
try:
	chmail=br.find_element_by_id("nav-mail")
except:
	print"not able to find mail check option on left side "
else:
	actions=ActionChains(br)
	actions.move_to_element(chmail)
	actions.perform()
	chmail.click()
br.implicitly_wait(10)
# now find compose and click
try:
	chcompose=br.find_element_by_link_text("Compose")
except:
	print"not able to locate compose"
else:
	br.implicitly_wait(10)
	actions=ActionChain(br)
	actions.move_to_element(chcompose)
	actions.perform()
	chcompose.click()
# not working...not able to find compose
	