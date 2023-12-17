#cube for number in reverse

num=int(input("Enter number: "))
i=num
while i>=1:
	if i%2==1:
		print(i*i*i)
	i-=1
'''
i=1
for i in range(1,15+1):
	if i%2==1:
		print(i*i*i)
'''
