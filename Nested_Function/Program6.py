#nested functions

def outer(x,y):
	def inner():
		print("In inner")
	print("In outer")
	return x+y

retval=outer(10,20)
print(retval)
