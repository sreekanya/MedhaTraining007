# finding help hyperlink 

import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://login.yahoo.com")
br.implicitly_wait(5)
try:
	help=br.find_element_by_link_text("yucs-help_link")
except:
	print "not able to find help hyperlink"
	
else:
	print "able to find"
br.close()
	
