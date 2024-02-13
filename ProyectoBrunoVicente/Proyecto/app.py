import sys
import os
import textwrap
import subprocess
from PySide6.QtWidgets import QApplication,QMessageBox, QGridLayout,QButtonGroup, QRadioButton, QLayout, QDialog, QTabWidget, QHBoxLayout, QMainWindow, QVBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit, QWidget, QGroupBox, QScrollArea
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QIcon, QFont
from uploadGame import UploadGameDialog
from uploadApp import UploadAppDialog
from bdGames import play_game, get_game_count, get_game_details, get_game_script





current_dir = os.path.dirname(os.path.abspath(__file__))
resources_dir = os.path.join(current_dir, 'resources')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()      

        #ruta al juego para jugar
        self.game_path = os.path.join('Games', 'Pong', 'pong.py') # Cambia 'game.py' a la ruta de tu archivo .py del juego
        
        #Componenetes superiores
        #Cargamos el logo y el nombre de usuario
        pixmap = QPixmap(os.path.join(resources_dir, 'avatar.png'))  # Asegúrate de que la ruta a la imagen es correcta
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)      
        self.logo_label = QLabel()
        self.logo_label.setPixmap(pixmap)


        #QLabel para el nombre de usuario
        self.username_label = QLabel()
        font = QFont("Arial", 14, QFont.Bold)  # Cambia "Arial", 14 y QFont.Bold a la fuente, tamaño y estilo que prefieras
        self.username_label.setFont(font)

        #Menu superior derecho
        self.dropdown_menu = QComboBox()
        self.dropdown_menu.setFixedSize(QSize(200, 50))
        self.dropdown_menu.addItem("Salir")
        self.dropdown_menu.addItem("Cambiar de Usuario")
        self.dropdown_menu.activated.connect(self.handle_dropdown_menu)
        

    


        #Componenetes inferiores
        self.modo_desarrollador_label = QLabel("Modo desarrollador ACTIVADO/DESACTIVADO")
        self.upload_game_button = QPushButton("Subir juego")
        self.upload_game_button.setFixedSize(QSize(200, 40))
        self.upload_game_button.setIcon(QIcon(os.path.join(resources_dir, 'consola-de-juego.png')))
        self.upload_game_button.setIconSize(QSize(25, 25))
        self.upload_game_button.clicked.connect(self.open_upload_game_button)
        self.upload_app_button = QPushButton("Subir app")
        self.upload_app_button.setFixedSize(QSize(200, 40))
        self.upload_app_button.setIcon(QIcon(os.path.join(resources_dir, 'escritorio.png')))
        self.upload_app_button.setIconSize(QSize(25, 25))
        self.upload_app_button.clicked.connect(self.open_upload_app_dialog)




        # Creacion del Tab donde la funcion creara el componente central
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.create_scroll_area(), "Juegos")
        self.tab_widget.addTab(self.create_scroll_area(), "Apps")
        self.tab_widget.setStyleSheet("QTabBar::tab { width: 915px; height: 35px; }")


        #layout de la parte superior
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.logo_label)
        self.top_layout.addWidget(self.username_label)
        self.top_layout.addStretch(1)
        #self.top_layout.addWidget(self.logo_label_left)
        self.top_layout.addWidget(self.dropdown_menu)

        #layout parte inferior
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.modo_desarrollador_label)
        self.bottom_layout.addWidget(self.upload_game_button)
        self.bottom_layout.addWidget(self.upload_app_button)

        #layout principal y añadimos los layouts secundarios
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.tab_widget)
        #self.main_layout.addWidget(self.create_scroll_area())
        self.main_layout.addLayout(self.bottom_layout)
        

        # Crear un widget central y establecer el layout principal
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: grey;")
    
    #Definimos el componente dentral que tendra un Scroll
    

    def create_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Hacemos el widget sea redimensionable

        scroll_widget = QWidget()
        scroll_layout = QGridLayout()
        
        game_count = get_game_count()  # Obtén el número de juegos de la base de datos
        print(game_count) # Me esta contando 2 JUEGOS
        rows = game_count // 2  # Calcula el número de filas necesarias
        if game_count % 2 != 0:  # Si hay un número impar de juegos, añade una fila extra
            rows += 1

        game_id = 1
        for i in range(rows):  # Añadir filas
            for j in range(2):  # Añadir 2 columnas
                if game_id <= game_count:  # Solo crea una caja de juego si aún hay juegos
                    game_box = self.create_game_box(game_id)  # Pasa el game_id a la función
                    scroll_layout.addWidget(game_box, i, j)
                    game_id += 1  # Incrementa el game_id

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)

        return scroll_area



    #Creamos el pack del que se compondra una unidad de juego o app
    def create_game_box(self, game_id):
        group_box = QGroupBox()

        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()

        game_details = get_game_details(game_id)  # Obtén los detalles del juego de la base de datos
        
        filename = os.path.basename(game_details[0])
        pixmap = QPixmap(os.path.join(resources_dir, filename))  # Usa la imagen del juego
        pixmap = pixmap.scaled(300, 300)  # Redimensionar la imagen a 300x300
        definicion_juego_texto = game_details[1]  # Usa la descripción del juego
        definicion_juego_texto = textwrap.fill(definicion_juego_texto, 45)
        definicion_juego = QLabel(definicion_juego_texto)
        definicion_juego.setStyleSheet("background-color: grey; margin: 10px;")
        definicion_juego.setAlignment(Qt.AlignTop)

        # Aumentar el tamaño de la letra
        font = QFont()
        font.setPointSize(14) 
        definicion_juego.setFont(font)

        # QLabel para la última reseña
        ultima_resenia = QLabel("Muy buen juego, me encanta")  # La reseña es la misma para todos los juegos
        ultima_resenia.setStyleSheet("background-color: grey; margin: 10px;")

        #damos la horientacion que tendran
        nota = QLabel("Nota: 4.5/5")  # La nota es la misma para todos los juegos
        nota.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        nota.setFont(font)
        vertical_label = QVBoxLayout()
        vertical_label.addWidget(definicion_juego)
        vertical_label.addWidget(ultima_resenia)
        vertical_label.addWidget(nota)

        image_button = QPushButton()
        image_button.setIcon(QIcon(pixmap))
        image_button.setIconSize(pixmap.size())
        image_button.clicked.connect(self.on_image_clicked)
        image_button.game_id = game_id  # Almacena el game_id en el botón

        layout_horizontal.addWidget(image_button)
        layout_horizontal.addLayout(vertical_label)
        self.resena_label = QLabel("Haz clic <font color='blue'>aquí</font> para escribir una reseña")
        self.resena_label.setFixedSize(QSize(300, 30))
        self.resena_label.mousePressEvent = self.resena_clicked

        layout_vertical.addStretch()  # Añadir un espacio en blanco a la izquierda
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.resena_label)
        layout_vertical.addStretch()  # Añadir un espacio en blanco a la derecha

        group_box.setLayout(layout_vertical)

        return group_box
    
    def on_image_clicked(self):

        game_id = self.sender().game_id
        #Crear un nuevo QDialog
        self.dialog = QDialog()
        self.dialog.game_id = game_id
        self.dialog.setStyleSheet("background-color: grey;")

        self.juego_seleccionado = QLabel("Juego seleccionado")
        #crear los botones
        self.play_button = QPushButton("Jugar",self.dialog)
        self.play_button.setFixedSize(QSize(200, 50))
        self.play_button.setIcon(QIcon(os.path.join(resources_dir, 'jugar2.png'))) 
        self.play_button.setIconSize(QSize(35, 35))
        self.play_button.clicked.connect(self.play_clicked)
        self.download_button = QPushButton("Descargar",self.dialog)
        self.download_button.setFixedSize(QSize(200, 50))
        self.download_button.setIcon(QIcon(os.path.join(resources_dir, 'descargar.png')))
        self.download_button.setIconSize(QSize(35, 35))
        self.download_button.clicked.connect(self.download_clicked)
        self.cancel_button = QPushButton("Cancelar",self.dialog)
        self.cancel_button.setFixedSize(QSize(200, 50))
        self.cancel_button.setIcon(QIcon(os.path.join(resources_dir, 'salir.png')))
        self.cancel_button.setIconSize(QSize(35, 35))
        self.cancel_button.clicked.connect(self.cancel_clicked)

        
        

        #Crear el layout
        layout = QVBoxLayout()
        layout.addWidget(self.juego_seleccionado)
        layout.addWidget(self.play_button)
        layout.addWidget(self.download_button)
        layout.addWidget(self.cancel_button)

        #Establecer el layout
        self.dialog.setLayout(layout)

        #Mostrar el dialogo
        self.dialog.exec()


    #Aqui conseguimos cambiar el Label superior dependiendo del usuario que se loguee
    def handle_user_logged_in(self, username):
        self.username_label.setText(f"{username}") 
        

    def open_upload_game_button(self):
        self.upload_game_dialog = UploadGameDialog(self)
        self.upload_game_dialog.show()

    
    def play_clicked(self):
        game_id = self.dialog.game_id 
        # Esta función se llamará cuando se haga clic en el botón "Jugar"
        game_script_path = get_game_script(game_id)

        if game_script_path is not None:
            subprocess.run(["python", game_script_path])
        else:
            print(f"No se encontró un script para el juego con id: {game_id}")


    def download_clicked(self):
    # Esta función se llamará cuando se haga clic en el botón "Descargar"
        #TODO: # Descargar el juego
        print("¡Descargando!")

    def cancel_clicked(self):
    # Esta función se llamará cuando se haga clic en el botón "Cancelar"
        print("¡Cancelando!")
        self.dialog.close()

    def resena_clicked(self, event):
        # Crear un nuevo QDialog
        dialog = QDialog()
        dialog.setStyleSheet("background-color: grey;")

        # Crear un QTextEdit para la reseña
        resena_edit = QTextEdit()
        #resena_edit.setFixedSize(QSize(300, 100))

        # Crear un QButtonGroup para la puntuación
        puntuacion_group = QButtonGroup(dialog)
        puntuacion_layout = QHBoxLayout()
        for i in range(1, 6):  # Crea 5 botones de radio
            button = QRadioButton()
            button.setIcon(QIcon(os.path.join(resources_dir, 'estrella.png')))  # Asume que tienes un icono de estrella
            button.setIconSize(QSize(24, 24))  # Ajusta el tamaño del icono 
            puntuacion_group.addButton(button, i)
            button_layout = QHBoxLayout()
            puntuacion_layout.addWidget(button)
            button_layout.addWidget(QLabel(str(i)))
            puntuacion_layout.addLayout(button_layout)
        

        # Crear un botón para guardar la reseña
        guardar_button = QPushButton("Guardar")
        guardar_button.setIcon(QIcon(os.path.join(resources_dir, 'guardar.png')))
        guardar_button.clicked.connect(lambda: self.guardar_resena(resena_edit.toPlainText(), puntuacion_group.checkedId()))
        cancelar_button = QPushButton("Cancelar")
        cancelar_button.setIcon(QIcon(os.path.join(resources_dir, 'salir.png')))
        cancelar_button.clicked.connect(dialog.close)

        # Añadimos los botones
        botones_resena_layout = QHBoxLayout()
        botones_resena_layout.addWidget(guardar_button)
        botones_resena_layout.addWidget(cancelar_button)

        # Crear un layout para el QDialog y añadir el QTextEdit y el botón
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(resena_edit)
        dialog_layout.addWidget(QLabel("puntuacion: "))
        dialog_layout.addLayout(puntuacion_layout)
        dialog_layout.addLayout(botones_resena_layout)
        dialog.setLayout(dialog_layout)

        # Mostrar el QDialog
        dialog.exec_()    

    # Esta función se llamará cuando se haga clic en el botón "SubirJuego"
    # Abrira una ventana donde colocaremos los datos del juego
    

    def open_upload_app_dialog(self):
        self.upload_app_dialog = UploadAppDialog(self)
        self.upload_app_dialog.show()

    
    def handle_dropdown_menu(self, index):
        text = self.dropdown_menu.itemText(index)
        if text == "Salir":
            QApplication.quit()
        elif text == "Cambiar de Usuario":
            msg_box = QMessageBox(QMessageBox.Information, "Información", "Usuario desconectado")
            msg_box.exec()  # Muestra el mensaje y bloquea la ejecución hasta que el usuario cierre el cuadro de mensaje
            self.close()  # Cierra la ventana principal
            ruta_a_login = os.path.join(os.path.dirname(
            __file__), "login.py")
            resultado_login = subprocess.run(["python", ruta_a_login])   # Muestra un mensaje de información

    def set_username(self, username):
        self.username_label.setText(f"Logueado como {username}")        

    def closeEvent(self, event):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())