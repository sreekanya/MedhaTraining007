
def getBignum():
    a = list()
    a=raw_input ("Please enter a number")
    
   
  
    compnum = a[0]
    
    b = a[1]
    #print 'i am here'
    if(compnum<=b):
        print 'i am here'
        for i in range(0,len(a)):
            print i,'is', a[i]
            while b<=a[i]:
                b=a[i]
                print b
                break
    else:
         for i in range(0,len(a)):
            print i,'is', a[i]
            while compnum<=a[i]:
                compnum=a[i]
                print compnum
        
                break



                
getBignum()
