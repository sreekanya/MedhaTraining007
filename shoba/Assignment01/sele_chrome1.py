import selenium 
from selenium import webdriver

def assertcheck(actual,expected):
	if(actual == expected):
		return True
	else:
		return False
		
fh=open("sele_chrom.csv",'r')

for i in fh:
	newi = i.rstrip()
	data=newi.split(',')    
#for j in data:
	print data[0],data[1],data [2],data[3],data[4]			

chrombr = webdriver.ChromeOptions()
chrombr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

br=webdriver.Chrome("C:\Users\Shoba\Downloads\chromedriver_win32\chromedriver.exe",chrome_options = chrombr)
br.get("http://bing.com")
br.implicitly_wait(10)

print "page title",br.title
pagetitle = br.title
print assertcheck("Bing",pagetitle)
pageName = br.find_element_by_name("q")
print "this is page name : ",pageName
pageId = br.find_element_by_id("sb_form_q")
print "this is page name : ",pageId
pageLtext = br.find_element_by_link_text("IMAGES")
print "this is page name : ",pageLtext
pageLtext2 = br.find_element_by_link_text("NEWS")
print "this is page name : ",pageLtext2
print assertcheck(data[1],pageName)
#PageID = br.id
#print PageID
br.close()