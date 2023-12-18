#Array

import array as arr

data=arr.array('i',[10,20,30,40,50,10])
print(data)

print(data.buffer_info())

print(id(data))

print(data.count(10))

data.append(500)
print(data)

data.extend([70,80,80])
print(data)

newData=arr.array('i',[100,200,300,400,500])
listData=[10,20,30,40,50]

newData.fromlist(listData)

print(newData)

print(data.index(20))

data.pop()
print(data)

data.remove(20)
print(data)

copyList=data.tolist()
print(copyList)

