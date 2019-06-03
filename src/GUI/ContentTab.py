from PySide2.QtWidgets import QTabWidget,QMessageBox

from DataTable import DataTable
from Messages import CloseMessage,ErrorMessage
from CSV import csvSaver


class ContentTab(QTabWidget):

    def __init__(self,parent=None):
        super(ContentTab,self).__init__(parent)

        self.tables_ = {}

        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTable)



    def getCurrent(self):
        return self.tables[self.currentIndex]



    def addTable(self,table):
        index = self.addTab(table,table.name)
        self.tables_[index] = table



    def saveCurrent(self,fileName,isSaved=True):
        table = self.tables_[self.currentIndex()]
        print(table.table)
        #try:
        csvSaver(fileName,table.table)
        #except Exception as inst:
         #   message = ErrorMessage(str(inst))
          #  message.exec_()
           # return

        table.isSaved = isSaved;



    def closeTable(self,index):
        table = self.tables_[index]
        if table.isSaved == False:
            message = CloseMessage(table.name)
            returnValue = message.exec_()
        
            if returnValue == QMessageBox.Cancel:
                return False
            if returnValue == QMessageBox.Save:
                #TODO add save feature here
                table.isSaved = True
        
        self.removeTab(index)
        return True

    

    def checkTables(self):
        unsavedTables = []
        for elem in self.tables_:
            if not self.closeTable(elem):
                return False
        return True

