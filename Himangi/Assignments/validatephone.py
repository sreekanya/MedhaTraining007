phoneNo=raw_input("Please enter Phone no.: ")
def validate(phoneNo):
    y = 0
    for i in range(0, len(phoneNo)):
        if phoneNo[i].isdigit():
            y=y+1
        else:
            break
        
        
        
        
    if(y==11):
       
        if(phoneNo[0]=='1' and phoneNo[1]!='0' and phoneNo[4]!='0'):  
            print "USA phone no"
        else:
            print "oops! not a valid no." + phoneNo[0]
    elif(y==12):
        if(phoneNo[0]=='9' and phoneNo[1]=='1' and phoneNo[2]!='0' and phoneNo[4]!='0'): 
            print "india phone no"
        else:
            print "oops! not a valid no. here i am" + phoneNo[3]
    else:
        print "Please enter a valid no."

validate(phoneNo)
        
            



