# script for checking valid US phone number
import re

pt=re.compile('[1-9][0-9][0-9]\-[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9]')

input1=raw_input("Please enter the phone number:")
print input1
result=pt.match(input1)

print result
#it ia taking phone number with - inbetn,after escape sign also not working for without-