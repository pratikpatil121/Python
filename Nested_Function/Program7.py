#nested functions

def outer():
	def inner1():
		print("In inner1")
	def inner2():
		print("In inner2")
	print("In outer")
	return inner1,inner2

retobj=outer()
for i in retobj:
	i()
