
##Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from the user 
x = int(input())
upper = x
print ("the numbers are as below ")
for num in range(0,upper):
	if num>1:
		for i in range(2,num):
			if (num % i) == 0 :
				break
		else:
			print(num)
