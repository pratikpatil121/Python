#Multiple Inheritance

class Boss:
	def report(self):
		print("In Boss")

class Manager1(Boss):
	def report(self):
		print("In Manager: 1")

class Manager2(Boss):
	def report(self):
		print("In Manager: 2")

class Manager3(Boss):
	def report(self):
		print("In Manager: 3")

class Team1(Manager1,Manager3):
	def report(self):
		print("In Team: 1")

class Team2(Manager2,Manager3):
	def report(self):
		print("In Team: 2")

class Developer(Team1,Team2):
	def report(self):
		print("In Developer")

obj=Developer()
print(Developer.mro())
