from Date import Date
class Line(object)  :
	  def __init__(self, name="",iD ="", date="none"):
		  #public attributes
		  self.date = date
		  self.name = name
		  self.iD= iD

if __name__ == "__main__":
	a =Line("theo","bouh-dah",Date(1,0,0))
	print(a.name)
	print(a.date.getDateString())
	
