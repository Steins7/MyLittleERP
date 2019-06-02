from PySide2.QtWidgets import QMenu,QFileDialog,QInputDialog

from Messages import NewMessage
from DataTable import DataTable

#import save/parser

class FileMenu(QMenu):

    def __init__(self,parent=None):
        super(FileMenu,self).__init__(parent)

        self.parent_ = parent;

        self.setTitle("Fichier")
        self.addAction("Nouveau",self.newFunc)
        self.addAction("Ouvrir...",self.openFunc)
        self.addAction("Importer...",self.importFunc)
        self.addAction("Sauvegarder",self.saveFunc)
        self.addAction("Sauvegarder sous...",self.saveAsFunc)
        self.addSeparator()
        self.addAction("Quitter",self.quitFunc)



    def newFunc(self):
        print("called newFunc")
        #text = QInputDialog.getText(self, "Nouveau Tableau", "type :")
        items = ["Membres","Tésorerie"]
        tableType = QInputDialog.getItem(self,"Nouveau Tableau","type de tableau",items,0,False)
        if tableType[1]:
            tableName = QInputDialog.getText(self,"Nouveau Tableau","nom du tableau")
            if tableName[1]: 
                #TODO implement proper table creation
                table = DataTable(name = tableName[0])
                self.parent_.contentTab.addTable(table)


    def openFunc(self):
        print("called openFunc")
        #TODO link to save code


    def importFunc(self):
        print("called importFunc")
        fileName = QFileDialog.getOpenFileName(self,"Importer un tableur",
                                                "~", "CSV files (*.csv *)")


    def saveFunc(self):
        print("called saveFunc")



    def saveAsFunc(self):
        print("called saveAsFunc")



    def quitFunc(self):
        print("called closeFunc")

