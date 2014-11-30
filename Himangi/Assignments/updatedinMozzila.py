
import sys


filename = sys.argv[1]
webpageURL = sys.argv[2]
browserType= sys.argv[3] 
import selenium
from selenium import webdriver
testDataMap = {}
def getBrowser(browserType):
    if(browserType=="chrome"):
        chromebr=webdriver.ChromeOptions()
        browser= webdriver.Chrome("C:\Users\himangi\work\pyth\chromedriver.exe", chrome_options = chromebr)

        return browser
    else:
        browser=webdriver.Firefox()
        return browser
br = getBrowser(browserType)

br.get(webpageURL)

## Function to read the csv content and create HashMap

def getInputData(filename):
    fh=open(filename,'r')
    for i in fh:
        i=i.rstrip()
        testdata = i.split(',')
     	testDataMap[testdata[0]]=testdata[1]

# following function is to findout element by id using browser object and id value

def testElementByID(browser,id):
    try:
        browser.find_elements_by_id(id)
    except:
        print "not able to find ID ",id
    else:
        print "test case passed", id

#
def testElementByName(browser,name):
    try:
        browser.find_elements_by_name(name)
    except:
        print "not able to find name ",name
    else:
        print "test case passed", name

def testElementByLinkText(browser,linktext):
    try:
        browser.find_elements_by_link_text(linktext)
    except:
        print "not able to find link text ",linktext
    else:
        print "test case passed", linktext

def testElementByClassName(browser,classname):
    try:
        browser.find_element_by_class_name(classname)
    except:
        print "not able to find class name ",classname
    else:
        print "test case passed", classname

def testElementByxPath(browser,xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except:
        print "not able to find xpath ",xpath
    else:
        print "test case passed", xpath


getInputData(filename)

#br = webdriver.Firefox()
#br.get(webpageURL)

for eachdata in testDataMap.keys():
    print eachdata
    if(eachdata== "id"):
        testElementByID(br,testDataMap[eachdata])
    elif(eachdata== "name"):
        testElementByName(br,testDataMap[eachdata])
    elif(eachdata== "linktext"):
        testElementByLinkText(br,testDataMap[eachdata])
    elif(eachdata== "classname"):
        testElementByClassName(br,testDataMap[eachdata])
    elif(eachdata== "xpath"):
        testElementByxPath(br,testDataMap[eachdata])
    else:
        print "element not defined"

br.close()
