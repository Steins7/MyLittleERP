from PySide2.QtWidgets import QMenu

#import save/parser

class EditMenu(QMenu):

    def __init__(self,parent=None):
        super(EditMenu,self).__init__(parent)
        
        self.setTitle("Edit")
        self.addAction("Copy",self.copyFunc)
        self.addAction("Cut",self.cutFunc)
        self.addAction("Paste",self.pasteFunc)


    def copyFunc(self):
        print("called copyFunc")



    def cutFunc(self):
        print("called cutFunc")



    def pasteFunc(self):
        print("called pasteFunc")

