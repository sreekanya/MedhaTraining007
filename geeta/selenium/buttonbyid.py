# finding google search button in google.com...by_id
import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get("https://google.com")

try:
	searchbutton=br.find_elemnt_by_id("gbqfba")
except:
	print"not able to find"
else:
	print"able to find"
br.close()

# need to check why not working for id
