import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Firefox()

br.get("https://gmail.com")
try:
    uname=br.find_element_by_id("Email")
except:
    print "not able to find the field"
else:
    uname.send_keys("pythonclass14")
try:
    pwd=br.find_element_by_id("Passwd")
except:
    print "not able to find the field", pwd
else:
    pwd.send_keys("python2014")

getbut = br.find_element_by_id("signIn")
getbut.click()
br.implicitly_wait(15)
#try:
#    signoutElement = br.find_element_by_partial_link_text("pythonclass14@gmail.com")
   
#except:
#    print "i am here"
#    print "not able to find Menu item sign out"
#else: # Once after finding Element we are tring to move mouse to that element using ActionChain modules and functionality
#     signoutElement.click()
br.implicitly_wait(15)

try:
    inboxBut= br.find_elements_by_name("Himangi Sathaye")
except:
    print "No sender found"
else:
    br.implicitly_wait(10)
    inboxBut[1].click()
    br.implicitly_wait(15)
try:
    replyBut= br.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/table/tr/td/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/table/tbody/tr/td[2]/div/div/span")
except:
    print "No sender found"
else:

    #print replyBut
    replyBut.click()

try:
    br.implicitly_wait(30)
    writeInput= br.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/table/tr/td/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr/td/div/div[2]/div/div/table/tbody/tr/td[2]/div[2]/div/iframe")
except:
    print "No writing field found"
else:
   
    br.implicitly_wait(25)
    #print writeInput
    writeInput.send_keys("Hi there")
    

try:
    br.implicitly_wait(30)
    sendBut= br.find_element_by_class_name("T-I J-J5-Ji aoO T-I-atl L3 T-I-JO T-I-Zf-aw2")
                                     
except:
    print "No button found"
else:
    br.implicitly_wait(20)
    sendBut.click()
   
#try:
 #   signoutBut= br.find_element_by_id("gb_71")
#except:
 #   print "No element found"
#else:
 #   signoutBut.click()

#try:
 #   signoutElement = br.find_element_by_partial_link_text("pythonclass14@gmail.com")
   
#except:
 #   print "i am here"
  #  print "not able to find Menu item sign out"
#else: # Once after finding Element we are tring to move mouse to that element using ActionChain modules and functionality
#     signoutElement.click()






 #   getSignOut = br.find_element_by_link_text("sign Out")
  #  getSignOut.click()
    #actions = ActionChains(br)#where to perform action
    #actions.move_to_element(signoutElement)#what action to perform
    #actions.perform()# perform the action


#pageHTMLSource= br.page_source
#if("Please enter your password" in pageHTMLSource):
#    print"Error message present"
#else:
#    print "no message found"
#br.close()
