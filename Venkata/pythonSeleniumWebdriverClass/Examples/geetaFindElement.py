import selenium
from selenium import webdriver

import sys
testDataMap = {}
filename = sys.argv[1]
webpageURL = sys.argv[2]

## Function to read the csv content and create HashMap
def getInputData(filename):
  fh=open(filename,'r')
  for i in fh:
    i=i.rstrip()
    testdata = i.split(',')
    print testdata[0],testdata[1]
    testDataMap [testdata[0]]=testdata[1]
# following function is to findout element by id using browser object and id value
def testElementByID(browser,id):
  try:
    browser.find_element_by_id(id)
  except:
    print "not able to find ID ",id
  else:
    print "test case passed"
#
def testElementByName(browser,name):
  try:
    browser.find_element_by_name()
  except:
    print "not able to find name ",name
  else:
    print "test case passed"


getInputData(filename)
br = webdriver.Firefox()
br.get(webpageURL)

for eachdata in testDataMap.keys():
 if(eachdata=="id"):
  testElementByID(br,testDataMap[eachdata])
 else:
  testElementByName(br,testDataMap[eachdata])
atul.sathaye