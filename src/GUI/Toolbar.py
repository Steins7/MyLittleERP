from PySide2.QtWidgets import QVBoxLayout,QHBoxLayout,QStackedLayout,QGroupBox,QWidget,QPushButton,QFrame
from PySide2.QtCore import Qt

from ToolButton import ToolButton

class Toolbar(QWidget):

    def __init__(self,parent=None):
        super(Toolbar,self).__init__(parent)

        #buttons
        self.button1 = ToolButton("BalanceVerification.xpm","Generate balance verification",self)
        self.button2 = ToolButton("SortBy.xpm","Sort table",self)
        #layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addStretch()
        self.setLayout(layout)

