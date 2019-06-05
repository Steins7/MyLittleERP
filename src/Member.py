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

    def __init__(self, name, firstName, surname="None", eMail="None", 
                 birthDate="None", cotiz=False, belongingGroups = []):
    
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



    def __getitem__(self,key):
        items = [self.name,self.firstName,self.surname,self.eMail,
                 self.birthDate,self.cotiz,self.belongingGroups]
        return items[key]
    


    def __setitem__(self,key,value):
        if key==0:
            self.name = value
        elif key==1:
            self.firstName = value
        elif key==2:
            self.surname = value
        elif key==3:
            self.eMail = value
        elif key==4:
            self.birthDate = value
        elif key==5:
            self.cotiz = value
        elif key==6:
            self.belongingGroups = value



if(__name__ == "__main__"):
   pass

