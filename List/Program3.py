#List
#append
#extends
#index
#deletion

player=["Rohit","Shubman","Virat","Shreyas","KL"]
print(player)

player.append("SKY")
print(player)


player.extend(["Jaddu","Bumbrah","Shami"])
print(player)

player.insert(3,"Jaddu")
print(player)

player.remove("SKY")
print(player)

player.pop()
print(player)

#player.clear()
#print(player)

print(player.count("Jaddu"))

print(player.index("Virat"))

print(player.reverse())

print(player.sort())

batesmen=player.copy()
print(batesmen)
