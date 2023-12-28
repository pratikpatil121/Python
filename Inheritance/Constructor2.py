#Constructor in inheritance

class Parent:
		
	def __init__(self):
		print("In Constructor")

	def parentFunc(self):
		print("In Parent Function")

class Child(Parent):
	def __init__(self):
		print("In Child Constructor")

obj1=Child()
obj1.parentFunc()
