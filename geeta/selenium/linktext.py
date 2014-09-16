# trial for....Gmail hyperlink on google.com..using id it works
import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://google.com")
br.implicitly_wait(5)

try:
	gmaillink=br.find_element_by_id("gsr")
except:
	print " not found"
else:
	print " able to find"
	