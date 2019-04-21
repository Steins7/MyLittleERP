# coding=UTF-8
from Member import *

class Group(object):

    def __init__(self):
        def __init__():
        	#TODO add to database
        


    def addCaracteristic(self, name = "new caracteristic", attribute = none):
        """
         Enable the user to add a Caracteristic to all the Members of the Group

        @param string name : The name of the new Caracteristic
        @param int attribute : The attribute of the new Caracteristic
        @return bool :
        @author
        """
        def addCaracteristic(name,attribute):
        	for (elem in members):
        		if (!elem.addCaracteristic(name,attribute)):
        			return 1
        	return 0	


    def deleteCaracteristic(self, caracteristicName):
        """
         Allow the user to delete a Caracteristic from all the Members of the group

        @param string caracteristicName : The name of the caracteristic to be deleted
        @return bool :
        @author
        """
        def deleteCaracteristic():
        	for (elem in members):
        		if (elem.deleteCaracteristic()):
        			return 1
        	return 0
        	




