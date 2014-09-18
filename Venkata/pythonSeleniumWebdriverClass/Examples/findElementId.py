import selenium 

from selenium import webdriver


browser = webdriver.Firefox()
browser.get("https://login.yahoo.com")

#print "page getting loaded"

browser.implicitly_wait(30)

try:
	userName = browser.find_element_by_id("username")
except:
	print "not able to find user name element"
else:
	print "able to find user name"

browser.close()
