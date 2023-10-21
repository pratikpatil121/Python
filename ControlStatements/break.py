#BREAK STATEMENT

x=int(input("Enter value for x: "))
while(x>0):
	print(x)
	x=x-1
	if(x==5):
		break


playerList=["Rohit","Shubmna","Virat","Ayyar","KLRahul"]
playerName=input("Enter Player Name: ")
count=0
for player in playerList:
	count=count+1
	if player == playerName:
		print(playerName,"Present in list: ")
	#	count=count+1
		break
print(count)
if count == 0:
	print("Not in list")
