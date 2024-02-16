from pathlib import Path
import pytest
import os
import bcrypt
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery
from login import CreateUserDialog

@pytest.fixture
def app(qtbot, tmp_path: Path):
    db_path = tmp_path / "test.db"
    dialog = CreateUserDialog(str(db_path))
    dialog.create_database()
    qtbot.addWidget(dialog)
    return dialog

def test_create_user(app, qtbot):
    
    # Inserta un nuevo usuario
    qtbot.keyClicks(app.user, "test_user")
    qtbot.keyClicks(app.password, "test_password")
    qtbot.mouseClick(app.btn_create, Qt.LeftButton)

    # El usuario esta bien insertado
    if app.db.open():
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE user = ?")
        query.addBindValue("test_user")
        query.exec_()
        while query.next():
            assert query.value(0) == "test_user"
            assert bcrypt.checkpw("test_password".encode('utf-8'), query.value(1).encode('utf-8'))

    # Elimina la base de datos temporal
    os.remove(app.db.databaseName())
