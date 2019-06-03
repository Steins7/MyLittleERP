import sys
from PySide2.QtWidgets import QMenu,QFileDialog,QInputDialog

from DataTable import DataTable
from Messages import ErrorMessage

sys.path.insert(0,'GUI/')
from saves import getPath
from CSV import csvParser,csvList


class FileMenu(QMenu):

    def __init__(self,mainWindow=None,parent=None):
        super(FileMenu,self).__init__(parent)

        self.mainWindow_ = mainWindow;

        self.setTitle("File")
        self.addAction("New",self.newFunc)
        self.addAction("Open...",self.openFunc)
        self.addAction("Import...",self.importFunc)
        self.addAction("Save",self.saveFunc)
        self.addAction("Export...",self.exportFunc)
        self.addSeparator()
        self.addAction("Quit",self.quitFunc)



    def newFunc(self):
        items = ["Members","Finance"]
        tableType = QInputDialog.getItem(self,"New table","table type",items,0,False)
        if tableType[1]:
            tableName = QInputDialog.getText(self,"New table","table name")
            if tableName[1]: 
                #TODO implement proper table creation
                table = DataTable(name = tableName[0],tableType = tableType[0])
                self.mainWindow_.contentTab.addTable(table)



    def openFunc(self):
        path = "~/../../csv_files"
        #TODO add list of files



    def importFunc(self):
        fileName = QFileDialog.getOpenFileName(self,"Import table",
                                                "~/../../", "CSV files (*.csv)")
        if fileName[0] == "":
            return 

        #try:
        table = csvParser(fileName[0])
        #except Exception as inst:
         #   message = ErrorMessage(str(inst))
          #  message.exec_()
           # return

        dataTable = DataTable(name="normalMembers",tableType="Members",table=table) 
        self.mainWindow_.contentTab.addTable(dataTable)



    def saveFunc(self):
        self.mainWindow_.contentTab.saveCurrent()



    def exportFunc(self):
        fileName = QFileDialog.getSaveFileName(self,"Export table",
                                                "~/../../", "CSV files (*.csv)")

        if fileName[0] == "":
            return

        self.mainWindow_.contentTab.saveCurrent(fileName[0],False)        
        



    def quitFunc(self):
        if self.mainWindow_.contentTab.checkTables():
            self.mainWindow_.quit() 

