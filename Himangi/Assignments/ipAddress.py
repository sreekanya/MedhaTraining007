#for IP adress pattern I searched up on internet and find many complicated things.
#A few of the things I could understand were: 1. It has four sets of three digits
#ranging from 0-255,except the first set, it can not start with 0 value or 0 as 
#first digit. 2. Each set is  seperated by a '.' 


import re
input1 = raw_input("Please enter IP Address: ")
pt = re.compile('^(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(2[0-4][0-9]|25[0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$')
result = pt.match(input1)
if (result):
     print input1, " is a valid IP address." 
else:
    print input1,  "is not a valid IP address."
