import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://login.yahoo.com")
br.implicitly_wait(6)
try:

	username=br.find_element_by_tag_name("input")
except:
	print"not able to find"
else:

	print "able to find"
br.close()
