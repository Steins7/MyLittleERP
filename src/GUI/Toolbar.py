from PySide2.QtWidgets import QVBoxLayout,QWidget,QPushButton,QMenu
from PySide2.QtCore import Qt

from ToolButton import ToolButton

class Toolbar(QWidget):
    """
    a custom Widget to be used as a toolbar on the left side of the appication
    """

    def __init__(self,mainWindow,parent=None):
        super(Toolbar,self).__init__(parent)

        self.__mainWindow = mainWindow

        #buttons
        self.generateButton = ToolButton("BalanceVerification.xpm","Generate balance verification",self)
        self.sortButton = ToolButton("SortBy.xpm","Sort table",self)
        self.sortMenu = QMenu()
        self.sortMenu.addAction("Name",
                                lambda :self.__mainWindow.contentTab.sortTable("name"))
        self.sortMenu.addAction("Firstname",
                                lambda :self.__mainWindow.contentTab.sortTable("firstName"))
        self.sortMenu.addAction("Surname",
                                lambda :self.__mainWindow.contentTab.sortTable("surname"))
        self.sortMenu.addAction("eMail",
                                lambda :self.__mainWindow.contentTab.sortTable("eMail"))
        self.sortMenu.addAction("cotisation",
                                lambda :self.__mainWindow.contentTab.sortTable("cotisation"))
        self.sortMenu.addAction("Groups",
                                lambda :self.__mainWindow.contentTab.sortTable("belongingGroups"))
        self.sortButton.setMenu(self.sortMenu)
        self.sortButton_inv = ToolButton("SortBy_inv.xpm","Sort table",self)
        self.sortMenu_inv = QMenu()
        self.sortMenu_inv.addAction("Name",
                                    lambda :self.__mainWindow.contentTab.sortTable("name",True))
        self.sortMenu_inv.addAction("Firstname",
                                    lambda :self.__mainWindow.contentTab.sortTable("firstName",True))
        self.sortMenu_inv.addAction("Surname",
                                    lambda :self.__mainWindow.contentTab.sortTable("surname",True))
        self.sortMenu_inv.addAction("eMail",
                                    lambda :self.__mainWindow.contentTab.sortTable("eMail",True))
        self.sortMenu_inv.addAction("cotisation",
                                    lambda :self.__mainWindow.contentTab.sortTable("cotisation",True))
        self.sortMenu_inv.addAction("Groups",
                                    lambda :self.__mainWindow.contentTab.sortTable("belongingGroups",True))
        self.sortButton_inv.setMenu(self.sortMenu_inv)
        self.addButton = ToolButton("Add.xpm","Add an element",self)
        self.addButton.released.connect(self.addItem)
        self.substractButton = ToolButton("Substract.xpm","Substract selected element",self)
        self.substractButton.released.connect(self.delItem)
        #layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.sortButton)
        layout.addWidget(self.sortButton_inv)
        layout.addWidget(self.addButton)
        layout.addWidget(self.substractButton)
        layout.addWidget(self.generateButton)
        layout.addStretch()
        self.setLayout(layout)


        
    def addItem(self):
        print("add")



    def delItem(self):
        self.__mainWindow.contentTab.delItem()


