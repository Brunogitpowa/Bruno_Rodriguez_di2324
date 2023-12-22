from PySide6.QtWidgets import QApplication, QLineEdit, QLabel, QHBoxLayout, QWidget

class Finestra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")

        # QLineEdit
        self.edit_text = QLineEdit(self)
        self.edit_text.setMaxLength(10)  # número máximo de caracteres
        self.edit_text.setFixedSize(100, 30)  # tamaño del QLineEdit

        # QLabel
        self.etiqueta1 = QLabel(self)
        self.etiqueta1.setFixedSize(100, 30)  # tamaño fijo del QLabel

        # Conectar la señal
        self.edit_text.textChanged.connect(self.frase_introducida)

        # QHBoxLayout y añadir los widgets
        layout = QHBoxLayout(self)
        layout.addWidget(self.edit_text)
        layout.addWidget(self.etiqueta1)

        # Ajustar el tamaño de la ventana a los widgets
        self.adjustSize()

    # Definir el slot que se ejecutará cuando el texto del QLineEdit cambie
    def frase_introducida(self, text):
        self.etiqueta1.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = Finestra()
    finestra1.show()
    app.exec()