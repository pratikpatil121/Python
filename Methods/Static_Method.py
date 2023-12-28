#Static Method

class Player:
	
	teamName="India"

	def __init__(self,jerno,pname):
		print("In Constructor")
		self.jerno=jerno
		self.pname=pname
	
	@staticmethod
	def playerInfo():
		print(Player.teamName)

cric1=Player(18,"Virat")
cric2=Player(45,"Rohit")

Player.playerInfo()
cric1.playerInfo()
