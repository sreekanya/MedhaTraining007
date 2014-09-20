import re
username=("Please enter a user name: ")
Pt = ^\w+.\w+$
result = pt.match(username)
print result
if(result != None):
    print "It is a valid user name"
else:
    print "Oops! Please enter a valid user name"
