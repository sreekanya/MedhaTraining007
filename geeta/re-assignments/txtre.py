# to check file is text file or python file.

import re
input1=raw_input("please enter the file name:")

pt=re.compile('[a-zA-Z0-9\._-]+\.[txt|py]$')

result=pt.match(input1)

print result