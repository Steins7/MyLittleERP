from PySide2.QtWidgets import QMainWindow,QMenuBar,QStatusBar,QVBoxLayout,QDockWidget,QWidget,QPushButton,QTableWidget, QMenu
from PySide2.QtCore import Qt

from Toolbar import Toolbar
from DataTable import DataTable
from FileMenu import FileMenu
from EditMenu import EditMenu
from ContentTab import ContentTab


class MainWindow(QMainWindow):

    def __init__(self,application,parent=None):
        super(MainWindow,self).__init__(parent)

        #private attributes
        self.menuBar_ = QMenuBar()
        self.fileMenu_ = FileMenu(self)
        self.editMenu_ = EditMenu(self)
        self.statusBar_ = QStatusBar()
        self.toolbar_ = QDockWidget()
        self.toolbarWidget_ = Toolbar()

        #public attributes
        self.application = application
        self.contentTab = ContentTab()
        
        #menuBar
        self.menuBar_.addMenu(self.fileMenu_)
        self.menuBar_.addMenu(self.editMenu_)
        self.menuBar_.addAction("Help",self.helpFunc)
        self.setMenuBar(self.menuBar_)
        #statusBar
        self.statusBar_.showMessage("status bar")
        self.setStatusBar(self.statusBar_)
        #toolBar
        self.toolbar_.setWidget(self.toolbarWidget_)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.toolbar_)
        #contentab
        table = DataTable(name = "example table")
        self.contentTab.addTable(table)
        self.setCentralWidget(self.contentTab)



    def helpFunc(self):
        print("called helpFunc")

    def quit(self):
        self.application.quit()

