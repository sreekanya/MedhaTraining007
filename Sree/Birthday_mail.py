#! /usr/bin/python

import selenium
from selenium import webdriver
import datetime
from datetime import date 

list=[]
data=[]
list_mail=[]
today=[]
mail=''

def log_in():
	browser=webdriver.Chrome()
	browser.implicitly_wait(20)
	browser.get("http://gmail.com")
	browser.implicitly_wait(20)
	
	email=browser.find_element_by_id("Email")
	email.send_keys("einfoteam@gmail.com")
	browser.implicitly_wait(20)
	
	pass_wd=browser.find_element_by_id("Passwd")
	pass_wd.send_keys("einfoteam123")
	browser.implicitly_wait(20)
	
	s_in=browser.find_element_by_id("signIn")
	s_in.click()
	
	browser.implicitly_wait(50)
	
	click_comp=browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div").click()
	browser.implicitly_wait(90)

	mail_to=browser.find_element_by_id(':ae')
	mail_to.send_keys(mail)
	print "mail_to", mail
	browser.implicitly_wait(60)

	sub=browser.find_element_by_id(':9m')
	sub.send_keys("Birthday Mail")
	browser.implicitly_wait(60)

	body1=browser.find_element_by_id(':ao')
	body1.send_keys("Happy Birthday To You")
	browser.implicitly_wait(100)
	
	send=browser.find_element_by_id(':9c').click()
	browser.implicitly_wait(60)
	print browser.title
	
	logo=browser.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div[2]/div[5]/div[1]/a/span").click()
	
	browser.implicitly_wait(100)
	
	browser.quit()
	
	

def read_file():
	try:
		fh=open("Birthday_mailing.csv",'r')
	except:
		print "File not present"
	else:
		for line in fh:
			line=line.rstrip()
			list.append(line)
	fh.close()
	
	for i in list:
		j=i.split(',')
		data.append(j)
	
def today_date():
	today_d= str(date.today())
	d=today_d.split('-')
	today.append(d)
	

	
read_file()

today_date()
year,month,day=today[0]

flag=0
i=0
for value in data:
	i=value[1].split('-')
	if((i[1]==month)and(i[2]==day)):
		list_mail.append(value)
		flag=1

if (flag==1):
	mail=list_mail[0][2]
	if(len(list_mail)>1):
		for l in list_mail[1:]:
		  mail=mail+','+l[2]
	print "Birthday's are :",mail
	log_in()

	
if(flag==0):
	print "No Birthdays"
	
	