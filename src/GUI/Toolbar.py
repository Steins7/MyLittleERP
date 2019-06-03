from PySide2.QtWidgets import QVBoxLayout,QWidget,QPushButton,QDockWidget

class Toolbar(QDockWidget):

    def __init__(self,parent=None):
        super(Toolbar,self).__init__(parent)

        #buttons
        self.button1 = QPushButton(self,"button1")
        self.button2 = QPushButton(self,"button2")
        self.button3 = QPushButton(self,"button3")
        #layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addStretch()
        self.setLayout(layout)

        

    def refreshLayout(self):
        print("Called refreshLayout")

