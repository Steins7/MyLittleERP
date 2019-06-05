from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide2.QtCore import Qt


class DataTable(QTableWidget):
    """
    A general table that will be displayed in the contentTab
    """
    
    def __init__(self,name,table,tableType,parent=None):
        super(DataTable,self).__init__(parent)

        self.name = name
        self.isSaved = False
        self.table = table
        self.tableType = tableType

        nbColumn = self.table.getLength()
        self.setRowCount(nbColumn)
        if self.tableType == "Members":
            self.setColumnCount(7)
            titles = ["Name","FirstName","Surname","eMail","BirthDate","Cotisation","Groups"]
        elif self.tableType == "Finances":
            self.setColumnCount(6)
            titles = ["ID","Name","Cumulated_sum","Balance","Balance_gap","Date"]
        else:
            raise Exception("The table type is invalid")

        self.setHorizontalHeaderLabels(titles)
        self.itemChanged.connect(self.updateData)

        self.refresh()



    def updateData(self,item):
        """
        update the content of the table, based on the users modifications
        """
        data = item.data(Qt.EditRole)
        self.table[item.row()][item.column()] = data
        self.isSaved = False



    def refresh(self):
        """
        refresh the values displayed
        """
        if(self.tableType == "Members"):
            if self.table.getLength() > 0:
                r = 0
                for member in self.table.iterateMembers():
                    c = 0
                    for attribute in member.iterateAttributes():
                        item = QTableWidgetItem(str(attribute))
                        self.setItem(r,c,item)
                        c += 1
                    r += 1
            
            for i in range(6):
                self.horizontalHeader().setMinimumSectionSize(100)
                self.horizontalHeader().setSectionResizeMode(i,QHeaderView.ResizeToContents)
            self.horizontalHeader().setSectionResizeMode(6,QHeaderView.Stretch)
        else:
            #TODO add support for tresury table
            for i in range(5):
                self.horizontalHeader().setMinimumSectionSize(200)
                self.horizontalHeader().setSectionResizeMode(i,QHeaderView.ResizeToContents)
            self.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
         


    def sortBy(self,key,reverse=False):
        """
        sort the table folowing the specified parameters
        """
        if(self.tableType == "Members"):
            self.table.sortBy(key,reverse)
            self.refresh()
        else:
            #TODO add support for tresury table
            pass
 
