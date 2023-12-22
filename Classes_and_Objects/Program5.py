#Class Variable/Static Variable

class Company:
	compname="Facebook"

	def __init__(self):
		print("In Constructor")
		self.empid=12
		self.empname="Kanha"

	def compinfo(self):
		print(self.empid)
		print(self.empname)
		print(Company.compname)

emp1=Company()
emp2=Company()

emp1.compinfo()
emp2.compinfo()
