
from Line import *

class BalanceVerification(Line):
	
	def __init__(self, name="",iD ="",cumul =0.0 , balance=0.0 , balanceGap=0.0,jour =0,mois=0,annee=0):
		super(BalanceVerification,self).__init__(name,iD,jour,mois,annee)
		self.cumul=cumul
		self.balance=balance
		self.balanceGap=balanceGap



if __name__ == "__main__":
	a =BalanceVerification("theo","bouh-dah", 10.0,10.0,0,3,12,1997)
	print(a.name)
	print("a.balance = "+a.balance)
	print(a.date.getDateString())
