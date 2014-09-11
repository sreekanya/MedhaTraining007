# this script is to calcualte auto loan money payment per month 

import math

loanAmt = raw_input("please enter the amount of loan: ")
loanAmt = int(loanAmt)
rate = raw_input("please enter the rate of interest: ")
rate = float(rate)
#y = int(rate)

duration = raw_input("please enter the no. of months to pay off: ")
duration = int(duration)

def calculate(loanAmt,rate,duration):
    r = rate/12/100
    x = math.pow(duration,1+r) 
    emi = int(loanAmt)* rate*x/x-1
    print emi

calculate(loanAmt,rate,duration)

