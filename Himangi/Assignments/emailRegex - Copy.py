import re
#this code validates the email id
#i'd like to know how can I make it case insensitive
email=raw_input("Please type in your e-mail ID: ")
pt=re.compile('^\w+.*_*@\w+.\w+.\w$')
result = pt.match(email)
print result
if(result != None):
    print "It is a valid E-mail ID"
else:
    print "Oops! Please enter an E-mail Id"
