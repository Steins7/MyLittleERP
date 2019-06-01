from PySide2.QtWidgets import QMainWindow,QMenuBar,QStatusBar,QVBoxLayout,QDockWidget,QWidget,QPushButton,QTableWidget
from PySide2.QtCore import Qt

from Toolbar import Toolbar
from DataTable import DataTable


class MainWindow(QMainWindow):

    def fileFunc(self):
        print("called fileFunc")



    def editFunc(self):
        print("called editFunc")



    def helpFunc(self):
        print("called helpFunc")



    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        #attributes
        self.menuBar_ = QMenuBar()
        self.statusBar_ = QStatusBar()
        self.toolbar_ = QDockWidget()
        self.toolbarWidget_ = Toolbar()
        self.dataTable_ = DataTable()
        
        #menuBar
        self.menuBar_.addAction("File",self.fileFunc)
        self.menuBar_.addAction("Edit",self.editFunc)
        self.menuBar_.addAction("Help",self.helpFunc)
        self.setMenuBar(self.menuBar_)
        #statusBar
        self.statusBar_.showMessage("status bar")
        self.setStatusBar(self.statusBar_)
        #toolBar
        self.toolbar_.setWidget(self.toolbarWidget_)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.toolbar_)
        self.setCentralWidget(self.dataTable_)



