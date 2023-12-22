#for multiple arguments in the decorator

def normalFun(*args):
	sumData=0
	
	for i in args:
		sumData=sumData+i
	return sumData

print(normalFun())

