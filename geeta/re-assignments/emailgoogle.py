



# check given email address is valid or no.
import re

input1=raw_input("please enter the email address:")
pt=re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

result=pt.match(input1)
print result
# this script got by google is working









