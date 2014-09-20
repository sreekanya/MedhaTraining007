import selenium 
from selenium import webdriver

import sys 

browserselection = sys.argv[1]

# this function will take the browser type and return the browser object based on browser selection

def getBrowser(browserType):
	if(browserType=="chrome"):
		chromebr = webdriver.ChromeOptions()
		chromebr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		browser = webdriver.Chrome("C:\Users\Venkata\Documents\workspace\chromedriver_win32\chromedriver.exe",chrome_options=chromebr)
	else:
		browser = webdriver.Firefox()
	return browser

br = getBrowser(browserselection) # trying to open the browser based on user selection in commond line
br.get("https://mail.yahoo.com")   
br.implicitly_wait(10)   # I am trying to wait for page to load for 10second to make sure all the elements are loadded


# trying to find user name element and enter user name into username filed
try:
	uname = br.find_element_by_id("username")
except:
	print "not able to find user name filed"
else:
	uname.send_keys("naninice2000")

# Clicking on signin button without entering password so that we can get error message.

signinbutton  = br.find_element_by_id(".save")
signinbutton.click()

# getting the page source and then finding specific text inside that page source

pageHTMLSource = br.page_source

if ("Please enter your password" in pageHTMLSource):
	print "Error message present"
else:
	print "No Error message "

