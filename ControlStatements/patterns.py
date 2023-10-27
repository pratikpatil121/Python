#Star patterns
'''
* * *
* * *
* * *
'''
for i in range(3):
	for j in range(3):
		print("*",end=" ")
	print()
print()
'''
A A A
A A A
A A A
'''
for i in range(3):
	for j in range(3):
		print("A",end=" ")
	print()       
print()
'''
1 1 1
2 2 2 
3 3 3
'''
num=1
for i in range(3):
		
	for j in range(3):
		print(num,end=" ")
		        
	print()
	num=num+1
print()
'''
1 2 3
4 5 6
7 8 9
'''
num=1
for i in range(3):
	for j in range(3):
		print(num,end=" ")
		num=num+1
	print()
print()
'''
1 2 3
1 2 3
1 2 3
'''
for i in range(3):
	num=1
	for j in range(3):
		print(num,end=" ")
		num=num+1
	print()
print()
'''
1 2 3
2 3 4
3 4 5
'''
for i in range(3):
	num=i+1
	for j in range(3):
		print(num,end=" ")
		num=num+1
	print()
print()
'''
*
* *
* * *
'''
for i in range(3):
	for j in range(i+1):
		print("*",end=" ")
	print()
print()

'''
1
2 3
4 5 6
'''

num=1
for i in range(3):
	for j in range(i+1):
		print(num,end=" ")
		num=num+1
	print()
print()
'''
A
B C
D E F
'''
num=65
for i in range(3):
	for j in range(i+1):
		print(chr(num),end=" ")
		num=num+1
	print()
print()

'''
1 2 3
4 5
6
'''
num=1
row=3
for i in range(row):
	for j in range(row-i):
		print(num,end=" ")
		num=num+1
	print()
print()
