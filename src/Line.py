import Date
class Line  :
	  def __init__(self, name="",iD ="", jour =[0,0],mois=0,annee=0):
		  #public attributes
		  self.date = Date(jour,mois,annee)
		  self.name = name
		  self.iD= iD

