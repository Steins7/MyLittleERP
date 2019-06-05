from Flux import *
from BalanceVerification import *
from Date import Date

class Table(object):

    def __init__(self,name) :
        self.__table=[]
        self.name = name
    


    def addBalanceVerification(self,name="",iD ="",cumul =0.0 , balance=0.0 ,
                            balanceGap=0.0,date="none"):
        a=BalanceVerification(name,iD,cumul,balance,balanceGap,date)
        self.__table.append(a)
        return 0
    


    def addFlux(self,name="",iD ="",value =0.0 ,shortInfo="" , longInfo="" ,
            supplier="" , iN=0.0 , out=0.0 ,date="none"):
        a = Flux(name,iD,value,shortInfo,longInfo,supplier,iN,out,date)
        self.__table.append(a)
        return 0
            


    def getLength(self):
        return len(self.__table)



    def iterateLines(self):
       for elem in self.__table:
           yield elem



if __name__ == "__main__":

    a = Table()
    a.addBalanceVerification("theo","bouh-dah", 10.0,10.0,0,Date(3,12,1997))
    print(a.__table[0].name)

