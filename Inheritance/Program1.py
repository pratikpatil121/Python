#Inheritance

class Company:
	x=10

	def __init__(self,compName,loc):
		print("In Constructor")
		self.compName=compName
		self.loc=loc

	def compInfo(self):
		print(self.compName)
		print(self.loc)

class Employee(Company):
	pass

obj1=Employee("Microsoft","Pune")
obj2=Employee("Microsoft","Banglore")

obj1.compInfo()
obj2.compInfo()
