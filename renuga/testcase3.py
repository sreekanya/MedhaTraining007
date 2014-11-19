import sys
from selenium import webdriver
input=sys.argv
flag=0
#identifymap={}
#actionmap={}
if (len(input)<5):
		print "please check number of inputs"
		sys.exit()
else :
	url=sys.argv[1]
	fileinput=sys.argv[2]
	brw=webdriver.Firefox()
	brw.get(url)
	uname=sys.argv[3]
	pwd=sys.argv[4]
def login(brw,uname,pwd):
	e=brw.find_element_by_id("Email")
	e.send_keys(uname)
	p=brw.find_element_by_id("Passwd")
	p.send_keys(pwd)
	submit=brw.find_element_by_id("signIn").click()
	print "Logging in"
	
def id(brw,keys,value):
	try:
		elementid=brw.find_element_by_id(data[2])
		print data[3]+"found"
	except:
		"Element not found"
		flag=1
def hylin(b,ke,va):
	try:
		tit=brw.find_element_by_tag_name(data[1])
		print data[3]+"found"
	except:
		flag=1
def cn(br,key,val):
	try:
		cass=brw.find_element_by_class_name(data[2])
		print data[3]+"found"
		flag=1
	except:
		flag=1
	
login(brw,uname,pwd)
brw.implicitly_wait(60)
f=open(fileinput,'r')
try:
	for line in f:
		line=line.rstrip()
		data=line.split(',')
		if (data[1]=='id'):
			print "finding element by id"
			id(brw,data[1],data[2])
		elif (data[1]=='classname'):
			print "finding element by class name"
			cn(brw,data[1],data[2])
		else:
			print "finding element by link"
			hylin(brw,data[1],data[2])
		
except :
	print "Error in opening file"
if (flag==1):
	print "Some element is not identified"
else:
	print "logging in and validation of second page is Successfull,Google logo found,Username found"
	
f.close()

	