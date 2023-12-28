#Class Method

class Player:
	teamName="India"

	def __init__(self,jerno,pname):
		print("In Constructor")
		self.jerno=jerno
		self.pname=pname

	@classmethod
	def playerInfo(cls):
		#print(self.jerno)
		#print(self.pname)
		print(cls.teamName)

cric1=Player(18,"Virat")
cric2=Player(45,"Rohit")

Player.playerInfo()
cric1.playerInfo()
