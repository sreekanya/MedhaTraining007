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
