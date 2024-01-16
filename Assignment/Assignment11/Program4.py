'''
1 1 1 1
2 2 2
3 3
4
'''
row=4
num=1
for i in range(row):
	for j in range(row-i):
		print(num,end=" ")
	num+=1
	print()
print()
