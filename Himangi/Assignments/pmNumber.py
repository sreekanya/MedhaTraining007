import math
def primeNum():
    myNum = raw_input("Please enter a number:")
    sqRoot = int(myNum)**.5
    myr = int(math.ceil(sqRoot))
    if(myr <= 2):
        myr = myr+1
    if(myr == 3):
        myr = myr + 1
    for i in range(2,myr):
        if(int(myNum) != i):
            if((int(myNum) % i) == 0):
                print "not a prime number"           
                break
    else:
        print"prime number"

    





primeNum()
