#Methods of set

#add()
setdata1={1,2,3,4}
setdata1.add(5)
print(setdata1)

#copy()
setdata2={1,2,3,4}
setdata3=setdata1.copy()
print(setdata2)
print(setdata3)

#difference()
setdata4={1,2,3,4}
setdata5={3,4,5,6}

setdata6=setdata4.difference(setdata5)
print(setdata6)

#difference_update()
setdata7={1,2,3,4}
setdata8={3,4,5,6}

setdata7.difference_update(setdata8)
print(setdata7)
print(setdata8)

#discard()
setdata9={1,2,3,4}
setdata9.discard(3)
print(setdata9)

#intersection()
setdata10={1,2,3,4}
setdata11={3,4,5,6}

setdata12=setdata10.intersection(setdata11)
print(setdata10)
print(setdata11)
print(setdata12)

#intersection_update()
setdata13={1,2,3,4}
setdata14={3,4,5,6}

setdata15=setdata13.intersection_update(setdata14)
print(setdata13)
print(setdata14)
print(setdata15)

#isdisjoint()
setdata16={1,2,7,8}
setdata17={3,4,5,6}
print(setdata16)
print(setdata17)

print(setdata16.isdisjoint(setdata17))

#issubset()
setdata18={1,2,3,4}
setdata19={3,4,5,6,1,2}

print(setdata18.issubset(setdata19))

#issuperset()
setdata20={1,2,3,4}
setdata21={3,4,5,6,1,2}

print(setdata20.issuperset(setdata21))

#symmetric_difference()
setdata22={1,2,3,4}
setdata23={3,4,5,6}

print(setdata23.symmetric_difference(setdata22))

#union()
setdata24={1,2,3,4}
setdata25={3,4,5,6}
print(setdata24)
print(setdata25)
print(setdata24.union(setdata25))

#update()
setdata26={1,2,3,4}
setdata27={3,4,5,6}
print(setdata26)
print(setdata27)

setdata26.update(setdata27)
print(setdata26)
print(setdata27)

#pop()
setdata28={10,20,30,40}
print(setdata28)
setdata28.pop()
print(setdata28)

#remove()
setdata29={10,20,30,40}
setdata29.remove(30)
print(setdata29)

#clear()
setdata30={10,20,30,40}
print(setdata30)
setdata30.clear()
print(setdata30)
