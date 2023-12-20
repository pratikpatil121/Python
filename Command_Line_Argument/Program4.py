#Command line argument

import sys

print(sys.argv)
size=len(sys.argv)
sum=0

for i in range(1,size):
	sum=sum+int(sys.argv[i])
print(sum)
