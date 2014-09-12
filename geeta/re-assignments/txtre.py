# to check file is text file or python file.

import re
input1=raw_input("please enter the file name:")

pt1=re.compile('[a-zA-Z0-9\._-]+[.txt]$')
pt2=re.compile('[a-zA-Z0-9\._-]+[.py]$')
result=pt1.match(input1)
result=pt2.match(input1)
if result==pt1.match(input1):
	print result1," is a text file"
	elsif
	result=pt2.match(input1)
	print result,"it is a python file"
	else:
		print"not a text or python file"