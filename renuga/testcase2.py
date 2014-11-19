
import sys
from selenium import webdriver
input=sys.argv
if (len(input)<2):
	print "please check number of inputs"
	sys.exit()
else :
	url=sys.argv[1]
	fileinput=sys.argv[2]
	brw=webdriver.Firefox()
	brw.get(url)
f=open(fileinput,'r')

def gmail():
	flag=0
	for i in f:
		i=i.rstrip()
		data=i.split(',')
		print data[2]
		try :
			#print "Checking for title"
			if (data[1]=='tagname'):
				tit=brw.find_element_by_tag_name(data[0])
				checktitle(tit,brw,data[4])
			elif (data[1]=='link'):
				link1=brw.find_element_by_link_text(data[2])
				print data[2]+found
			else :
				w=brw.find_element_by_id(data[2])
				print data[2]+"found"
				if (w.get_attribute("type")=='email' or w.get_attribute("type")=='password'):
					print "Sending data"
					w.send_keys(data[3])
				else:
					brw.implicitly_wait(60)
					print "Clicking on "+ data[2]
					w.click()
			flag =1
		except:
			print "Not found"
			flag =0
	if flag==1:
		print " ALL Elements present and this page accepting credentials test case 2 Pass"
	else :
		print "Not sucessfull"
	return brw
def checktitle(tit,brw,dat):
	expectedtitle=tit.get_attribute("text")
	print expectedtitle
	if(expectedtitle==dat):
		print "Title found and text matching with expected result"
	else:
		print "Title didn't match with expected result"
		
gmail()


	
	