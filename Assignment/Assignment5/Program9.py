'''
1 3 5
3 5 7
5 7 9
'''
add=1
num=1
for i in range(3):
	num=add
	for j in range(3):
		print(num,end=" ")
		num+=2
	add+=2
	print()
