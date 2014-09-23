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
#now find inbox and click to open inbox
br.implicitly_wait(10)
try:
	chinbox=br.find_element_partial_link_text("Inbox")
except:
	print"not able to find inbox option on left side"
else:
	actions=ActionChains(br)
	actions.move_to_element(chinbox)
	actions.perform()
	chinbox.click()
# not able to find inbox,tried with link text,partial link text

br.implicitly_wait(5)
try:
	geetamail=br.find_element_by_name("Geeta Patil")
except:
	print"not able to find mail from geeta patil"
else:
	br.implicitly_wait(10)
	
	geetapatil[1].click()
# not checking finding mail from geeta patil
	


