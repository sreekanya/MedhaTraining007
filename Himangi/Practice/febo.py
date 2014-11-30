a,b = 0,1
for i in range(0,10):
    print a
#    a,b=b,a+b
    tmp = a+b
    a = b
    b=tmp


