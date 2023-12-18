#nested functions

def outer(x,y):
	def inner():
		print("In inner")
	print("In outer")

retval=outer(10,20)
print(retval)
