#file name can't start with digit, must start with a-z in any caps or_, followed by 0-9 or a-z or A-Z
#or.+a-z,-Z,0-9 then a . followed by three letters.  

import re
input1 = raw_input("Please enter a file name: ")
pt = re.compile('^[a-z|A-Z|_]\w+\.*\w*\.[a-z]{3}$')
if result:

    pt1 = re.compile('^[a-z|A-Z|_]\w+\.*\w*\.(py|txt)$')
    result1 = pt1.match((input1))
    if(result1):
        print result
    else:
        "The file is neither python nor text file."
else:
    print "please enter a valid file name."
