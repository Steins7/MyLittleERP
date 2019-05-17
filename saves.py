import json
import os
from BalanceVerification import *

def serializator(obj):
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
    if isinstance(obj, Date):
        return {'__class__' : "Date",
                'day'   : obj.day,
                'month' : obj.month,
                'year'  ; obj.year }
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
                
    if isinstance(obj, Group):
        return {'__class__' : "Group",
                'name' : obj.name,
                '__members' : serializator(obj.member) }


                                
    raise TypeError(repr(obj) + " n'est pas sérialisable !")


path = os.path.abspath(".")
path,useless = os.path.split(path)

savePath = path + "/json_files"
print(savePath)

l1.name = "salut"

def serializator(obj):
    if isinstance(obj,Line):
        return {'__class__' : "Line",
                'date' : obj.date,
                'name' : obj.name,
                'iD'   : obj.iD }
    if isinstance(obj,Membre):
        return {'__class__' : "Membre",
                '
    raise TypeError(repr(obj) + " n'est pas sérialisable !")



with open(savePath + "/save.json", "w", encoding="utf-8") as fichier:
    json.dump(l1, fichier, default=serializator, indent=4)
    json.dump(l2, fichier, default=serializator, indent=4)
    

