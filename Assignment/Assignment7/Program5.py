#Reverse the numbers

x=int(input("Enter numbers: "))
c=0
while x>0:
	c+=1
	x=x//10
print(c)
