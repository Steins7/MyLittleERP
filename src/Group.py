# coding=UTF-8
from Member import *

class Group(object):
    """A Group is defined by his name and contains Members"""

    
    def __init__(self, name, members=[]):
        
        #public attributes
        self.name = name

        #private attributes
        self.__members = members


    def addMember(self, member):
        """
        Add the specified member to the group. If the member is already in the group, this function will
        raise an exception
        """
        if(member.ID in self.__members):
            raise Exception("Oops, " + member.name, " " + member.firstName + " is already in " + self.name)
        self.__members.append(member)
        member.belongingGroups.append(self.name)


    def deleteMember(self, member):
        """
        Delete the specified member from the group. IF the member is not in the group, this function will
        raise an exception
        """
        if(not member.ID in self.__members):
            raise Exception("Oops, " + member.name + " " + member.firstName + " is not in " + self.name)
        self.__members.remove(member.ID)
        member.belongingGroups.remove(self.name)


    def sortBy(self, sortingKey):
        """
        Sort the list of Members in the group by the key specified. If the key is not valid, it will sort by ID

        @return list : the list of sorted members
        """
        key = None
        def name(elem):
            return elem.name
        def firstName(elem):
            return elem.firstName
        def cotiz(elem):
            return elem.cotiz
        def surname(elem):
            return elem.surname
        def eMail(elem):
            return elem.eMail
        def birthDate(elem):
            return elem.birthDate
        switcher = {
            "name":name,
            "firstName":firstName,
            "cotiz":cotiz,
            "surname":surname,
            "eMail":eMail,
            "birthDate":birthDate
        }
        func = switcher.get(sortingKey)
        return sorted(self.__members,key=func)


    def iterate_members(self):
        """python's default iterator implementation"""
        for elem in self.__members:
            yield elem


    def __contains__(self,key):
        """python's default "in" implementation"""
        return key in self.__members


    def isEmpty(self):
        """
        @return bool : true if the group is empty
        """
        return any(self.__members)
        
    def serialize(self,a):
        if self.name == 'default':
            return {'__class__' : "Group",
                    'name' : self.name,
                    '__members' : [m.serialize() for m in self.__members] }
        else:
            return {'__class__' : "Group",
                    'name' : self.name,
                   '__members' : [m.name for m in self.__members] }


#if(__name__ == "__main__"):

default = Group("default")
clara = Member("Clara","Oswald", True, "b", "b", Date([1,2],3,2004)) 
clara1 = Member("Klara","Yswald", True, "a", "a", Date([5,2],7,2002)) 
clara2 = Member("CKlara","Aswald", True, "", "", Date([2,2],4,2001)) 
clara3 = Member("KClara","Iswald", False, "", "", Date([6,2],5,2022)) 
try:
    default.addMember(clara)
    default.addMember(clara1)
    default.addMember(clara2)
    default.addMember(clara3)
except Exception as inst:
    print(inst)
for m in default.iterate_members():
    pass#print( m.ID, " : ",  m.birthDate.getDateString())
try:
    default.deleteMember(clara)
except Exception as inst:
    print(inst)
try:
    default.deleteMember(clara)
except Exception as inst:
    print(inst)
for m in default.iterate_members():
    print( m.ID, " : ",  m.birthDate.getDateString())
members = default.sortBy("birthDate")
for m in members:
    pass#print( m.ID, " : ", m.name, " : ", m.firstName, " : ", m.cotiz, " : ", m.surname, " : ", m.eMail, " : ", m.birthDate.getDateString(), " : ", m.belongingGroups )
    
