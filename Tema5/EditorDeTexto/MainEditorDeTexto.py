import sys
from PySide6 import QtWidgets

from editorTexto import Ui_Activitat3 


class MainWindow(QtWidgets.QMainWindow, Ui_Activitat3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # esta linea añade el texto de ayuda al TextEdit del editor de texto
        '''self.editorTexto.setPlaceholderText("Escribir aqui ...")'''


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()