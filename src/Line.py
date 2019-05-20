# coding=UTF-8
from Date import *

class Line(object)  :
	  def __init__(self, name="",iD ="", jour =[0,0],mois=0,annee=0):
		  #public attributes
		  self.date = Date(jour,mois,annee)
		  self.name = name
		  self.iD= iD

if __name__ == "__main__":
	a =Line("theo","bouh-dah",[0,1],0,0)
	print a.name
	print a.date.getDateString()
	
