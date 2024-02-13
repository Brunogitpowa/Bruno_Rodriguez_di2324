import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication,QDialog,QHBoxLayout,QSpacerItem,QSizePolicy, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PySide6.QtGui import QPixmap,QFont
from PySide6.QtCore import Qt, Signal
from bdApp import crear_bd, registrar_usuario, verificar_credenciales
from app import MainWindow

crear_bd()

class LoginPrincipal(QMainWindow):

    def __init__(self,main_window):
        super().__init__()

        self.main_window = main_window  # Guarda la referencia a MainWindow
        self.initLogin()

    def initLogin(self):
        # Cargar y mostrar logo
        ruta_logo = os.path.join(os.path.dirname(
            __file__), "resources/logoProjecte.png")
        pixmap = QPixmap(ruta_logo)
        imagen_label = QLabel(self)
        imagen_label.setPixmap(pixmap.scaledToWidth(250))

        # Campos de usuario y contraseña
        usu_label = QLabel('Usuario:')
        usu_label.setFont(QFont('Arial',20))
        contra_label = QLabel('Contraseña:')
        contra_label.setFont(QFont('Arial',20))
        self.usu_edit = QLineEdit()
        self.usu_edit.setFixedWidth(150)
        self.contra_edit = QLineEdit()
        self.contra_edit.setFixedWidth(150)
        self.contra_edit.setEchoMode(QLineEdit.Password)

        # Botón de inicio de sesión
        boton_login = QPushButton('Iniciar Sesión')
        boton_login.clicked.connect(self.login)

        # separacion de botones
        texto= QLabel('o')

        # Boton Registro
        boton_registro = QPushButton('Registrarse')
        boton_registro.clicked.connect(self.registrarse)

        # Diseño del formulario
        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Spacer before
        layout.addWidget(imagen_label, 0, alignment=Qt.AlignCenter)
        layout.addLayout(self.createCenteredLayout(usu_label))
        layout.addLayout(self.createCenteredLayout(self.usu_edit))
        layout.addLayout(self.createCenteredLayout(contra_label))
        layout.addLayout(self.createCenteredLayout(self.contra_edit))
        layout.addLayout(self.createCenteredLayout(boton_login))
        layout.addLayout(self.createCenteredLayout(texto))
        layout.addLayout(self.createCenteredLayout(boton_registro))
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Spacer after


        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.setWindowTitle('Inicio de Sesión')
        self.showMaximized() # para verse en pantalla completa por defecto

    def createCenteredLayout(self, widget):
        layout = QHBoxLayout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Spacer before
        layout.addWidget(widget)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Spacer after
        return layout    


    def login(self):
    # controlamos el usuario obtenido
        usuario = self.usu_edit.text()
        contraseña = self.contra_edit.text()

        # mostrar mensaje
        self.barra_estado = self.statusBar()
        self.barra_estado.addPermanentWidget(QLabel())

        if verificar_credenciales(usuario, contraseña):
            self.barra_estado.setStyleSheet('color: green')
            self.barra_estado.showMessage("Usuario correcto")
            self.main_window.set_username(usuario)
            self.main_window.showMaximized()

            self.close() 
        else:
            self.barra_estado.setStyleSheet('color: red')
            self.barra_estado.showMessage("Usuario incorrecto")       


    def registrarse(self):
        # aqui se abre el formulario de registro
        # mostrar mensaje
        self.barra_estado = self.statusBar()
        self.barra_estado.addPermanentWidget(QLabel())
        self.barra_estado.showMessage("Se abre el registro")
        # aqui para abrir otro archivo .py
        ruta_a_registro = os.path.join(os.path.dirname(
            __file__), "registro.py")

        subprocess.run(["python",ruta_a_registro])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    login_window = LoginPrincipal(main_window)
    login_window.show()  # Solo muestra la ventana de inicio de sesión al principio
    sys.exit(app.exec())