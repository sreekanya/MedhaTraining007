# check given email address is valid or no.
import re

input1=raw_input("please enter the email address:")
pt=re.compile('[a-z|A-Z]+\.*[a-z|A-Z]*[0-9]*+@[a-z]+\.com$')

result=pt.match(input1)
print result
#script not working
