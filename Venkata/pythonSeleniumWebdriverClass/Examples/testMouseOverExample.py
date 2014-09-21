import selenium 
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Firefox()
br.get("http://ubuntu.com")
try:
	cloudMenuElement = br.find_element_by_link_text("Cloud")
except:
	print "not able to find Menu item Cloud"
else: 
	actions = ActionChains(br)
	actions.move_to_element(cloudMenuElement)
	actions.perform()

