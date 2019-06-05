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
    name = fileName.split(".")[0]
    csvfile = open(filePath, newline = '')
    reader = csv.DictReader(csvfile)

    try:
        members = []
        for row in reader:
            m = Member(row['name'],
                       row['firstName'],
                       row['surname'],
                       row['eMail'],
                       Date(int(row['birthDate'].split('/')[0]),
                            int(row['birthDate'].split('/')[1]),
                            int(row['birthDate'].split('/')[2])),
                       bool(row['cotisation']),
                       row['belongingGroups'])
            members.append(m)
           
        csvfile.close()
        return [Group(name,members),name]
    except:
        pass

    t = Table()
    for row in reader:
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
        return [t,name] 

    raise Exception("The file name or file content is invalid")


def csvSaver(dirPath,obj):
    """saves obj, either a Group or a Table, in a file with the good name
    at the dirPath location
    name is only for a Table object"""

    name = os.path.split(dirPath)[1]
        
    if isinstance(obj,Group):
        fileName = ".csv"
    elif isinstance(obj,Table):
        fileName = ".csv"
    else: raise Exception("the object given is not good... Grumph")

    bF = ''  #bufferFile
    if isinstance(obj,Group):
        bF += "name,firstName,surname,eMail,birthDate,cotisation,belongingGroups\n"
        for m in obj.iterateMembers():
            bF += m.name + ','
            bF += m.firstName + ','
            bF += m.surname + ','
            bF += m.eMail + ','
            bF += str(m.birthDate) + ','
            bF += str(m.cotiz) + ','
            bF += str(m.belongingGroups) + '\n'
            
    if isinstance(obj, Table):
        for l in obj.table:
            if isinstance(l,BalanceVerification):
                bF += l.name + ','
                bF += l.iD + ','
                bF += str(l.cumul) + ','
                bF += str(l.balance) + ','
                bF += str(l.balanceGap) + ','
                bF += str(l.date) + '\n'
            if isinstance(l,Flux):
                bF += l.name + ','
                bF += l.iD   + ','
                bF += str(l.value) + ','
                bF += l.shortInfo + ','
                bF += l.longInfo + ','
                bF += str(l.iN) + ','
                bF += str(l.out) + ','
                bF += str(l.Date) + '\n'
        
    currentFile = open(dirPath+fileName,'w')
    currentFile.write(bF)
    currentFile.close()



def csvList(path):
    
    fichiers = os.listdir(path)
    csvFiles = [f for f in fichiers if ".csv" in f]
    return csvFiles








