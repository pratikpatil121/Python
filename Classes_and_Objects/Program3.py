#Constructor
#__new__
#__init__

class Employee:
	def __new__(cls):
		print("Create")
	def __init__(self):
		print("Constructor")

Employee()

