'''
2  5  10
17 26 37
50 65 82
'''
var=0
num=1
for i in range(3):
	for j in range(3):
		var=num*num
		print(var+1,end=" ")
		num=num+1
	print()
print()
