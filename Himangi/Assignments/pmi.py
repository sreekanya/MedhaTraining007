import math
loanAmt = raw_input("please enter the amount of loan: ")
loanAmt = int(loanAmt)
rate = raw_input("please enter the rate of interest: ")
rate = float(rate)
#y = int(rate)
duration = raw_input("please enter the no. of months to pay off: ")
duration = int(duration)

def calculate(loanAmt,rate,duration):
    r = (rate/100)/12
    print r
    x =(1+r)**duration 
    emi = int(loanAmt)*(r*x /(x-1))
    emi = math.ceil(emi)
    print emi

calculate(loanAmt,rate,duration)

