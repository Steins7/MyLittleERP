import os
import csv
from Group import Group
from Member import Member
from Table import Table
from Date import Date

def csvParser(filePath):
    """ filePath is where the file is save, and it
    must include the name of the file
    Also, if the file name does not include "Members" or 
    "Fincances", csvParser will throw an Exception
    """

    print(filePath)
    fileName = os.path.split(filePath)[1]
    csvfile = open(filePath, newline = '')
    reader = csv.DictReader(csvfile)

    if "Members" in fileName:
        members = []
        for row in reader:
            m = Member(row['name'],
                       row['firstName'],
                       row['surname'],
                       row['eMail'],
                       Date(int(row['birthDate'].split('/')[0]),
                            int(row['birthDate'].split('/')[1]),
                            int(row['birthDate'].split('/')[2])),
                       bool(row['cotiz']),
                       row['belongingGroups'])
            members.append(m)
           
        csvfile.close()
        return Group(fileName.split("Members")[0],members)
           
    if "Finances" in fileName:
        t = Table()
        for row in reader:
            l = None
            try:
                t.addBalanceVerification(row['name'],
                                       row['iD'],
                                       float(row["cumul"]),
                                       float(row["balance"]),
                                       float(row['balanceGap']),
                                       int(row['date'].split('/')[0]),
                                       int(row['date'].split('/')[1]),
                                       int(row['date'].split('/')[2]))
            except:
                pass
            
            try:
                t.addFlux(row["name"],
                          row['iD'],
                          float(row['value']),
                          row['shortInfo'],
                          row['longInfo'],
                          row['supplier'],
                          float(row['iN']),
                          float(row['out']),
                          int(row['date'].split('/')[0]),
                          int(row['date'].split('/')[1]),
                          int(row['date'].split('/')[2]))
            except:
                pass
                
        csvfile.close()
        return Table(table)    

    raise Exception("The file name or file content is invalid")


def csvSaver(dirPath,obj, name= ""):
    """saves obj, either a Group or a Table, in a file with the good name
    at the dirPath location
    name is only for a Table object"""
        
    if isinstance(obj,Group):
        fileName == obj.name + "Members"
    elif isinstance(obj,Table):
        fileName == name + "Finances"
    else: raise Exception("the object given is not good... Grumph")

    bF = ''  #bufferFile
    if isinstance(obj,Goup):
        for m in obj.__members:
            bF += m.name + ', '
            bF += m.firstName + ', '
            bF += str(cotiz) + ', '
            bF += surname + ', '
            bF += eMail + ', '
            bF += str(birthDate) + ', '
            bF += str(belongingGroups) + '\n'
            
    if isinstance(obj, Table):
        for l in obj.table:
            if isinstance(l,BalanceVerification):
                bF += l.name + ', '
                bF += l.iD + ', '
                bF += str(l.cumul) + ', '
                bF += str(l.balance) + ', '
                bF += str(l.balanceGap) + ', '
                bF += str(l.date) + '\n'
            if isinstance(l,Flux):
                bF += l.name + ', '
                bF += l.iD   + ', '
                bF += str(l.value) + ', '
                bF += l.shortInfo + ', '
                bF += l.longInfo + ', '
                bF += str(l.iN) + ', '
                bF += str(l.out) + ', '
                bF += str(l.Date) + '\n'
        
    currentFile = open(dirPath+'\\'+fileName,'w')
    currenfFile = bF
    currentFile.close()



def csvList(path):
    
    fichiers = os.listdir(path)
    csvFiles = [f for f in fichiers if ".csv" in f]
    return csvFiles








