#Perfect Number

x=int(input("Enter number to check the perfect number: "))

for i in range(1,x):
	if x%i==0:
		print(i)
		sum=i
	sum=sum+i
	if sum==x:
		print(sum,"is perfect number")
