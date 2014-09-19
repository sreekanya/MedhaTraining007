#this file opens chrome and supposed to go to targeted web site(login.yahoo.com)
#but does not opens yahoo login page and yet gives positive results. when tried #to print title it is not able to print title of page as yahoo login page. Don't #know what's going on.



import selenium
from selenium import webdriver
chromebr = webdriver.ChromeOptions()


br= webdriver.Chrome("C:\Users\himangi\work\pyth\chromedriver.exe", chrome_options = chromebr)
br.get=("https://login.yahoo.com")
#browser= webdriver.Firefox()
#browser.get("https://login.yahoo.com")
fileHandle = open('tstCase1.csv','r')

br.implicitly_wait(10)
for i in fileHandle:
    myList = i.split(',')
    for i in range(1,len(myList)):
       
        try:
            print br.title
            a = "find_element_by_" 
       
            elements = "browser." + a + myList[0] + "(" + myList[1] + ")" 
            #eval(elements)
          
        
        except:
            print "not able to find ",myList[0],myList[1]
           
        else:
            print "able to find ",myList[0],myList[1]
          

br.close()        
