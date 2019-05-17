from Line import *

class Flux(Line):
	
	def __init__(self, name="",iD ="",value =0.0 ,shortInfo="" , longInfo="" ,supplier="" , iN=0.0 , out=0.0 ,jour =[0,0],mois=0,annee=0):
		super(Flux,self).__init__(name,iD,jour,mois,annee)
		self.value=value
		self.shortInfo=shortInfo
		self.longInfo=longInfo
		self.supplier=supplier
		self.iN=iN
		self.out=out
		
	
		
if __name__ == "__main__":
	a =Flux("theo","bouh-dah", 10.0,"est beau","mais genre vraiment","quelqu'un",1000.0,0.0,[0,3],12,1997)
	print a.name
	print "a.iN = ", a.iN
	print a.date.getDateString()
