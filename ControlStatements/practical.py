#PRACTICAL 2 CODES

x=int(input("Enter start range: "))
y=int(input("Enter stop range: "))
for i in range(x,y+1):
	if i%4==0 and i%5!=0:
		print(i,"Divisible by four")


x=int(input("Enter value for x"))
if x>0:
	print(x,"Positive Number")
elif x<0:
	print(x,"Negative Number")
else:
	print(x,"Number is Zero")


x=int(input("Enter value for  x: "))
if x>0:
	print(x)
if x<0:
	print(x)


y=int(input("Enter value for x: "))
x=0
for i in range(1,y+1):
	if y%i==0:
		x=x+1	
if x==2:
	print(y,"Is Prime")		
