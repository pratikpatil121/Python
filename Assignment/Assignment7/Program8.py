#odd numbers in integers

i=int(input("Enter numbers: "))
c=0

while i>0:
	#i=i//10
	if i%2==1:
		c+=1
	i=i//10
print(c)
