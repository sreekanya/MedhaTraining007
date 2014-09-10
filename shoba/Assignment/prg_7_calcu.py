#this is program for calculator
#returns the sum of num1 and num2
def add(num1,num2):
	return num1+num2
	
	#returns sub of two number
def sub(num1,num2):
	return num1-num2
	
	#returns multiplication of two num
def multi(num1,num2):
	return num1*num2
	
	#returns division of two numbers
def div(num1,num2):
	return num1/num2
		



def main():
	operation=raw_input("what operation would u like to perform (+,-,*,%)  ")
	if(operation != "+" and operation != "-" and operation !="*" and operation != "%"):
			#if invalid operation
		print("please enter a valid operation   ")
	else:
		num1=int(raw_input("enter num1   "))
		num2 =int(raw_input("enter num2   "))
		if(operation =='+'):
			print(add(num1,num2))
		elif(operation == '-'):
			print (sub(num1,num2))
		elif(operation== '*'):
			print (multi(num1,num2))
			#if(operation =="%"):
		else:
			print (div(num1,num2))
	

main()