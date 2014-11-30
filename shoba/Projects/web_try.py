from selenium import webdriver
import sys
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/")
try:
	element= br.find_element_by_id("facebook")
except:
	print "unable to find the element title"
else:
	print ("able to find the element title ", title)
	print " tring to find title......"
	print element.title()