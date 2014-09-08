def processAge(bdEpo, myEpo):
    ageEpo = myEpo-bdEpo
    _month = ageEpo/2629744
    age= _month/12
    months= int(_month)%12
    print "your age is ", int(age),"years and ", months, " months"

#    return (age,months)    

def calcAge():
    import time
    myEpo=time.time()
    obtainBD = raw_input("Please enter birthdate in yyyy-mm-dd: ")
    date_time = obtainBD + ' 00:00:00'
    patern = '%Y-%m-%d %H:%M:%S'
    bdEpo = int(time.mktime(time.strptime(date_time, patern)))
    if(bdEpo<0):
        bdEpo = abs(bdEpo)
        processAge(bdEpo,myEpo)
    else:
        processAge(bdEpo,myEpo)
    
calcAge()
