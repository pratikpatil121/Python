#ascii value return

start=input("Enter start of range: ")
end=input("Enter start of range: ")
char1=ord(start)
char2=ord(end)
for i in range(char1,char2):
	char=chr(i)
	print("Ascii value for %s is"%char,i)
