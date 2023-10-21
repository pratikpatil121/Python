#NESTED FOR LOOP

x=int(input("Enter value for x: "))
for i in range(x):
	print("5",end= " ")
print()

x=int(input("Enter value for x: "))
for i in range(x):
	print(i+1,end=" ")
print()

x=10
for i in range(x):
	if i%2==0:
		print("*",end=" ")
	else:
		print(i,end=" ")
print()

x=50
for i in range(5,x+1,5):
	if i%2==0:
		print("*",end=" ")
	else:
		print(i,end=" ")
print()

for i in range(1,20):
	if i%3==0:
		print("Three")
	elif i%5==0:
		print("Five")
	else:
		print(i)

#problem statement
for i in range(1,21):
	if i%2==0:
		print(i,end=" ")

x=1
i=int(input("Enter number for multiplication table"))
while x<=10:
	print(x*i)
	x+=1

x=int(input("Enter value for x: "))
for i in range(1,x+1):
	if x%i==0:
		print(i)


for i in range(3):
	print("i loop")
	for j in range(3):
		print("j loop")	

for i in range(3):
        print("i loop")
        for j in range(i+1):
                print("j loop") 

