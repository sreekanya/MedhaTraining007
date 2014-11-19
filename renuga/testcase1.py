# This Script is to validate elements present in the login page of any website.
#send website name and hack1.csv in console as input.
import sys
from selenium import webdriver
input=sys.argv
flag=0
if (len(input)<2):
	print "please check number of inputs"
	sys.exit()
else :
	url=sys.argv[1]
	fileinput=sys.argv[2]
	brw=webdriver.Firefox()
	brw.get(url)
f=open(fileinput,'r')
def id(brw,keys,value,sk):
	try:
		elementid=brw.find_element_by_id(data[2])
		print data[2]+"found"
	except:
		flag=1
		print data[2]+"Not found"
	#return elementid
def tagname(brw,keys,value):
	try:
		tit=brw.find_element_by_tag_name(data[2])
		print data[2]+"found"
		if (tit.get_attribute("text")==data[4]):
			print "Title Matches with expected result"
		else:
			print "Doesn't match with expected result"
	except:
		flag=1
		print data[2]+"Not found"
		
def link(brw,keys,value):
	try:
		forgot=brw.find_element_by_link_text(data[2])
		print value+"found"
	except:
		flag=1
		print data[2]+"not found"
for line in f:
	line=line.rstrip()
	data=line.split(',')
	#key=data[1]
	#value=data[2]
	#identifymap={data[1]:data[2]}
	if (data[1]=='tagname'):
		tagname(brw,data[1],data[2])
	elif (data[1]=='id'):
		id(brw,data[1],data[2],data[3])
	else:
		link(brw,data[1],data[2])
f.close()
if (flag==1):
	print "Some element is not in page"
else:
	print "Gmail page is launched and title match with gmail Test case 1 Pass"
	
	
		
