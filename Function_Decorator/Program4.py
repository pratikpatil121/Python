#Decor Function

def decorFun(func):
	
	def wrapper():
		print("In Wrapper")
		func()
		print("Out of Wrapper")

	return wrapper

@decorFun            #1st Method 
def normalFun():
	print("In Normal Functoin")

#normalFun=decorFun(normalFun)		#2nd Method
normalFun()
