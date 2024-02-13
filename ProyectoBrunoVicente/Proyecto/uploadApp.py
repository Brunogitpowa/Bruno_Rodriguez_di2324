from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QLabel, QHBoxLayout, QTextEdit

class UploadAppDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("UPLOAD APP")
        self.setMinimumSize(600, 500)

        self.name_label = QLabel("Nombre de la APP", self)
        self.name_input = QLineEdit(self)

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)

        self.description_label = QLabel("Descripción", self)
        self.description_input = QTextEdit(self)
        self.description_input.setFixedHeight(200)

        description_layout = QHBoxLayout()
        description_layout.addWidget(self.description_label)
        description_layout.addWidget(self.description_input)

        self.game_file_input = QLineEdit(self)
        self.game_file_button = QPushButton('Subir App', self)
        self.game_file_button.setFixedWidth(150)  # Ajusta la anchura del botón
        self.game_file_button.clicked.connect(self.select_game_file)

        game_file_layout = QHBoxLayout()
        game_file_layout.addWidget(self.game_file_button)
        game_file_layout.addWidget(self.game_file_input)

        self.image_file_input = QLineEdit(self)
        self.image_file_button = QPushButton('Subir imagen', self)
        self.image_file_button.setFixedWidth(150)  # Ajusta la anchura del botón
        self.image_file_button.clicked.connect(self.select_image_file)

        image_file_layout = QHBoxLayout()
        image_file_layout.addWidget(self.image_file_button)
        image_file_layout.addWidget(self.image_file_input)

        self.upload_button = QPushButton('Subir', self)
        self.cancel_button = QPushButton('Cancelar', self)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.upload_button)
        button_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout(self)
        layout.addLayout(name_layout)
        layout.addSpacing(15)
        layout.addLayout(description_layout)
        layout.addSpacing(15)
        layout.addLayout(game_file_layout)
        layout.addSpacing(15)
        layout.addLayout(image_file_layout)
        layout.addSpacing(15)
        layout.addLayout(button_layout)

        self.upload_button.clicked.connect(self.upload_game)
        self.cancel_button.clicked.connect(self.reject)

    def select_game_file(self):
        game_file_path, _ = QFileDialog.getOpenFileName(self, 'Selecciona la APP', "", "Python Files (*.py)")
        self.game_file_input.setText(game_file_path)

    def select_image_file(self):
        image_file_path, _ = QFileDialog.getOpenFileName(self, 'Selecciona la imagen', "", 'Image Files (*.png *.jpg *.jpeg)')
        self.image_file_input.setText(image_file_path)

    def upload_game(self):
        name = self.name_input.text()
        description = self.description_input.text()
        game_file_path = self.game_file_input.text()
        image_file_path = self.image_file_input.text()

        if not all([name, description, game_file_path, image_file_path]):
            # Muestra un mensaje de error y retorna
            return

        # Aquí es donde enviarías una solicitud HTTP a tu servidor Django con los datos recogidos
        # Podrías usar la biblioteca requests de Python para hacer esto

        self.accept()