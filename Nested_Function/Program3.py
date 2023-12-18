#nested functions

def outer():
	def inner():
		print("In inner")
	print("In outer")

outer()
