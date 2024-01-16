'''
1
1 2
2 3 4
4 5 6 7
7 8 9 10 11
'''
add=1
num=1
for i in range(5):
	num=add-1
	for j in range(i+1):
		num+=1
		print(num,end=" ")
		add=num		
	print()
print()
