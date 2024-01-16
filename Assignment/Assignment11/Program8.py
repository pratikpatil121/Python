'''
1
3 2
6 5 4
10 9 8 7
'''
num=1
for i in range(4):
	num=i-1
	for i in range(i+1):
		print(num,end=" ")
		num+=1	
	print()
print()
