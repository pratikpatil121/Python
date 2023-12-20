#command line argument
#addition of even number
import sys

print(sys.argv)
size=len(sys.argv)
add=0

for i in range(1,size):
	if int(sys.argv[i])%2==0:
		add=add+int(sys.argv[i])
print(add)
