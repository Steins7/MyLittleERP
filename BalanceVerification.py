
from Line import *

class BalanceVerification(Line):
	
	def __init__(self, name="",iD ="",cumul =0.0 , balance=0.0 , balanceGap=0.0,jour =[0,0],mois=0,annee=0):
		self.line = Line(name,iD,jour,mois,annee)
		self.cumul=cumul
		self.balance=balance
		self.balanceGap=balanceGap
