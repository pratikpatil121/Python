#Function Decorator

def fun():
	print("In Outer Function")

	def inner1():
		print("In inner1 function")
	
	def inner2():
		print("In inner2 function")

	return inner1,inner2

ret1,ret2=fun()

ret1()
ret2()
