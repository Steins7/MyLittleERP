from Flux import *
from BalanceVerification import *

class Table(object):
	def addBalanceVerification(self,balance = 0.0):
		BalanceVerification(balance)
		return 1
		
	def addFlux(self,name="",iD ="",value =0.0 ,shortInfo="" , longInfo="" ,supplier="" , iN=0.0 , out=0.0):
		Flux(name,iD,value ,shortInfo , longInfo ,supplier, iN , out)
		return 1
		
	
if __name__ == "__main__":
	t = Table.addFlux()
	Table.addBalanceVerification()
