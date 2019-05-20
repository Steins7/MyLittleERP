from Flux import *
from BalanceVerification import *

class Table(object):
	def __init__(self) :
		self.table=[]
	def addBalanceVerification(self,name="",iD ="",cumul =0.0 , balance=0.0 , balanceGap=0.0,jour =[0,0],mois=0,annee=0):
		a=BalanceVerification(name,iD,cumul,balance,balanceGap,jour,mois,annee)
		self.table.append(a)
		return 0
		
	def addFlux(self,name="",iD ="",value =0.0 ,shortInfo="" , longInfo="" ,supplier="" , iN=0.0 , out=0.0 ,jour =[0,0],mois=0,annee=0):
		a = Flux(name,iD ,value,shortInfo , longInfo,supplier, iN , out,jour ,mois,annee)
		self.table.append(a)
		return 0
		
	
if __name__ == "__main__":


	a = Table()
	a.addBalanceVerification("theo","bouh-dah", 10.0,10.0,0,[0,3],12,1997)
	print a.table[0].name
