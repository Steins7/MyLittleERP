import os
import csv
import Group

def csvParser(filePath):

    print(filePath)
    print(type(filePath))
    fileName = os.path.split(filePath)[1]
    print(fileName)
    csvfile = open(filePath, newline = '')
    reader = csv.DictReader(csvfile)

    if "Members" in fileName:
        members = []
        for row in reader:
            m = Member()
            m.name = row['name']
            m.firstName = row['firstName']
            m.cotiz = row['cotiz']
            m.surname = row['surname']
            m.eMail = row['eMail']
            m.birthDate = row['birthDate']
            m.belongingGroup = row['belongingGroup']
            members.append(m)
           
        csvfile.close()
        return Group(fileName.split("Members")[0],members)
           
    if "Finances" in fileName:
        t = Table()
        for row in reader:
            l = None
            try:
                l = BalanceVerification()
                l.name = row['name']
                l.iD = row['iD']
                l.cumul = float(row["cumul"])
                l.balance = float(row["balance"])
                l.balanceGap = float(row['balanceGap'])
                l.jour = row["date"] #c'est faux !!! (à faire propre plus tard)
                
                t.addBalanceVerification(l)
            except:
                pass
            
            try:
                l = Flux()
                l.name = row["name"]
                l.iD = row['iD']
                l.value = float(row['value'])
                l.shortInfo = row['shortInfo']
                l.longInfo = row['longInfo']
                l.supplier = row['supplier']
                l.iN = float(row['iN'])
                l.out = float(row['out'])
                l.jour = row['date'] #voir try except au dessus
                t.addFlux(l)
            except:
                pass
                
        csvfile.close()
        return Table(table)    
                
    raise Exception("File name or file content is invalid")

                
                
                
               

              
                
