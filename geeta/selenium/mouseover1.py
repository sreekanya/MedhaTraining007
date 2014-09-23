# to move mouse over dropdown menu then in menu find tools
import selenium
from selenium import webdriver
# for this importing 'actionchains' from selenium
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
try:
	br.find_element_by_link_text("Tools")
except:
	print "not able to find tools sub menu option"
else:
	print "able to find Tools sub menu"