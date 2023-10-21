#FOR LOOP

for i in range(1,15):
	print(i)	#1,2,3,4,5,6,7,8,9,10,11,12,13,14


for y in range(1,15,3):
	print(y)	#1,4,7,10,13


x=int(input("Enter value for X: "))	#5
y=int(input("Enter value for Y: "))	#10
for i in range(x,y+1):
	print(i)	#5,6,7,8,9,10


for i in range(10,3,-2):
	print(i)	#10,8,6,4

x=int(input("Enter value for x: "))	#1
y=int(input("Enter value for y: "))	#10
for i in range(x,y+1):
	if i%2==0:
		print("%d is even"%i)	#2,4,6,8,10
	else:
		print("%d is odd"%i)	#1,3,5,7,9

x=10
y=50
for i in range(x,y+1):
	if i%4==0 and i%5==0:
		print(i)	#20,40
