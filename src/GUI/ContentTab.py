from PySide2.QtWidgets import QTabWidget,QMessageBox

from DataTable import DataTable
from Messages import CloseMessage

class ContentTab(QTabWidget):

    def __init__(self,parent=None):
        super(ContentTab,self).__init__(parent)

        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTable)


    def addTable(self,table):
        self.addTab(table,table.name)



    def closeTable(self,index):
        message = CloseMessage()
        returnValue = message.exec_()
        
        if returnValue == QMessageBox.Cancel:
            return
        if returnValue == QMessageBox.Save:
            #TODO add save feature here
            pass
        
        self.removeTab(index)

