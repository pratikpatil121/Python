#Multiple Inheritance

class Parent1:
	
	def dispData(self):
		print("In DispData")

class Parent2:
	
	def printData(self):
		print("In PrintData")

class Child(Parent1,Parent2):
	pass

obj=Child()
obj.dispData()
obj.printData()
