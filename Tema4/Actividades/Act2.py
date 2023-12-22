from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton



class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layouts")

        # Creem un layout horizontal
        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        

        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))

        #Al HBox le añadimos el VBox y los botones directamente
        layout_horizontal.addLayout(layout_vertical)
        layout_horizontal.addWidget(QPushButton('H1'))
        layout_horizontal.addWidget(QPushButton('H2'))
        layout_horizontal.addWidget(QPushButton('H3'))
        layout_horizontal.addWidget(QPushButton('H4'))

        componente_principal = QWidget()
        componente_principal.setLayout(layout_horizontal)
        self.setCentralWidget(componente_principal)



app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()