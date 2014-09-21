import selenium 
from selenium import webdriver
# this action chain import is required to use mouse over functionality.

from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Firefox()
br.get("http://ubuntu.com")

try:
	cloudMenuElement = br.find_element_by_link_text("Cloud")
except:
	print "not able to find Menu item Cloud"
else: # Once after finding Element we are tring to move mouse to that element using ActionChain modules and functionality 
	actions = ActionChains(br)
	actions.move_to_element(cloudMenuElement)
	actions.perform()
	#br.implicitly_wait(20)

try:
	br.find_element_by_link_text("Tools")
except:
	print "not able to find Tools sub menu option"
else:
	print "able to find Tools sub menu option"