import sys
from PySide2.QtWidgets import QApplication,QWidget,QMenuBar,QPushButton,QVBoxLayout,QMainWindow

from MainWindow import MainWindow

app = QApplication(sys.argv)

        


class Page(QWidget):

    def __init__(self,parent=None):
        super(Page,self).__init__(parent)
        #bars
        self.toolBar = ToolBar()
        #layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolBar)
        self.setLayout(layout)

def fileFunc():
    print("called fileFunc")

def editFunc():
    print("called editFunc")

def helpFunc():
    print("called helpFunc")


mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
