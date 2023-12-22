#Chaining Decorator

def decorFun(func):
	
	def wrapper():
		print("In Wrapper 1")
		func()
		print("Out Wrapper 1")
	return wrapper

def decorRun(func):

	def wrapper():
		print("In Wrapper 2")
		func()
		print("Out Wrapper 2")
	return wrapper

#@decorRun
#@decorFun
def normalFun():
	print("In NormalFun")
	
normalFun=decorFun(decorRun(normalFun))
normalFun()
