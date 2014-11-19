import selenium
from selenium import webdriver
br = webdriver.Firefox()
br.get("https://facebook.com")
br.implicitly_wait(30)

		
try:
	title= br.find_element_by_xpath("//*[@id=\"blueBarNAXAnchor\"]/div/div/div/a")
except:
	print "unable to find the element title"
else:
	print ("able to find the element title ", title)

try:
	uname= br.find_element_by_id("email")
except:
	print "unable to find the element id "
else:
	print ("able to find the element emaillogin", uname)
	uname.send_keys("shoba24.s@gmail.com")

try:
	password= br.find_element_by_id("pass")
except:
	print "unable to find the element password"
else:
	print ("able to find the element password ", password)
	password.send_keys("lamps123")
	
try:
	login= br.find_element_by_id("u_0_n")
except:
	print "unable to find the element id "
else:
	print ("able to find the element login button ", login)
	login.click()

try:
	loggenin_logo= br.find_element_by_xpath("//*[@id=\"u_0_f\"]/a")
except:
	print "unable to find the element loggenin_logo "
else:
	print ("able to find the element loggenin_logo ", loggenin_logo)
	
	
try:
	search_tab= br.find_element_by_xpath("//*[@id=\"u_0_e\"]/div[3]")
except:
	print "unable to find the element search_tab "
else:
	print ("able to find the element search_tab", search_tab)

	
			
try:
	home_link= br.find_element_by_xpath("//*[@id=\"u_0_g\"]/a")
except:
	print "unable to find the element home_link "
else:
	print ("able to find the element home_link ",home_link)	
	
try:
	anchor_logout= br.find_element_by_xpath("//*[@id=\"pageLoginAnchor\"]")
except:
	print "unable to find the element anchor_logout "
else:
	print ("able to find the element loggenin_logo ", anchor_logout)
	
	
try:
	logout_button= br.find_element_by_xpath("//*[@id=\"logout_form\"]/label/input")
except:
	print "unable to find the elementlogout_button "
else:
	print ("able to find the element loggenin_logo ", logout_button)

print "program successfull"
br.close()	