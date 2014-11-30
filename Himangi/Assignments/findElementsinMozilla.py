import selenium
from selenium import webdriver
browser= webdriver.Firefox()
browser.get("https://login.yahoo.com")
fileHandle = open('tstCase1.csv','r')

browser.implicitly_wait(5)
for i in fileHandle:
    myList = i.split(',')
    for i in range(1,len(myList)):
       
        try:
            print browser.title
            
            a = "find_element_by_" 
       
            elements = "browser." + a + myList[0] + "(" + myList[1] + ")" 
            #eval(elements)
          
        
        except:
            print "not able to find ",myList[0],myList[1]
           
        else:
            print "able to find ",myList[0],myList[1]
          
browser.close()
        
