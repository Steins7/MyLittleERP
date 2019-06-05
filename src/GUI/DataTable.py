from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide2.QtCore import Qt


class DataTable(QTableWidget):
    
    def __init__(self,name,table,parent=None):
        super(DataTable,self).__init__(parent)

        self.name = name
        self.isSaved = False
        self.table = table
        self.itemChanged.connect(self.updateData)



    def updateData(self,item):
       # print(item.row())
       # print(item.column())
        data = item.data(Qt.EditRole)
       # print(data)
        self.table[item.row()-1][item.column()] = data
       # print(self.table[item.row()-1][item.column()])
        self.isSaved = False



class GroupTable(DataTable):

    def __init__(self,name,table,parent=None):
        super(GroupTable,self).__init__(name,table,parent)

        self.setColumnCount(7)
        self.setRowCount(100)
        titles = ["Name","FirstName","Surname","eMail","BirthDate","Cotisation","Groups"]
        self.setHorizontalHeaderLabels(titles)
        self.refresh()



    def refresh(self):
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

    

    def sortBy(self,key):
        self.table.sortBy(key)
        self.refresh()
 
    
