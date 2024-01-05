#Multiple Inheritance

class A:
	def __init__(self):
		print("In Fun: A")

class B:
	def __init__(self):
		print("In Fun: B")

class C:
	def __init__(self):
		print("In Fun: C")

class D(A,B):
	def __init__(self):
		print("In Fun: D")
		super().__init__()
class E(B,C):
	def __init__(self):
		print("In Fun: E")
		super().__init__()

class F(D,E):
	def __init__(self):
		print("In Fun: F")
		super().__init__()

obj=F()
