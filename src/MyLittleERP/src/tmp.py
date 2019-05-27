class Child:
    def __init__(self,name="noname"):
        self.name = name
        
    def load(obj_dict):
        if obj_dict["__class__"] == "Child":
            self.name = obj_dict["name"]
        
        
class Test:
    def __init__(self,name="noname",sT=0):
        self.name = name
        self.sleepingTime = sT
        self.child = Child()
   
    def load(obj_dict):
        if obj_dict["__class__"]=="Test":
            self.name = obj_dict["name"]
            self.sleepingTime = obj_dict["sleepingTime"]
            self.child = 
        
        
test1 = Test()


if FirstTime:
    test1.name = "salut"
    test1.sleepingTime = 0
    

test1 = Test.load()

def sleep(test):
    pass            
        
sleep(test1)

def loader(obj_dict):
    if "__class__" in obj_dict:
        if obj_dict["__class__"]=="Test":
            test1 = Test.load(obj_dict)
            
    

fichier = open(savePath + "/tests.json", "r", encoding="utf-8")


t = json.load(fichier, object_hook=loader)

    
    
