'''
$ = $ =
$ = $ =
$ = $ =
$ = $ =
'''
num=1
for i in range(4):
	for j in range(4):
		if num%2==1:
			print("$",end=" ")
		else:
			print("=",end=" ")
		num=num+1
	print()
print()
