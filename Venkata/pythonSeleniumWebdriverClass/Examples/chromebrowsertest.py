import selenium 
from selenium import webdriver


def assertCheck(actual, expected):
	if(actual == expected):
		print "Test Case passing getting expected result"
		return True;
	else:
		print "Test Case Failed not gettng expected result"
		return False;


chromebr = webdriver.ChromeOptions()
chromebr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# Chrome brower need driver information to open the chrome browser ChromeOptions we are not setting any path for chrome browser 
# installed location it is going to take default location where chrome is installed from system path, nut it's always recommonded 
# to give chrome browser installation location through ChromeOptions. 

br = webdriver.Chrome("C:\Users\Venkata\Documents\workspace\chromedriver_win32\chromedriver.exe",chrome_options=chromebr)
br.get("https://bing.com")


br.implicitly_wait(10)
print "Page title is ",br.title
pagetitle = br.title

print assertCheck("Bing",pagetitle)
