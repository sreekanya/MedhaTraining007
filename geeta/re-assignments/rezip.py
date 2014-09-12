# check entered zipcode is valid US zipcode or not.

import re

input1=raw_input("please enter the zip code you want to check:")
pt=re.compile('[1-9][0-9][0-9][0-9][0-9]')

result=pt.match(input1)
print result

# its matching more than 5 digits entered 