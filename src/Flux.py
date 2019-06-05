from Line import *
from Date import Date

class Flux(Line):
	
	def __init__(self, name="",iD ="",value =0.0 ,shortInfo="" , 
                     longInfo="" ,supplier="" , iN=0.0 , out=0.0 ,date="none"):
		super(Flux,self).__init__(name,iD,date)
		self.value=value
		self.shortInfo=shortInfo
		self.longInfo=longInfo
		self.supplier=supplier
		self.iN=iN
		self.out=out
		
	
		
if __name__ == "__main__":
	a =Flux("theo","bouh-dah", 10.0,"est beau","mais genre vraiment","quelqu'un",1000.0,0.0,Date(3,12,1997))
	print(a.name)
	print("a.iN = "+a.iN)
	print(a.date.getDateString())
