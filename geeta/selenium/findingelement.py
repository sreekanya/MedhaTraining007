import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://login.yahoo.com")

br.implicitly_wait(5)
try:
	signinButton=br.find_element_by_name(".save")
except:
	print"not able to find"
else:
	print"able to find"
