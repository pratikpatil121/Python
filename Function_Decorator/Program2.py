#Passing function as parameters/arguments

def run():
	print("In Run")

def fun(x):
	print("In Fun")
	x()

fun(run)
