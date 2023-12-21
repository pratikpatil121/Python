#Passing multiple funtion as a parameters/arguments

def gun():
	print("In Gun")

def run(y):
	print("In Run")
	y()

def fun(x):
	print("In Fun")

fun(run(gun))
