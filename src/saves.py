# coding=UTF-8
import json
import os
#from Date import *

#from Member import *

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
savePath = path + "/json_files"
#print('\n' + savePath + '\n')

with open(savePath + "/save.json", "w", encoding="utf-8") as fichier:
#    json.dump(clara, fichier, default=serializator, indent=4)
#    json.dump(clara1, fichier, default=serializator, indent=4)
    json.dump(default, fichier, default=default.serialize, indent=4)

def save():
    print('=============enter save()============')
    variables = [v for v in globals().keys()]
    
    for v in variables:
        if v[0:2] == '__':
            continue
        if( isinstance(globals()[v],type)
           or (isinstance(globals()[v],module))
           or isinstance(globals()[v],function)):
            continue
            
        print(v + ' : ' + str(globals()[v]) + ' : ' +str(type(globals()[v])) )
        
save()
""" sauvegarder le groupe défaut contenant tout les membres
puis sauvegarder les autres groupes avec juste l'id des membres"
"""


"""
with open(savePath + "/save.json", "w", encoding="utf-8") as fichier:
    json.dump(l1, fichier, default=serializator, indent=4)
    json.dump(l2, fichier, default=serializator, indent=4)
    """
