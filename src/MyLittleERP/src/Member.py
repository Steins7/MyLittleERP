# coding=UTF-8
from Group import *
#from Meeting import *
from Date import *

class Member(object):
    """A Member contain all informations about a person : name, firstname, cotiz, surname, eMail, birthDate,
    and belongingGroups
    """
    
    #static variables
    newID = 0

    def __init__(self, name, firstName, cotiz, surname, eMail, birthDate, belongingGroups = []):
    
        #public attributes
        self.ID = Member.newID 
        Member.newID += 1
        self.name = name
        self.firstName = firstName
        self.cotiz = cotiz
        self.surname = surname
        self.eMail = eMail
        self.birthDate = birthDate
        self.belongingGroups = belongingGroups

    def __lt__(self,other):
        return self.ID < other.ID
        
    def serialize(self):
        return {'__class__' : "Member",
                'ID'        : self.ID,
                'name'      : self.name,
                'firstName' : self.firstName,
                'cotiz'     : self.cotiz,
                'surname'   : self.surname,
                'eMail'     : self.eMail,
                'birthDate' : self.birthDate.serialize(),
                'belonginGroups' : self.belongingGroups }

    def load(self):
        pass
    
    
if(__name__ == "__main__"):
   pass

