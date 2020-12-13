## Write a function which can return a Factorial of any numbers as INT, given in the argument.
n = int(input())
factorial = 1
if n<0:
	print("factorial of a negative number doesn't exist")
elif n==0:
	print("factorial of zero is 1")
else:
	for i in range(1,n+1):
		factorial = factorial*i
	print('The factorial of',n ,"is",factorial)

	