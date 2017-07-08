import os
class Path:
	def __init__(self):
		maind=os.getcwd().split("/")
		self.mainp=""
		for i in range(len(maind)-1):
			self.mainp=self.mainp+maind[i]+"/"
		
		

