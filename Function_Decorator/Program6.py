#for multiple keywords and arguments in decorator

def normalFun(**kargs):
	sumData=0

	for k,v in kargs.items():
		sumData=sumData+v
	return sumData

print(normalFun(x=10,y=20,z=30))
