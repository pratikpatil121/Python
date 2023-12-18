#Array Bits Size unicodes

import array as arr

data=arr.array('b',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('u','abcde')
print(data.itemsize)

data=arr.array('B',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('h',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('H',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('i',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('I',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('l',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('L',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('q',[10,20,30,40,50])
print(data.itemsize)

data=arr.array('Q',[10,20,30,40,50])
print(data.itemsize)

