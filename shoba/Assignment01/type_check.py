# this program prints what kind of file the user entered
import sys
import re

print sys.argv[0]
pt1=re.compile('[a-z]-\.[txt]')
pt2=re.compile('[a-z]-\.[py]')

name = sys.argv[1]
result1= pt1.match(name)
result2 = pt2.match(name)
print result1 

print result2
#if result1 != true:
#	   print "is a txt file"
#elif result2 !=true:
#		print "is a .py	file"
#else:
#	print " is neither text nor .py file"		




