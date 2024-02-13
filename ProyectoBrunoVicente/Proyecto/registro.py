import sys
import os
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,  QMainWindow, QCheckBox, QFileDialog
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen
from PySide6.QtCore import Qt, QCoreApplication
from bdApp import registrar_usuario

class Registre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initRegistro()

    def initRegistro(self):
        # Cargar y mostrar logo
        ruta_logo = os.path.join(os.path.dirname(
            __file__), "resources/logoProjecte.png")
        pixmap_logo = QPixmap(ruta_logo)
        imagen_label = QLabel(self)
        imagen_label.setPixmap(pixmap_logo.scaledToWidth(140))

        # Campo de correo electronico
        correo_label = QLabel('Escribe un e-mail : * ')
        self.correo_edit = QLineEdit()

        # Campo de usuario
        usu_label = QLabel('Nombre de Usuario : * ')
        self.usu_edit = QLineEdit()

        # contraseña
        contra_label = QLabel("Escribe una Contraseña : * ")
        self.contra_edit = QLineEdit()
        self.contra_edit.setEchoMode(QLineEdit.Password)
       # mostrar contraseña
        self.mostrar_contra = QPushButton("Mostrar Contraseña")
        self.mostrar_contra.setCheckable(True)
        self.mostrar_contra.clicked.connect(self.accio_mostrar)

        # Crear y Poner Avatar
        ruta_avatar = os.path.join(os.path.dirname(
            __file__), "resources/avatar.png")
        icono_label = QLabel("Modifica el avatar si quieres: ")
        self.pixmap_avatar = QPixmap(ruta_avatar)
        self.icono_avatar = QLabel(self)
        self.icono_avatar.setPixmap(self.pixmap_avatar.scaledToWidth(80))
        self.icono_avatar.mousePressEvent = self.cambiar_imagen
        
        # Crear nombre real
        nom_label = QLabel('Cuál és tu nombre real ? * ')
        self.nom_edit = QLineEdit()

        #crear check box
        check_label = QLabel("Eres desarrolador ? ")
        self.check = QCheckBox("Activa si vas a subir Aplicaciones/Juegos a la plataforma")
        # creamos variable para saber si el usuario es desarrollador o no.
        self.esDesarrollador = False
        self.check.stateChanged.connect(self.activar_check)

        # Botón de registrarse
        boton_registro = QPushButton('Confirmar Registro')
        boton_registro.clicked.connect(self.registro)

        # botones extra
        self.distribuidor_label = QLabel('Nom del distribuidor : ')
        self.distribuidor_edit = QLineEdit()
        self.pais_label = QLabel('País del distribuidor : ')
        self.pais_edit = QLineEdit()
        #ocultarlo porque se activa con el checkbox
        self.distribuidor_label.hide()
        self.distribuidor_edit.hide()
        self.pais_label.hide()
        self.pais_edit.hide()


        # Diseño del formulario
        layout = QVBoxLayout()
        layout.addWidget(imagen_label, 0, alignment=Qt.AlignCenter)
        layout.addWidget(correo_label)
        layout.addWidget(self.correo_edit)
        layout.addWidget(usu_label)
        layout.addWidget(self.usu_edit)
        layout.addWidget(contra_label)
        layout.addWidget(self.contra_edit)
        layout.addWidget(self.mostrar_contra)
        layout.addWidget(icono_label)
        layout.addWidget(self.icono_avatar, alignment=Qt.AlignCenter)
        layout.addWidget(nom_label)
        layout.addWidget(self.nom_edit)
        layout.addWidget(check_label)
        layout.addWidget(self.check)
        # para sacar mas datos cuando se active el checkbox
        layout.addWidget(self.distribuidor_label)
        layout.addWidget(self.distribuidor_edit)
        layout.addWidget(self.pais_label)
        layout.addWidget(self.pais_edit)
        layout.addWidget(boton_registro)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Inicio de Sesión')
        self.show()


    def registro(self):
        if not self.correo_edit.text() or not self.usu_edit.text() or len(self.contra_edit.text()) < 4 or not self.nom_edit.text():
            QMessageBox.warning(self,"Faltan Datos","Error, debes rellenar los *, y la contraseña debe contener mínimo 4 letras")
            print("Error")
            return
        else:
            # Recoger los datos del formulario
            email = self.correo_edit.text()
            username = self.usu_edit.text()
            password = self.contra_edit.text()
            imagen = self.icono_avatar.pixmap().toImage().save("temp.png")  # Guardar la imagen temporalmente
            realname = self.nom_edit.text()
            es_desarrollador = self.esDesarrollador
            nombreDistribuidor = self.distribuidor_edit.text() if es_desarrollador else None
            paisDistribuidor = self.pais_edit.text() if es_desarrollador else None

            try:
                registrar_usuario(email, username, password, imagen, realname, es_desarrollador, nombreDistribuidor, paisDistribuidor)
                QMessageBox.information(self, "Registro exitoso", "Registrado con éxito. Ya puedes iniciar sesión.")
                
                self.close()
                
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
            


    def accio_mostrar(self):
        if self.mostrar_contra.isChecked():
            self.contra_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.contra_edit.setEchoMode(QLineEdit.Password)

    def activar_check(self,estat):
        if estat == 2:
            self.esDesarrollador = True
            self.distribuidor_label.show()
            self.distribuidor_edit.show()
            self.pais_label.show()
            self.pais_edit.show()
        else:
            self.esDesarrollador = False
            self.distribuidor_label.hide()
            self.distribuidor_edit.hide()
            self.pais_label.hide()
            self.pais_edit.hide()

    def cambiar_imagen(self, event):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.ReadOnly
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Archivos de Imágenes (*.png *.jpg *.bmp);;Todos los Archivos (*)", options=opciones)

        if archivo:
            pixmapNuevo = QPixmap(archivo)
            self.pixmap_avatar = pixmapNuevo
            self.icono_avatar.setPixmap(self.pixmap_avatar.scaledToWidth(80))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registre()
    sys.exit(app.exec())