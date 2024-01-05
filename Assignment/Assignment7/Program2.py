#Prime number 

x=int(input("Enter a number to check prime number: "))
count=0
for i in range(1,x+1):
	if x%i==0:
		count+=1
if count==2:
	print("is prime number")
else:
	print("not a prime number")
