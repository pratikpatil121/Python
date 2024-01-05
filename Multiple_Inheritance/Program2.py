#Multiple Inheritance

#class object:
#	def __init__(self):
#		print("In Class Object")

class Parent1:
	def fun(self):
		print("In Parent1")
#		super().fun()

class Parent2:
	def fun(self):
		print("In Parent2")
#		super().fun()

class Child(Parent1,Parent2):
	
	def fun(self):
		print("In function")
		super().fun()
obj=Child()
obj.fun()
print(Child.mro())
