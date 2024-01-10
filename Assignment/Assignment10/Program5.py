'''
1  2  9  4
25 6  49 8
81 10 121 12
169 14 225 16
'''

num=1
for i in range(4):
	for j in range(4):
		if num%2==0:
			print(num,end=" ")
		else:
			print(num*num,end=" ")
		num+=1
	print()	
print()	
