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



    def addTable(self,table):
        """
        Allow to add a new table in the view
        """
        index = self.addTab(table,table.name)
        self.tables_[index] = table



    def saveCurrent(self,fileName,isSaved=True):
        """
        Allow to save the table currently displayed
        """
        table = self.tables_[self.currentIndex()]
        try:
            csvSaver(fileName,table.table)
        except Exception as inst:
            message = ErrorMessage(str(inst))
            message.exec_()
            return

        table.isSaved = isSaved;



    def saveAll(self):
        """
        Save all tables
        """
        for table in tables_:
            try:
                csvSaver(table.name,table.table)
            except Exception as inst:
                message = ErrorMessage(str(inst))
                message.exec_()
                return
            table.isSaved = True



    def closeTable(self,index):
        """
        Close the specified table, after prompting the user if the
        table has not been saved
        """
        table = self.tables_[index]
        if table.isSaved == False:
            message = CloseMessage(table.name)
            returnValue = message.exec_()
        
            if returnValue == QMessageBox.Cancel:
                return False
            if returnValue == QMessageBox.Save:
                self.SaveCurrent(table.name)
        
        self.removeTab(index)
        return True

    

    def checkTables(self):
        """
        check if a table hasn't been saved in the displayed tables
        """

        unsavedTables = []
        for elem in self.tables_:
            if not self.closeTable(elem):
                return False
        return True



    def sortTable(self,key,reverse=False):
        """
        sort the current table by the key specified
        """
        table = self.tables_[self.currentIndex()]
        table.sortBy(key,reverse)
        table.refresh()

