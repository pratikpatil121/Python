#nested functions

def outer():
	def inner1(x,y):
		print("In inner1")
		return x+y
	def inner2(a,b):
		print("In inner2")
		return a*b
	return inner1,inner2

inner1,inner2=outer()
ret1=inner1(10,20)
ret2=inner2(3,4)
print(ret1+ret2)
print(inner1)
print(inner2)
