from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

class ToolButton(QPushButton):

    def __init__(self,iconPath,toolTip,parent=None):
        super(ToolButton,self).__init__(parent)

        self.setFixedSize(40,40)
        #icon
        icon = QIcon("~/../ressources/"+iconPath)
        self.setIcon(icon)
        self.setIconSize(QSize(38,38))
        #toolTip
        self.setToolTip(toolTip)

