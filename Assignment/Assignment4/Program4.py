#Ascii value

start=int(input("Enter start range: "))
end=int(input("Enter end range: "))

for i in range(start,end):
	char=chr(i)
	print("The character of Ascii value %d is"%i,char)
