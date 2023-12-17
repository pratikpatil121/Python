#first 10 even numbers

#num=int(input("Enter number: "))
num=1
i=1
sum=0
while i<=10:
	if num%2==0:
		sum+=num
		i+=1
	num+=1
print(sum)	
