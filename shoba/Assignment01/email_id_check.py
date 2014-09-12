#python script to check if entered email id is valid or not
import re
#accepting email id from user
emailAddress = (raw_input("enter a  email id")
pt=re.compile('^[a-z]+\@+[a-z]+\.[com]')
check1 = pt.match(emailAddress)
pt2=re.compile('[a-z]+ [0-9]\@+[a-z]+\.[com]')
check2 = pt2.match(emailAddress)
pt3=re.compile('[0-9]+[a-z]+[0-9]@+[a-z]+\.[com]')
check3 = pt3.match(emailAddress)
pt4=re.compile('[a-z]+ [0-9]+[a-z]+\@+[a-z]+\.[com]')
check4 = pt4.match(emailAddress)
if check1 != none:
	   print "is a valid email id"
elif check2 != none:
	  print "is a valid email id"
elif check3 ! = none
	  print "is a valid email id"	
elif check3 ! = none
	  print "is a valid email id"
 else:
		print "invalid email id"	



