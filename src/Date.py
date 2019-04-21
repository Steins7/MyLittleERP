# coding=UTF-8

class Date(object):

    #static variables
    days = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
    months = ["Janvier","Février","Mars","Avril","Juin","Juillet","Aout","Septembre",
            "Octobre","Novembre","Décembre"]

    def __init__(self, day = [0,0], month = 0, year = 0):
    
        #public attributes
        self.__day = day
        self.__month = month
        self.__year = year

        


    def getDateString(self):
        """
         Allow to get a string of the Date

        @return string :
        @author
        """
        return (Date.days[self.__day[0]] + " " + str(self.__day[1]) + " " + Date.months[self.__month-1]
                + " " + str(self.__year))



