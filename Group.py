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


    def sortBy(self, sortingKey=None):
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
        self.__members = sorted(self.__members,key=func)
        return self.__members



    def iterateMembers(self):
        """python's default iterator implementation"""
        for elem in self.__members:
            yield elem


    def __contains__(self,key):
        """python's default "in" implementation"""
        return key in self.__members



    def __getitem__(self,key):
        """python's default "[]" implementation"""
        return self.__members[key]



    def __setitem__(self,key,value):
        """python's default "[]" implementation"""
        self.__members[key] = value



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



if(__name__ == "__main__"):
    
    normalMembers = Group("normalMembers")
    clara = Member("Clara","Oswald", "b", "b", Date([1,2],3,2004), True) 
    clara1 = Member("Klara","Yswald", "a", "a", Date([5,2],7,2002), True) 
    clara2 = Member("CKlara","Aswald", "", "", Date([2,2],4,2001), True)
    clara3 = Member("KClara","Iswald", "", "", Date([6,2],5,2022), True) 
    try:
        normalMembers.addMember(clara)
        normalMembers.addMember(clara1)
        normalMembers.addMember(clara2)
        normalMembers.addMember(clara3)
    except Exception as inst:
        print(inst)
    for m in normalMembers.iterateMembers():
        print( m.ID, " : ",  m.birthDate.getDateString())
    try:
        normalMembers.deleteMember(clara)
    except Exception as inst:
        print(inst)
    try:
        normalMembers.deleteMember(clara)
    except Exception as inst:
        print(inst)
    for m in normalMembers.iterateMembers():
        print( m.ID, " : ",  m.birthDate.getDateString())
    members = normalMembers.sortBy("birthDate")
    for m in members:
        print( m.ID, " : ", m.name, " : ", m.firstName, " : ", m.cotiz, " : ", m.surname, " : ", m.eMail, " : ", m.birthDate.getDateString() )
    
