'''
1 3 5
7 9 11
13 15 17
''' 

num=1
for j in range(3):
	i=1
	for i in range (3):
		if num%2==1:
			print(num,end=" ")
			num+=1
		num+=1
	print()
