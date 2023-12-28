#Method to writing the constructors

class Parent:
	
	def __init__(self):
		print("In Parent Construction")

	def parentFunc(self):
		print("In Parent Function")

class Child(Parent):
	
	#Parent()
	#Parent().__init__()

	def __init__(self):
		print("In Child Constructor")
		super().__init__()

	def childFunc(self):
		print("In Child Function")

obj1=Child()
obj1.parentFunc()
obj1.childFunc()
