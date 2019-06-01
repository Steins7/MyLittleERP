from PySide2.QtWidgets import QVBoxLayout,QWidget,QPushButton

class Toolbar(QWidget):


    def __init__(self,parent=None):
        super(Toolbar,self).__init__(parent)
        #buttons
        self.button1 = QPushButton("button1")
        self.button2 = QPushButton("button2")
        self.button3 = QPushButton("button3")
        #layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)

