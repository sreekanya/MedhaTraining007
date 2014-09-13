# trial for valid email.

import re

input1=raw_input("pleas enter email addrres")
pt= re.compile('^[a-z|A-Z]+\w+_.\w@[a-z]+.["com"|"biz"|"org"|"edu"|"co"|"au"|"uk"]+$')
result=pt.match(input1)

print result