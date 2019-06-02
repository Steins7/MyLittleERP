from PySide2.QtWidgets import QMessageBox, QInputDialog

class CloseMessage(QMessageBox):

    def __init__(self,parent=None):
        super(CloseMessage,self).__init__(parent)

        self.setText("Le fichier n'a pas été sauvegardé, voulez vraiment fermer ?")
        self.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Save)

