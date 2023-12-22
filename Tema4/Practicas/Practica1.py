from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit)
from PySide6.QtGui import QPalette


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.layout_horizontal = QHBoxLayout()
        self.componente_principal = QWidget()
        self.componente_principal.setLayout(self.layout_horizontal)
        self.setCentralWidget(self.componente_principal)

        self.usuario = (QLabel('Usuario: '))
        self.contrasena = (QLabel('Contraseña: '))
        self.usuario_text = QLineEdit()
        self.contrasena_text = QLineEdit()
        self.contrasena_text.setEchoMode(QLineEdit.Password)
        


        self.layout_usuario = QHBoxLayout()
        self.layout_usuario.addWidget(self.usuario)
        self.layout_usuario.addWidget(self.usuario_text)

        self.layou_pass = QHBoxLayout()
        self.layou_pass.addWidget(self.contrasena)
        self.layou_pass.addWidget(self.contrasena_text)

        self.frase = QLabel()
        self.boton_login = QPushButton('Iniciar sesión')
        self.boton_login.clicked.connect(self.iniciar_sesion)

        # Creem un layout vertical
        self.layout_vertical = QVBoxLayout()
        self.layout_vertical.addLayout(self.layout_usuario)
        self.layout_vertical.addLayout(self.layou_pass)
        self.layout_vertical.addWidget(self.boton_login)
        self.layout_vertical.addWidget(self.frase)

          
        self.layout_horizontal.addLayout(self.layout_vertical)


    def iniciar_sesion(self):
        if self.usuario_text.text() == 'admin' and self.contrasena_text.text() == 'admin':
            self.frase.setStyleSheet('color: green')
            self.frase.setText('Usuario Correcto')
        else:
            self.frase.setStyleSheet('color: red')
            self.frase.setText('Usuario Incorrecto')
            


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()