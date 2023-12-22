#Constructor and Instance Variable

class Employee:
	
	def __init__(self,empid,empname):
		print("In Constructor")
		self.empid=empid
		self.empname=empname

	def empinfo(self):
		print(self.empid)
		print(self.empname)

emp1=Employee(12,"kanha")
emp2=Employee(15,"rahul")

emp1.empinfo()
emp2.empinfo()
