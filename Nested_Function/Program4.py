#nested functions

def outer():
	def inner1():
		print("In inner1")
	def inner2():
		print("In inner2")
	inner1()
	inner2()
	print("In outer")

outer()
