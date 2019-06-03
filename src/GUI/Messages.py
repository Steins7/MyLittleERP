from PySide2.QtWidgets import QMessageBox, QInputDialog

class CloseMessage(QMessageBox):

    def __init__(self,fileName,parent=None):
        super(CloseMessage,self).__init__(parent)

        self.setText("Le fichier " + fileName + " n'a pas été sauvegardé, voulez vraiment fermer ?")
        self.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Save)

