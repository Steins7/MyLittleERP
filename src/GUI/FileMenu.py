from os.path import dirname,abspath
import sys
from PySide2.QtWidgets import QMenu,QFileDialog,QInputDialog

from DataTable import DataTable, GroupTable
from Messages import ErrorMessage

sys.path.insert(0,'GUI/')
from saves import getPath
from CSV import csvParser,csvList



class FileMenu(QMenu):
    """
    A custom menu designed to fit the menubar
    """

    def __init__(self,mainWindow,parent=None):
        super(FileMenu,self).__init__(parent)

        self.mainWindow_ = mainWindow;

        self.setTitle("File")
        self.addAction("New",self.newFunc)

        self.openMenu = QMenu()
        self.openMenu.setTitle("Open...")
        self.refreshOpenMenu()
        self.addMenu(self.openMenu)

        self.addAction("Import...",self.importFunc)
        self.addAction("Save",self.saveFunc)
        self.addAction("Save all",self.saveAllFunc)
        self.addAction("Export...",self.exportFunc)
        self.addSeparator()
        self.addAction("Quit",self.quitFunc)



    def newFunc(self):
        """
        Creates a new table, it opens a popup for the user to 
        chose the type and name
        """
        items = ["Members","Finance"]
        tableType = QInputDialog.getItem(self,"New table","table type",items,0,False)
        if tableType[1]:
            tableName = QInputDialog.getText(self,"New table","table name")
            if tableName[1]: 
                table = DataTable(name = tableName[0],tableType = tableType[0])
                self.mainWindow_.contentTab.addTable(table)



    def openFunc(self,fileName):
        """
        Open the file at the specified path
        The file has to be JSON (for ot it's CSV though)
        """
        print(fileName)
        #TODO temporary, to be change by json call
        try:
            table,name = csvParser(fileName)
        except Exception as inst:
            message = ErrorMessage(str(inst))
            message.exec_()
            return

        dataTable = GroupTable(name,table) 
        self.mainWindow_.contentTab.addTable(dataTable)



    def refreshOpenMenu(self):
        """
        Refresh the "Open" menu so that new file can be seen
        To be changed when csv is dropped for internal saves
        """
        path = dirname(dirname(dirname((abspath(__file__)))))
        path += "/csv_files"
        #TODO implement json
        files = csvList(path)
        print(files)
        self.openMenu.clear()
        for elem in files:
            self.openMenu.addAction(elem,lambda : self.openFunc(path + "/" + elem))
        self.openMenu.addSeparator()
        self.openMenu.addAction("Refresh",self.refreshOpenMenu)
        


    def importFunc(self):
        """
        Allow the user to choose in the filesystem a csv file and open it
        in MLE
        """
        fileName = QFileDialog.getOpenFileName(self,"Import table",
                                                "~/../../", "CSV files (*.csv)")
        print(fileName[0])
        if fileName[0] == "":
            return 

        try:
            table,name = csvParser(fileName[0])
        except Exception as inst:
            message = ErrorMessage(str(inst))
            message.exec_()
            return

        dataTable = GroupTable(name,table) 
        self.mainWindow_.contentTab.addTable(dataTable)



    def saveFunc(self):
        """
        Saves the specified Table in internal storage
        """
        self.mainWindow_.contentTab.saveCurrent()



    def saveAllFunc(self):
        """
        Saves all tables in internal storage
        """
        self.maiWindow_.contentTab.saveAll()



    def exportFunc(self):
        """
        Allow the user to choose in the filesystem a path to save a table as a csv
        """
        fileName = QFileDialog.getSaveFileName(self,"Export table",
                                                "~/../../", "CSV files (*.csv)")

        if fileName[0] == "":
            return

        self.mainWindow_.contentTab.saveCurrent(fileName[0],False)        



    def quitFunc(self):
        """
        Quit the application after checking if all tables have been saved
        """
        if self.mainWindow_.contentTab.checkTables():
            self.mainWindow_.quit() 

