from PySide2.QtWidgets import QVBoxLayout,QWidget,QPushButton,QMenu
from PySide2.QtCore import Qt

from ToolButton import ToolButton

class Toolbar(QWidget):
    """
    a custom Widget to be used as a toolbar on the left side of the appication
    """

    def __init__(self,mainWindow,parent=None):
        super(Toolbar,self).__init__(parent)

        self.mainWindow = mainWindow

        #buttons
        self.generateButton = ToolButton("BalanceVerification.xpm","Generate balance verification",self)
        self.sortButton = ToolButton("SortBy.xpm","Sort table",self)
        self.sortMenu = QMenu()
        self.sortMenu.addAction("Name",lambda :self.mainWindow.contentTab.sortTable("name"))
        self.sortMenu.addAction("Firstname",lambda :self.mainWindow.contentTab.sortTable("firstName"))
        self.sortMenu.addAction("Surname",lambda :self.mainWindow.contentTab.sortTable("surname"))
        self.sortMenu.addAction("eMail",lambda :self.mainWindow.contentTab.sortTable("eMail"))
        self.sortMenu.addAction("cotisation",lambda :self.mainWindow.contentTab.sortTable("cotisation"))
        self.sortMenu.addAction("Groups",lambda :self.mainWindow.contentTab.sortTable("belongingGroups"))
        self.sortButton.setMenu(self.sortMenu)
        self.sortButton_inv = ToolButton("SortBy_inv.xpm","Sort table",self)
        self.sortMenu_inv = QMenu()
        self.sortMenu_inv.addAction("Name",lambda :self.mainWindow.contentTab.sortTable("name",True))
        self.sortMenu_inv.addAction("Firstname",lambda :self.mainWindow.contentTab.sortTable("firstName",True))
        self.sortMenu_inv.addAction("Surname",lambda :self.mainWindow.contentTab.sortTable("surname",True))
        self.sortMenu_inv.addAction("eMail",lambda :self.mainWindow.contentTab.sortTable("eMail",True))
        self.sortMenu_inv.addAction("cotisation",lambda :self.mainWindow.contentTab.sortTable("cotisation",True))
        self.sortMenu_inv.addAction("Groups",lambda :self.mainWindow.contentTab.sortTable("belongingGroups",True))
        self.sortButton_inv.setMenu(self.sortMenu_inv)
        #layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.generateButton)
        layout.addWidget(self.sortButton)
        layout.addWidget(self.sortButton_inv)
        layout.addStretch()
        self.setLayout(layout)

