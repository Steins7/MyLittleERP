from PySide2.QtWidgets import QMenu

#import save/parser

class FileMenu(QMenu):

    def __init__(self,parent=None):
        super(FileMenu,self).__init__(parent)
        
        self.setTitle("Fichier")
        self.addAction("Nouveau",self.newFunc)
        self.addAction("Ouvrir...",self.openFunc)
        self.addAction("Sauvegarder",self.saveFunc)
        self.addAction("Sauvegarder sous...",self.saveAsFunc)
        self.addSeparator()
        self.addAction("Quitter",self.quitFunc)



    def newFunc(self):
        print("called newFunc")



    def openFunc(self):
        print("called openFunc")



    def saveFunc(self):
        print("called saveFunc")



    def saveAsFunc(self):
        print("called saveAsFunc")



    def quitFunc(self):
        print("called closeFunc")

