#WHILE LOOP

i=1
while(i<5):
	print(i)
	i+=1

i=1
x=int(input("Enter value for x: "))
while(i<=x):
	if(i%5==0):
		print(i)
	i+=1

x=int(input("Enter value for x: "))
while (x>0):
	print(x)
	x=x-1

x=int(input("Enter value for x: "))
i=x
while(x>0):
	if(x%2==0):
		print(i)
		i=i-1
	x=x-1
