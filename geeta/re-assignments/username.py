# check entered username is valid or not

import re

input1=raw_input("pls enter the user name you want to check:")

pt=re.compile('^[a-z]+\[A-Z]+\[0-9]+')

result=pt.match(input1)

print result
