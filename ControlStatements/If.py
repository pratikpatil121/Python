#IF CONDITION

x=int(input("Enter value for Age: "))
if(x>18):
	print("Eligible For Voting")
print("Out of if")

#any number other than 0 gives output TRUE
x=10
y=20
if(x):
	print("true")
print("out of if")

#IF ELSE STATEMENT
	
x=int(input("Enter Value For X: "))
if(x>20):
	print("X is greater than 20")
else:
	print("Y is less than 20")

#else block
x=int(input("Enter value or x: "))
if(x>20):
	print("X is greater than 20")
else:
	print("X is less than 20")
	{
		print("Else block")
	}

x=int(input("Enter the number"))
if(x%2==0):
	print("%d is even"%x)
else:
	print("%d is odd"%x)

#IF ELIF ELSE STATEMENT

num=int(input("Enter number"))
if(num>0):
	print("{} is positive".format(num))
elif(num<0):
	print("{} is negative".format(num))
else:
	print("{} is zero")	

