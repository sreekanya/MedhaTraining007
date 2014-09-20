import selenium 
from selenium import webdriver

br = webdriver.Firefox()
br.get("https://login.yahoo.com")

br.implicitly_wait(5)

try:
	userName = br.find_element_by_name("login")
except: 
	print "not able to find element"
else:
	print "able to find element",userName