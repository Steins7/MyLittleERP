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

    def __init__(self, name, firstName, surname="None", eMail="None", birthDate="None", cotiz=False, belongingGroups = []):
    
        #public attributes
        self.ID = Member.newID 
        Member.newID += 1
        self.name = name
        self.firstName = firstName
        self.surname = surname
        self.eMail = eMail
        self.birthDate = birthDate
        self.cotiz = cotiz
        self.belongingGroups = belongingGroups

    def __lt__(self,other):
        return self.ID < other.ID

    
    def iterateAttributes(self):
        yield self.name
        yield self.firstName
        yield self.surname
        yield self.eMail
        #TODO reinclude getDateString when date will be processed
        yield self.birthDate#.getDateString()
        yield self.cotiz



if(__name__ == "__main__"):
   pass

