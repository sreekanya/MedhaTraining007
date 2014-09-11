# find out given file is a text file.

import re

input1=raw_input("please enter the file name you want to check:")


pt= re.compile('[a-z]+.txt$')
result=pt.match(input1)
print result