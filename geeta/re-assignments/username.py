
# check entered username is valid or not

import re

input1=raw_input("pls enter the user name you want to check:")


pt=re.compile('^[a-z|A-Z]+[a-z|A-Z|0-9\._-]+$')

result=pt.match(input1)

if (result !=None):
	print input1,"is a valid username"
else:
	print "invalid user name"
	
# it takes many .-_