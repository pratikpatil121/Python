#Public , Protected , Private class

class Demo():
	z=30		#Public clas

	def __init__(self):	
		self._x=10	#Protected Class
		self.__y=20	#Private Class

#print(dir(Demo))

obj=Demo()

print(obj.z)
print(obj._x)
print(obj._Demo__y)
