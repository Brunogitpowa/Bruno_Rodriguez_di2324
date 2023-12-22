import os
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QTextEdit, QMainWindow, QToolBar, QVBoxLayout
from PySide6.QtCore import QSize, Qt, QFile, QTextStream

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto")

         # Barra de menú
        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("Menu") # Creamos el menú
        menu_abrir = menu_archivo.addAction("Abrir") # Creamos la acción
        menu_abrir.triggered.connect(self.abrirArchivo) # Conectamos la acción con la función
        menu_guardar = menu_archivo.addAction("Guardar")
        menu_guardar.triggered.connect(self.guardarArchivo)
        menu_salir = menu_archivo.addAction("Salir")
        menu_salir.setShortcut("Ctrl+Q")
        menu_salir.triggered.connect(self.cerrarApp)
        
        

        # Rutas a los iconos u creamos las acciones
        ruta_a_icono1 = os.path.join(os.path.dirname(__file__), "Imagenes", "abrir.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(__file__), "Imagenes", "guardarFichero.png")
        abrir = QAction(QIcon(ruta_a_icono1), "Abrir Archivo", self)
        abrir.setShortcut("Ctrl+O")
        abrir.triggered.connect(self.abrirArchivo)
        guardar = QAction(QIcon(ruta_a_icono2), "Guardar Archivo", self)
        guardar.setShortcut("Ctrl+S")
        guardar.triggered.connect(self.guardarArchivo)
        

        # Barra de herramientas
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setIconSize(QSize(36, 36))
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addAction(abrir)
        barra_herramientas.addAction(guardar)
        self.addToolBar(barra_herramientas)

        #El editor de texto al agregarlo al CentralWidget ocupa toda la ventana
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)



    def abrirArchivo(self):
        ruta_al_archivo = os.path.join(os.path.dirname(__file__), "Imagenes", "fichero.txt")
        archivo = QFile(ruta_al_archivo)
        if archivo.open(QFile.ReadOnly):
            stream = QTextStream(archivo)
            self.editor.setPlainText(stream.readAll())
            archivo.close()    



    def guardarArchivo(self):
        ruta_al_archivo = os.path.join(os.path.dirname(__file__), "Imagenes", "fichero.txt")
        archivo = QFile(ruta_al_archivo)
        if archivo.open(QFile.WriteOnly): # Si 
            archivo.write(self.editor.toPlainText().encode()) # Escribimos el texto del editor
            archivo.flush()
            archivo.close() 



    def cerrarApp(self):
        self.close()               
        

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()