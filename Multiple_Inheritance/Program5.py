#id of multiple objectes of same class

class Demo:
	pass

obj1=Demo()
obj2=Demo()

print(id(obj1))
print(id(obj2))

print(obj1==obj2)
