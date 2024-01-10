'''
A b C
d E f
G h I
'''
var=96
num=65
for i in range(3):
	for j in range(3):
		if var%2==1:
			print(chr(var+1),end=" ")
		else:
			print(chr(num),end=" ")
		num+=1
		var+=1
	print()
print()
