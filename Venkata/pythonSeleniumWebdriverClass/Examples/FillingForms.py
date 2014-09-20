import selenium 
from selenium import webdriver

import sys 

browserselection = sys.argv[1]

def getBrowser(browserType):
	if(browserType=="chrome"):
		chromebr = webdriver.ChromeOptions()
		chromebr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		browser = webdriver.Chrome("C:\Users\Venkata\Documents\workspace\chromedriver_win32\chromedriver.exe",chrome_options=chromebr)
	else:
		browser = webdriver.Firefox()
	return browser

br = getBrowser(browserselection)

br.get("https://mail.yahoo.com")

br.implicitly_wait(10)   # I am trying to wait for page to load for 10second to make sure all the elements are loadded

try:
	uname = br.find_element_by_id("username")
except:
	print "not able to find user name filed"
else:
	uname.send_keys("naninice2000")


signinbutton  = br.find_element_by_id(".save")
signinbutton.click()

pageHTMLSource = br.page_source

if ("Please enter your password" in pageHTMLSource):
	print "Error message present"
else:
	print "No Error message "

