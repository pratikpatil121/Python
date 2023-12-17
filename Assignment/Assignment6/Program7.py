#nth even number

num=int(input("Enter number: "))
digit=0
i=1
while i<=num:
	digit+=1
	if digit%2==0:
		i+=1
		#digit=num
print(digit)
