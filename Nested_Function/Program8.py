#nested function

def outer(x,y):
	def inner(a,b):
		print("In inner")
		return a+b
	print("In outer")
	print(x+y)
	return inner

retobj=outer(5,8)
innerobj=retobj(3,4)
print(retobj)
print(innerobj)
