from Line import *

class Flux(Line):
	
	def __init__(self, name="",iD ="",value =0.0 ,shortInfo="" , longInfo="" ,supplier="" , iN=0.0 , out=0.0 ,jour =[0,0],mois=0,annee=0):
		super().__init__(name,iD,jour,mois,annee) #utilisation super  ? ,iD,jour,mois,annee
		self.value=value
		self.shortInfo=shortInfo
		self.longInfo=longInfo
		self.supplier=supplier
		self.iN=iN
		self.out=out
		
	
		
