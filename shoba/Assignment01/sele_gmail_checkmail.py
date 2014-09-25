import selenium 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Firefox()
br.get("http://gmail.com")


try:
	uName = br.find_element_by_id("Email")       #checking id by value ie for id is value "sb_form_q"
except:
	print "not able to find ID ",id
else:
	print "test case passed with id"
	uName.send_keys("shobasrinath.s")
	
br.implicitly_wait(10)

try:
	psWord = br.find_element_by_name("Passwd")
except:
	print "not able to fine name ",name
else:
	print "test case passed with name"
	psWord.send_keys("ssrinath18")
		

try:
	submitButton = br.find_element_by_id("signIn")
except:
	print "not able to fine id for sign in",
else:
	print "test case passed with Sign in",submitButton
br.implicitly_wait(20)
submitButton = br.find_element_by_id("signIn")
submitButton.click()


try:
	inboxElement = br.find_element_by_xpath(".//*[@id=':72']/div/div[1]")
	 
except:
	print "unable to find theInbox element"
else:
	print inboxElement
	action = ActionChains(br) #is a ActionChain is a class or module or function that carries all the function of mouse movement	
	action.move_to_element(inboxElement)
	br.implicitly_wait(10)
	inboxElement.click()
	#mailName= find_element_by_xpath(".//*[@id=':3m']")
try:
	mailName = br.find_element_by_xpath(".//*[@id=':3m']/span")
	 
except:
	print "unable to find mailName element"
else:
	print mailName
	action = ActionChains(br) #is a ActionChain is a class or module or function that carries all the function of mouse movement	
	action.move_to_element(mailName)
	br.implicitly_wait(10)	
	mailName.click()
try:
	replyElement = br.find_element_by_xpath(".//*[@id=':dk']/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[4]/div[1]")
	 
except:
	print "unable to find the reply element"
else:
	print replyElement
	action = ActionChains(br) #is a ActionChain is a class or module or function that carries all the function of mouse movement	
	action.move_to_element(replyElement)
	br.implicitly_wait(10)
	
	replyElement.click()
try:
	typeElement = br.find_element_by_xpath(".//*[@id=':jj']")
except:
	print "unable to find send element"
else:
	print typeElement
	action = ActionChains(br) #is a ActionChain is a class or module or function that carries all the function of mouse movement			action.move_to_element(sendElement)
	action.move_to_element(typeElement)
	typeElement.send_keys("hello")
	br.implicitly_wait(10)
try:
	sendElement = br.find_element_by_xpath(".//*[@id=':ha']")
except:
	print "unable to find send element"
else:
	print "its send button ",sendElement
	
sendElement = br.find_element_by_xpath(".//*[@id=':i2']")
sendElement.click()	
#br.close()	