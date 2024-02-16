import sys
import bcrypt
from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QPushButton
from PySide6.QtSql import QSqlDatabase, QSqlQuery

class CreateUserDialog(QDialog):
    def __init__(self, database_path):
        super().__init__()
        self.user = QLineEdit(self)
        self.user.setPlaceholderText("Usuario")
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Contraseña")
        self.btn_create = QPushButton("Crear usuario", self)
        self.layout = QFormLayout(self)
        self.layout.addRow("Usuario", self.user)
        self.layout.addRow("Contraseña", self.password)
        self.layout.addRow(self.btn_create)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(database_path)

    def create_user(self):
        if self.db.open():
            if(self.user.text() != "" and self.password.text() != ""):
                query = QSqlQuery()
                query.prepare("INSERT INTO users (user, password) VALUES (?, ?)")
                query.addBindValue(self.user.text())
                hashed_password = bcrypt.hashpw(self.password.text().encode(), bcrypt.gensalt())
                query.addBindValue(hashed_password.decode('utf-8'))
                query.exec()

            self.close()    

    def create_database(self):
        if self.db.open():
            query = QSqlQuery()
            query.exec("CREATE TABLE IF NOT EXIST users (user TEXT, password BLOB)")
            # Insertamos algunos usuarios de prueba
            users = [("user1", "password1"), ("user2", "password2")]
            for user, password in users:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                query.prepare("INSERT INTO users (user, password) VALUES (?, ?)")
                query.addBindValue(user)
                query.addBindValue(hashed_password.decode('utf-8'))
                query.exec()

def main():
    app = QApplication(sys.argv)
    login = CreateUserDialog("users.db")
    login.create_database()
    login.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()             