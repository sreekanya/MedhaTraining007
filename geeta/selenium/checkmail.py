#open yahoo login page, login find mail on left side and click on it.
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

#now to find mail option on left side and click to check mail
try:
	chmail=br.find_element_by_id("nav-mail")
except:
	print"not able to find mail check option on left side "
else:
	actions=ActionChains(br)
	actions.move_to_element(chmail)
	actions.perform()
	chmail.click()