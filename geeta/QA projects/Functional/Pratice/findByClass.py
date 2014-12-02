# Script for finding Gmail hyperlink on google.com..using class_name
import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://google.com")
br.implicitly_wait(5)

try:
	gmaillink=br.find_element_by_class_name("gb_d")
except:
	print " not found"
else:
	print " able to find"
br.close()	
