import sys
from PySide2.QtWidgets import QMenu,QFileDialog,QInputDialog

from DataTable import DataTable
sys.path.insert(0,'GUI/')
from saves import getPath

from Group import Group
from Member import Member
from Date import Date

normalMembers = Group("normalMembers")
clara = Member("Clara","Oswald", "b", "b", Date([1,2],3,2004), True) 
clara1 = Member("Klara","Yswald", "a", "a", Date([5,2],7,2002), True) 
clara2 = Member("CKlara","Aswald", "", "", Date([2,2],4,2001), True)
clara3 = Member("KClara","Iswald", "", "", Date([6,2],5,2022), True) 
try:
    normalMembers.addMember(clara)
    normalMembers.addMember(clara1)
    normalMembers.addMember(clara2)
    normalMembers.addMember(clara3)
except Exception as inst:
    print(inst)


#import save/parser

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
        #text = QInputDialog.getText(self, "Nouveau Tableau", "type :")
        items = ["Members","Finance"]
        tableType = QInputDialog.getItem(self,"New table","table type",items,0,False)
        if tableType[1]:
            tableName = QInputDialog.getText(self,"New table","table name")
            if tableName[1]: 
                #TODO implement proper table creation
                table = DataTable(name = tableName[0],tableType = tableType[0])
                self.mainWindow_.contentTab.addTable(table)



    def openFunc(self):
        path = getPath() + "/csv_files"
        fileName = QFileDialog.getOpenFileName(self,"Import table",
                                                path, "CSV files (*.csv)")
        print(fileName)
        if fileName[0] == "":
            return 

        #tmp
        table = DataTable(name="normalMembers",tableType="Members",table=normalMembers) 
        self.mainWindow_.contentTab.addTable(table)



    def importFunc(self):
        fileName = QFileDialog.getOpenFileName(self,"Import table",
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

