# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditorTextoNuevo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Activitat3(object):
    def setupUi(self, Activitat3):
        if not Activitat3.objectName():
            Activitat3.setObjectName(u"Activitat3")
        Activitat3.resize(649, 623)
        self.centralwidget = QWidget(Activitat3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.editorTexto = QTextEdit(self.centralwidget)
        self.editorTexto.setObjectName(u"editorTexto")
        
        

        self.verticalLayout.addWidget(self.editorTexto)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.CortarButton = QPushButton(self.centralwidget)
        self.CortarButton.setObjectName(u"CortarButton")
        self.CortarButton.setEnabled(True)
        self.CortarButton.setMinimumSize(QSize(0, 0))
        self.CortarButton.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.CortarButton.setFont(font1)
        self.CortarButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.CortarButton)

        self.CopiarButton = QPushButton(self.centralwidget)
        self.CopiarButton.setObjectName(u"CopiarButton")
        self.CopiarButton.setFont(font1)
        self.CopiarButton.setIconSize(QSize(20, 16))

        self.horizontalLayout_2.addWidget(self.CopiarButton)

        self.PegarButton = QPushButton(self.centralwidget)
        self.PegarButton.setObjectName(u"PegarButton")
        self.PegarButton.setFont(font1)
        self.PegarButton.setIconSize(QSize(20, 16))

        self.horizontalLayout_2.addWidget(self.PegarButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.SeleccionarTodoButton = QPushButton(self.centralwidget)
        self.SeleccionarTodoButton.setObjectName(u"SeleccionarTodoButton")
        self.SeleccionarTodoButton.setFont(font1)
        self.SeleccionarTodoButton.setIconSize(QSize(20, 16))

        self.horizontalLayout.addWidget(self.SeleccionarTodoButton)

        self.EliminarTodoButton = QPushButton(self.centralwidget)
        self.EliminarTodoButton.setObjectName(u"EliminarTodoButton")
        self.EliminarTodoButton.setFont(font1)
        self.EliminarTodoButton.setIconSize(QSize(20, 16))

        self.horizontalLayout.addWidget(self.EliminarTodoButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        Activitat3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Activitat3)
        self.CortarButton.clicked.connect(self.editorTexto.cut)
        self.CopiarButton.clicked.connect(self.editorTexto.copy)
        self.PegarButton.clicked.connect(self.editorTexto.paste)
        self.SeleccionarTodoButton.clicked.connect(self.editorTexto.selectAll)
        self.EliminarTodoButton.clicked.connect(self.editorTexto.clear)

        QMetaObject.connectSlotsByName(Activitat3)
    # setupUi

    def retranslateUi(self, Activitat3):
        Activitat3.setWindowTitle(QCoreApplication.translate("Activitat3", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("Activitat3", u"Editor de TEXTO", None))
        self.editorTexto.setPlaceholderText("")
        self.CortarButton.setText(QCoreApplication.translate("Activitat3", u"Cortar", None))
        self.CopiarButton.setText(QCoreApplication.translate("Activitat3", u"Copiar", None))
        self.PegarButton.setText(QCoreApplication.translate("Activitat3", u"Pegar", None))
        self.SeleccionarTodoButton.setText(QCoreApplication.translate("Activitat3", u"Seleccionar Todo", None))
        self.EliminarTodoButton.setText(QCoreApplication.translate("Activitat3", u"Eliminar Todo", None))
    # retranslateUi

