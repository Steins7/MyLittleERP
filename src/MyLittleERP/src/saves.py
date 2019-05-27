# coding=UTF-8
import json
import os

from Group import *


def serializator(obj):

    # partie membres
    # Group, Member, Date
    if isinstance(obj, Group):
        if obj.name == 'default':
            return {'__class__' : "Group",
                    'name' : obj.name,
                    '__members' : serializator(obj.__members) }
        else:
            return {'__class__' : "Group",
                    'name' : obj.name,
                   '__members' : [m.name for m in obj.__members] }

    if isinstance(obj, Member):
        return {'__class__' : "Group",
                'ID'        : obj.ID,
                'firstName' : obj.firstName,
                'cotiz'     : obj.cotiz,
                'surname'   : obj.surname,
                'eMail'     : obj.eMail,
                'birthDate' : serializator(obj.birthDate),
                'belonginGroups' : obj.BelongingGroups.name }
    
    if isinstance(obj, Date):
        return {'__class__' : "Date",
                'day'   : obj.day,
                'month' : obj.month,
                'year'  : obj.year }
                
    
    if False:   
        if isinstance(obj,Line):
            return {'__class__' : "Line",
                    'date' : obj.date,
                    'name' : obj.name,
                    'iD'   : obj.iD }
        if isinstance(obj,BalanceVerification):
            return {'__class__' : "BalanceVerification",
                    'line'  : serializator(obj.line),
                    'cumul' : obj.cumul,
                    'balance' : obj.balance,
                    'balanceGap' : obj.balanceGap }
        
        if isinstance(obj, Flux):
            return {'__class__' : "Flux",
                    'value'     : obj.value,
                    'shortInfo' : obj.shortInfo,
                    'longInfo'  : obj.longInfo,
                    'supplier'  : obj.supplier,
                    'iN'        : obj.iN,
                    'out'       : obj.out }
        if isinstance(obj, Rule):
            return {'__class__' : "Rule" }
                
                                
    raise TypeError(repr(obj) + " n'est pas sérialisable !")


path = os.path.abspath(".")
path,useless = os.path.split(path)
del useless
savePath = path + "/json_files"
#print('\n' + savePath + '\n')

with open(savePath + "/save.json", "w", encoding="utf-8") as fichier:
    json.dump(default, fichier, default=default.serialize, indent=4)
fichier.close()

def save():
    print('\n=============enter save()============')
    variables = [v for v in globals().keys()]
    tosave = []
    for v in variables:
        if v[0:2] == '__':
            continue
        var = globals()[v]
        if (isinstance(var,type) #):
           or str(type(var))=="<class 'function'>" #isinstance(globals()[v],module)
           or str(type(var))=="<class 'module'>"#or isinstance(globals()[v],function)):
           or str(type(var))=="<class 'Member.Member'>"):
            continue
        tosave.append(var)
        print(v + ' : ' + str(globals()[v]) + ' : ' +str(type(globals()[v])) +'\n')

    fichier = open(savePath + "/save.json", "w", encoding="utf-8")   
    json.dump(default, fichier, default=default .serialize, indent=4)
    fichier.close()
    print('=============leave save()============\n')
        
def load():
    fichier = open(savePath + "/save.json", "r", encoding="utf-8")
    
    #if "__class__" in fichier:
    
    
    
    fichier.close()
    
     

save()

