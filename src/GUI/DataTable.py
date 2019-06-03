from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


class DataTable(QTableWidget):
    
    def __init__(self,parent=None,name="default",tableType="Members",table=None):
        super(DataTable,self).__init__(parent)

        self.name = name
        self.type = tableType
        self.isSaved = False
        self.table = table
        

        #TODO use Group and Table functions
        if self.type == "Members" :
            self.setColumnCount(7)
            memberList = self.table.sortBy()
            self.setRowCount(len(memberList)+1)
            font = QFont("Times", 12, QFont.Bold)
            item = QTableWidgetItem("Name")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,0,item)
            item = QTableWidgetItem("Firstname")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,1,item)
            item = QTableWidgetItem("Surname")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,2,item)
            item = QTableWidgetItem("eMail")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,3,item)
            item = QTableWidgetItem("Birthdate")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,4,item)
            item = QTableWidgetItem("Cotisation")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            self.setItem(0,5,item)

            r = 1
            for member in memberList:
                c = 0
                for attribute in member.iterateAttributes():
                    item = QTableWidgetItem(attribute)
                    self.setItem(r,c,item)
                    c += 1
                r += 1

        if self.type == "Trésorerie" :
            self.setColumnCount(9)

        #TODO set option to do that automaticaly
        self.resizeColumnsToContents()


        
