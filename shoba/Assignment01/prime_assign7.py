#Create python script to check if a given number is prime number not?

import sys
n = int(raw_input("enter a number to find if its prime or not  :  "))
isPrime = True
for y in range(2,n):

	if(n%y==0) :
		isPrime = False
if isPrime:
	print n,":  is prime number"
else: 
	print n ,"  : not prime number "
	