# find google search on google.com

import selenium
from selenium import webdriver
browser=webdriver.Firefox()
browser.get("http://google.com")
try:
	googlesearch=browser.find_element_by_name("btnK")
except:
	print "not able to find googlesearch"
else:
	print "able to find"
	
