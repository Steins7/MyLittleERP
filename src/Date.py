# coding=UTF-8

class Date():
    """
    Define a date using the following information : year,  month, day (month number and week number)
    """

    #static variables
    days = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    months = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre",
            "Octobre","Novembre","Décembre"]


    def __init__(self, day = [0,0], month = 0, year = 0):
    
        #public attributes
        self.__day = day
        self.__month = month
        self.__year = year


    def getDateString(self):
        """
        Allow to get a string of the Date

        @return string : the date formated in a string
        """
        return (Date.days[self.__day[0]] + " " + str(self.__day[1]) + " " + Date.months[self.__month-1]
                + " " + str(self.__year))

    def __lt__(self,other):
        """
        Redefine "<" operator for easy comparisons

        @return bool : the result of the comparison
        """
        if(self.__year == other.__year):
            if(self.__month == other.__month):
                return self.__day[1] < other.__day[1]
            else:
                return self.__month < other.__month
        else:
            return self.__year < other.__year



# module test

if(__name__ == "__main__"):

    date = Date([1,2],3,2004)
    print(date.getDateString())

