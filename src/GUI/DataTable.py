from PySide2.QtWidgets import QTableWidget

class DataTable(QTableWidget):
    
    def __init__(self,parent=None,name="default",tableType="Membres"):
        super(DataTable,self).__init__(parent)

        self.name = name
        self.type = tableType
        self.isSaved = False

        #TODO use Group and Table functions
        if self.type == "Membres" :
            self.setColumnCount(7)
        if self.type == "Trésorerie" :
            self.setColumnCount(9)
        self.setRowCount(1)

        
