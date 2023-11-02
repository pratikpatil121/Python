'''
1 3 5 7
5 7 9 11
9 11 13 15
13 15 17 19
'''
add=1
num=1
for i in range(4):
	num=add
	for j in range(4):
		print(num,end=" ")
		num+=2
	add+=4
	print()
