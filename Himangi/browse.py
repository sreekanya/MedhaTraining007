import selenium #some changes
from selenium import webdriver #some more changes 

br = webdriver.Firefox()
br.get("http://cadence.com")
myList = br.find_elements_by_tag_name("div")
#elem = br.find_div("div")
#print elem
print len(myList)
print myList[100].id

