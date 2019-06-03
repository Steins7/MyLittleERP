from PySide2.QtWidgets import QMessageBox, QInputDialog

class CloseMessage(QMessageBox):

    def __init__(self,fileName,parent=None):
        super(CloseMessage,self).__init__(parent)

        self.setText("The file " + fileName + " has not been saved, save it before closing ?")
        self.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Save)



class ErrorMessage(QMessageBox):

    def __init__(self,message,parent=None):
        super(ErrorMessage,self).__init__(parent)

        self.setText("Sorry, there was an error :(")
        self.setDetailedText(message)
        self.setStandardButtons(QMessageBox.Ok)
        self.setDefaultButton(QMessageBox.Ok)
