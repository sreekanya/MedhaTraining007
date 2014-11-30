from selenium import webdriver
import sys
testDataMap = {}
browserchoice = sys.argv[1]
webpageURL = sys.argv[2]
filename = sys.argv[3]
#filename2 = sys.argv[4]


            

def chooseBrowser(browserType):
        if (browserType =="chrome"):
            chrombr = webdriver.ChromeOptions()
            chrombr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            browser=webdriver.Chrome("C:\Users\Shoba\Downloads\chromedriver_win32\chromedriver.exe",chrome_options = chrombr)
            return browser
        else:
            browser = webdriver.Firefox()
            return browser
            
br=chooseBrowser(browserchoice)
br.get(webpageURL)

# following function is to findout element by id using browser object and id value 

def testElementBytitle(br,v1):
    try:
        title= br.find_element_by_link_text(v1)
    except:
        print "unable to find the element title"
    else:
        print ("able to find the element title ", title)
        return True
        br.implicitly_wait(10)
def testElementByusername(br,v2):
    try:
        uname= br.find_element_by_id(v3)
    except:
        print "unable to find the element username"
    else:
        print ("able to find the element username ", uname)
        uname.send_keys("pythonclass14@gmail.com")
        return True
        br.implicitly_wait(10)

def testElementBypassword(br,v3):
    
    try:
        password= br.find_element_by_id("pass")
    except:
        print "unable to find the element password"
    else:
        print ("able to find the element password ", password)
        password.send_keys("python2014")
        return True
        
        br.implicitly_wait(10)        
        
def testElementBysignbutton(br,v4):
    try:
        login= br.find_element_by_id("u_0_n")
    except:
        print "unable to find the element id "
    else:
        print ("able to find the element login button ", login)
        login.click()
        
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
        if eachdata=="linktext":
            v1=testDataMap[eachdata]
            print v1
            testElementBytitle(br,v1)
            br.implicitly_wait(10)
        elif eachdata=="id":
            print eachdata
            v2=testDataMap[eachdata]
            print v2
            testElementByusername(br,v2)
        elif eachdata=="password":
            print eachdata
            v3=testDataMap[eachdata]
            print v3
            testElementBypassword(br,v3)
        elif eachdata=="linktext":
            print eachdata
            v4=testDataMap[eachdata]
            print v4
            testElementBysignbutton(br,v4)
        else:
            print "no match"

        br.implicitly_wait(10)
getInputData(filename)        

def testElementBylogo(br,v5):
    try:
        logo= br.find_element_by_xpath(v5)
    except:
        print "unable to find the element logo"
    else:
        print ("able to find the element logo ", logo)
        return True
        br.implicitly_wait(10)
def testElementBysearchtab(br,v6):
    try:
        searchtab= br.find_element_by_xpath(v6)
    except:
        print "unable to find the element searchtab"
    else:
        print ("able to find the element searchtab ", searchtab)
        return True
        br.implicitly_wait(10)

def testElementByhomelink(br,v7):
    
    try:
        homelink= br.find_element_by_id(v7)
    except:
        print "unable to find the element homelink"
    else:
        print ("able to find the element homelink ",homelink)
        return True
        
        br.implicitly_wait(10)        
        
def testElementByanchor(br,v8):
    try:
        anchor= br.find_element_by_id(v8)
    except:
        print "unable to find the element anchor "
    else:
        print ("able to find the element anchor ", anchor)
        login.click()
        
def testElementBylogout(br,v8):
    try:
        logout= br.find_element_by_id(v8)
    except:
        print "unable to find the element logout "
    else:
        print ("able to find the element logout ", logout)
        logout.click()
                
testDataMap2={}

# Function to read the csv content and create HashMap

def getInputData(filename2):
    fh=open('facebook2.csv','r')
    for i in fh:
        i=i.rstrip()  # my line is name,password
        testdata = i.split(',')
        print testdata[0],testdata[1]
        testDataMap2[testdata[0]]=testdata[1]# testDataMap2["id"]="username" testDataMap2["name"]="password"
    for eachdata in testDataMap2.keys():
        if eachdata=="loggenin_logo":
            v5=testDataMap2[eachdata]
            print v5
            testElementBylogo(br,v5)
            br.implicitly_wait(10)
        elif eachdata=="search_tab":
            v6=testDataMap2[eachdata]
            print v6
            testElementBysearchtab(br,v6)
        elif eachdata=="home_link":
            v7=testDataMap2[eachdata]
            print v7
            testElementByhomelink(br,v7)
        elif eachdata=="anchor_logout":
            print eachdata
            v8=testDataMap2[eachdata]
            print v8
            testElementByanchor(br,v8)
        elif eachdata=="logout_button":
            print eachdata
            v9=testDataMap2[eachdata]
            print v9
            testElementBylogout(br,v9)
        else:
            print "no match"

        br.implicitly_wait(10)
        br.close()
        

#getInputData(filename2)
