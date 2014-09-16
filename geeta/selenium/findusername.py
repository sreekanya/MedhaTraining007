# finding username in yahoologin page

import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://login.yahoo.com")
br.implicitly_wait(10)

try:
	username=br.find_elemet_by_id("username")
except:
	print "username not found on login page"
else:
	print "able to find username"
br.close()

# result is username not found
	
	
