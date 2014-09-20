#finding password on yahoo login page

import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://login.yahoo.com")
try:
	password=br.find_element_by_name("passwd")
except:
	print "not able to find password box"
else:
	print " able to find password box"
br.close()