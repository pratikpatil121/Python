#Two Character Addition

x=input("Enter first character: ")
y=input("Enter second character: ")
z=ord(x)+ord(y)
if ord(x)%2==1 and ord(y)%2==1:
	print("Addition is %d"%z)
