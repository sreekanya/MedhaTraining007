from selenium import webdriver
import sys
testDataMap = {}
filename = sys.argv[1]
webpageURL = sys.argv[2]



			

def chooseBrowser(browserType):
		if (browserType =="chrome"):
			chrombr = webdriver.ChromeOptions()
			chrombr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
			browser=webdriver.Chrome("C:\Users\Shoba\Downloads\chromedriver_win32\chromedriver.exe",chrome_options = chrombr)
			return browser
		else:
			browser = webdriver.Firefox()
			return browser
browserchoice = sys.argv[3]			
br=chooseBrowser(browserchoice)
br.get(webpageURL)

# following function is to findout element by id using browser object and id value 

def testElementBytitle(br,v1):
	try:
		element= br.find_element_by_xpath()
	except:
		print "unable to find the element title"
	else:
		print ("able to find the element title ", title)
		print element.title
		br.implicitly_wait(10)
def testElementByusername(br,v2):
	try:
		uname= br.find_element_by_xpath(v2)
	except:
		print "unable to find the element title"
	else:
		print ("able to find the element title ", title)
		uname.send_keys("shobasrinath6@gmail.com")
		br.implicitly_wait(10)

def testElementBypassword(br,v3):
	
	try:
		password= br.find_element_by_id(v3)
	except:
		print "unable to find the element password"
	else:
		print ("able to find the element password ", password)
		password.send_keys("learn123")
		return True
		
		br.implicitly_wait(10)		
		
def testElementBysignbutton(br,v4):
	try:
		login= br.find_element_by_id(v4)
	except:
		print "unable to find the element id "
	else:
		print ("able to find the element login button ", login)
		#login.click()
		
testDataMap={}

# Function to read the csv content and create HashMap

def getInputData(filename):
	fh=open(filename,'r')
	for i in fh:
		i=i.rstrip()  # my line is name,password
		testdata = i.split(',')
		print testdata[0],testdata[1]
		testDataMap[testdata[0]]=testdata[1]# testDataMap["id"]="username" testDataMap["name"]="password"
	for eachdata in testDataMap.keys():
		if eachdata=="class":
			v1=testDataMap[eachdata]
			print v1
			testElementBytitle(br,v1)
			br.implicitly_wait(10)
		if eachdata=="id":
			print eachdata
			v2=testDataMap[eachdata]
			print v2
			testElementByusername(br,v2)
		if eachdata=="password":
			print eachdata
			v3=testDataMap[eachdata]
			print v3
			testElementBypassword(br,v3)
		if eachdata=="singin":
			print eachdata
			v4=testDataMap[eachdata]
			print v4
			testElementBysignbutton(br,v4)


			br.implicitly_wait(10)
			#br.close()
		

getInputData(filename)

		