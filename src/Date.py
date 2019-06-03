# coding=UTF-8

class Date():
    """
    Define a date using the following information : year,  month, day (month number and week number)
    """


    def __init__(self, day = 0, month = 0, year = 0):
    
        #public attributes
        self.__day = day
        self.__month = month
        self.__year = year

        

    def __lt__(self,other):
        """
        Redefine "<" operator for easy comparisons

        @return bool : the result of the comparison
        """
        if(self.__year == other.__year):
            if(self.__month == other.__month):
                return self.__day < other.__day
            else:
                return self.__month < other.__month
        else:
            return self.__year < other.__year



    def __str__(self):
        return str(self.__day) + '/'+str(self.__month)+'/'+ str(self.__year)



# module test

if(__name__ == "__main__"):

    date = Date(1,3,2004)
    print(date.getDateString())

