from PySide2.QtWidgets import QTableWidget

class DataTable(QTableWidget):
    
    def __init__(self,parent=None,name="default"):
        super(DataTable,self).__init__(100,100,parent)

        self.name = name

        
