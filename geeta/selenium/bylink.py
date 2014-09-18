# finding Help by using by link_text
# link text means the actual text displayed on page for that particular link
import selenium
from selenium import webdriver
br=webdriver.Firefox()
br.get('https://login.yahoo.com')
br.implicitly_wait(8)
try:
	fb=br.find_element_by_link_text("Facebook")
except:
	print"not able to find facebook on page"
else:
	print"able to find facebook link on yahoo login page"
br.close()
	