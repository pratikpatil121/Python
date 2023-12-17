#7th odd number
count=0
num=1
i=1
while i<=7:
	if num%2==1:
		i+=1
		count=num
	num+=1
print(count)
