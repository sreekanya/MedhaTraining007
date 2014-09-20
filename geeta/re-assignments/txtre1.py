# to check file is text file or python file.

import re
input1=raw_input("please enter the file name:")
### input_file or input001_file or input001_file001 or input_file001

pt=re.compile('^[a-z|A-Z]+[0-9]*_*[a-z|A-Z|0-9]*\.[txt|py]$')

result=pt.match(input1)

print result

