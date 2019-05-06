
# coding=UTF-8

class Date(object):

    #static variables
    days = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]
    months = ["Janvier","Février","Mars","Avril","Juin","Juillet","Aout","Septembre",
            "Octobre","Novembre","Décembre"]

    def __init__(self, day = [0,0], month = 0, year = 0):
    
        #public attributes
        self.day = day
        self.month = month
        self.year = year

        


    def getDateString(self):
        """
         Allow to get a string of the Date
        @return string :
        @author
        """
        return (Date.days[self.day[0]] + " " + str(self.day[1]) + " " + Date.months[self.month-1]
                + " " + str(self.year))

