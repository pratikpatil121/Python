#Arithmetic Operators

x=2
y=5


print(x+y)	#7
print(x-y)	#-3
print(x*y)	#10
print(x/y)	#0.4
print(x%y)	#2
print(x//y)	#0
print(x**y)	#32

#Relational Operators

x=10
y=20

print(x<y)	#true
print(x>y)	#false
print(x<=y)	#true
print(x>=y)	#false
print(x==y)	#false
print(x!=y)	#true

#Logical operators

x=True
y=False

print(x and y)	#false
print(x or y)	#true
print(not x)	#false

a=10
b=20

print(a and b)	#20
print(a or b)	#10
print(not a)	#false

#Assignment operators

x=10
y=5

print(x)	#10
x+=y	
print(x)	#15

x/=y
print(x)	#

#Identity operators

listData=[10,20,30,40,50]
x=10
y=20

print(id(x))
print(id(y))
print(x is y)	#false
print(x is not y)	#true

#Membeship operators

listData=[10,20,30,40,50]

print(x in listData)	#true
print(y in listData)	#true
print(y not in listData)	#false

