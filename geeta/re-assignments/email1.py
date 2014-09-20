# trial for valid email.

import re

input1=raw_input("pleas enter email addrres:")
pt= re.compile('^[a-z|A-Z]+[\w+\.*\-*\w]+@[a-z]+\.["com"|"biz"|"org"|"edu"|"co"|"au"|"uk"]+$')
result=pt.match(input1)

print result
# himangi script

# script  working
