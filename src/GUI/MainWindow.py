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
        self.toolbarDoc_ = QDockWidget(self)
        self.toolbarWidget_ = Toolbar()

        self.setGeometry(0,0,1280,720)

        #public attributes
        self.application = application
        self.contentTab = ContentTab()
        self.statusBar = QStatusBar()

        #menuBar
        self.menuBar_.addMenu(self.fileMenu_)
        self.menuBar_.addMenu(self.editMenu_)
        self.menuBar_.addAction("Help",self.helpFunc)
        self.setMenuBar(self.menuBar_)
        #statusBar
        self.statusBar.showMessage("status bar")
        self.setStatusBar(self.statusBar)
        #toolBar
        self.toolbarDoc_.setFeatures(QDockWidget.DockWidgetMovable)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.toolbarDoc_)
        self.toolbarDoc_.setWidget(self.toolbarWidget_)
        self.toolbarDoc_.dockLocationChanged.connect(self.toolbarWidget_.refreshLayout)
        self.toolbarWidget_.show()
        #contentab
        table = DataTable(name = "example table")
        self.contentTab.addTable(table)
        self.setCentralWidget(self.contentTab)



    def helpFunc(self):
        print("called helpFunc")



    def quit(self):
        self.application.quit()

