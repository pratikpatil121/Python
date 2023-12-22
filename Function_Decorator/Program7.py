#multiple arguments in decorators

def decorFun(func):
	print("In DecorFun")
	def wrapper(*args):
		print("In Wrapper Function")
		val=func(*args)
		print("Out of Wrapper Function")
		return val
	return wrapper
@decorFun
def normalFun(x,y):
	print("In Normal Function")
	return x+y

#normalFun=decorFun(normalFun)
#normalFun(10,20)
print(normalFun(10,20))
