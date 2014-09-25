import selenium
from selenium import webdriver
import sys
testDataMap = {}
filename = sys.argv[1]
browserchoice = sys.argv[2]
webpageURL = sys.argv[3]

def chooseBrowser(browserType):
		if (browserType =="chrome"):
			chrombr = webdriver.ChromeOptions()
			chrombr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
			browser=webdriver.Chrome("C:\Users\Shoba\Downloads\chromedriver_win32\chromedriver.exe",chrome_options = chrombr)
			return browser
		else:
			browser = webdriver.Firefox()
			return browser
# Function to read the csv content and create HashMap

def getInputData(filename):
	fh=open(filename,'r')
	for i in fh:
		i=i.rstrip()  # my line is name,password
		testdata = i.split(',') # testdata[0] = name testdata[1]=password
		print testdata[0],testdata[1]
		testDataMap[testdata[0]]=testdata[1]# testDataMap["id"]="username" testDataMap["name"]="password"

# following function is to findout element by id using browser object and id value 

def testElementByID(browser,id):
	try:
		uName = browser.find_element_by_id(id)       #checking id by value ie for id is value "sb_form_q"
	except:
		print "not able to find ID ",id
	else:
		print "test case passed with id"
		uName.send_keys("shobasrinath.s")
		return True
#br.implicitly_wait(10)
# 
def testElementByPassword(browser,name):
	try:
		psWord = browser.find_element_by_name(name)
	except:
		print "not able to fine name ",name
	else:
		print "test case passed with name"
		psWord.send_keys("ssrinath18")
		return True
		
#br.implicitly_wait(10)		
def testElementByLinktext(browser,linktext):
	try:
		browser.find_element_by_link_text(linktext)
	except:
		print "not able to fine linktext ",linktext
	else:
		print "test case passed with linktext"
		
		
def testElementByIdSn(browser,submit):
	try:
		submitButton = browser.find_element_by_id(submit)
	except:
		print "not able to fine id for sign in",
	else:
		print "test case passed with Sign in",submit
		
			
getInputData(filename)
br=chooseBrowser(browserchoice)
br.get(webpageURL)
br.implicitly_wait(20)

for eachdata in testDataMap.keys():
	if(eachdata == "id"):
		testElementByID(br,testDataMap[eachdata])
		br.implicitly_wait(10)
	elif(eachdata == "name"):
		testElementByPassword(br,testDataMap[eachdata])
	elif(eachdata== "linktext"):
		testElementByLinktext(br,testDataMap[eachdata])
	elif(eachdata=="submit"):
		testElementByIdSn(br,testDataMap[eachdata])
	else:
		print "out of range"
if (testElementByID):
	if(testElementByPassword):
		submitButton = br.find_element_by_id("signIn")
		submitButton.click()

br.implicitly_wait(10)
br.close()
		