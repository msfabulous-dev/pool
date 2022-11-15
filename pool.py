from math import sqrt, log, factorial
def helper():
	print("Welcome to the simple math helper.\nWhat would you like to calculate?\n1. Sqrt\n2. Log\n3. Factorial")
	choice=input()
	
	if (int(choice) == 1):
		print("Enter the number to sqrt:")
		numb=input()
		return sqrt(int(numb))
		
	elif (int(choice) == 2):
		print("Enter the number to log:")
		numb=input()
		return log(int(numb))
 		
	elif (int(choice) == 3):
		print("Enter the number to factorial:")
		numb=input()
		return factorial(int(numb))
