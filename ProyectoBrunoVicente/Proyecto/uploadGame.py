from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QLabel, QHBoxLayout, QTextEdit
from bdGames import add_game

class UploadGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

       

        self.setWindowTitle("UPLOAD GAME")
        self.setMinimumSize(600, 500)

        self.name_label = QLabel("Nombre del juego", self)
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
        self.game_file_button = QPushButton('Subir juego', self)
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

    def get_game_name(self):
        return self.name_input.text()

    def get_game_path(self):
        return self.game_file_input.text()

    def get_image_path(self):
        return self.image_file_input.text()

    def get_game_description(self):
        return self.description_input.toPlainText()

    def select_game_file(self):
        game_file_path, _ = QFileDialog.getOpenFileName(self, 'Selecciona el archivo del juego', "", "Zip Files (*.zip);;Python Files (*.py)")
        self.game_file_input.setText(game_file_path)

    def select_image_file(self):
        image_file_path, _ = QFileDialog.getOpenFileName(self, 'Selecciona la imagen del juego')
        self.image_file_input.setText(image_file_path)

    def upload_game(self):
        name = self.get_game_name()
        description = self.get_game_description()
        zip_path = self.get_game_path()
        image_path = self.get_image_path()

        # Llama a la función add_game directamente
        add_game(name, zip_path, image_path, description)
        self.accept()