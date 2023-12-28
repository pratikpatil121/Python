#Class Method

class Player:

	teamName="India"

	def __init__(self,jerno,pname):
		print("In Constructor")
		self.jerno=jerno
		self.pname=pname

	def playerInfo(self):
		print(self.jerno)
		print(self.pname)
		print(self.teamName)

cric1=Player(18,"Virat")
cric2=Player(45,"Rohit")

cric1.playerInfo()
cric2.playerInfo()

Player.teamName="Bharat"

cric1.playerInfo()
cric2.playerInfo()
