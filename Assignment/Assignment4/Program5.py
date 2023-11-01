#divisible by 7 but not by 3

start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))

for i in range(start,end+1):
	if i%7==0 and i%3!=0:
		print(i)
