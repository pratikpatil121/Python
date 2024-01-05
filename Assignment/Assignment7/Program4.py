#Count of digits

x=int(input("Enter number: "))
c=0
while x>0:
	c+=1
	x=x//10
print(c)

