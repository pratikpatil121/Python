'''
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1
'''

row=5

for i in range(row):
	num=1
	for j in range(row-i):
		print(num,end=" ")
		if num==1:
			num-=1
		else:
			num+=1
	print()
print()
	
