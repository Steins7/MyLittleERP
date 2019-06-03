from PySide2.QtWidgets import QMenu,QFileDialog,QInputDialog

from DataTable import DataTable

#import save/parser

class FileMenu(QMenu):

    def __init__(self,mainWindow=None,parent=None):
        super(FileMenu,self).__init__(parent)

        self.mainWindow_ = mainWindow;

        self.setTitle("Fichier")
        self.addAction("Nouveau",self.newFunc)
        self.addAction("Ouvrir...",self.openFunc)
        self.addAction("Importer...",self.importFunc)
        self.addAction("Sauvegarder",self.saveFunc)
        self.addAction("Exporter sous...",self.exportFunc)
        self.addSeparator()
        self.addAction("Quitter",self.quitFunc)



    def newFunc(self):
        print("called newFunc")
        #text = QInputDialog.getText(self, "Nouveau Tableau", "type :")
        items = ["Membres","Trésorerie"]
        tableType = QInputDialog.getItem(self,"Nouveau Tableau","type de tableau",items,0,False)
        if tableType[1]:
            tableName = QInputDialog.getText(self,"Nouveau Tableau","nom du tableau")
            if tableName[1]: 
                #TODO implement proper table creation
                table = DataTable(name = tableName[0],tableType = tableType[0])
                self.mainWindow_.contentTab.addTable(table)



    def openFunc(self):
        print("called openFunc")
        #TODO implement file reading



    def importFunc(self):
        print("called importFunc")
        fileName = QFileDialog.getOpenFileName(self,"Importer un tableur",
                                                "~", "CSV files (*.csv *)")
        print(fileName)



    def saveFunc(self):
        self.mainWindow_.contentTab.saveCurrent()



    def exportFunc(self):
        print("called saveAsFunc")
        #TODO implement saving feature



    def quitFunc(self):
        if self.mainWindow_.contentTab.checkTables():
            self.mainWindow_.quit() 

