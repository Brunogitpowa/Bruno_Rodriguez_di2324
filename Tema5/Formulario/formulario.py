# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formularioModificado.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.limpiar_boton = QPushButton(self.centralwidget)
        self.limpiar_boton.setObjectName(u"limpiar_boton")

        self.horizontalLayout.addWidget(self.limpiar_boton)

        self.maximizar = QPushButton(self.centralwidget)
        self.maximizar.setObjectName(u"maximizar")

        self.horizontalLayout.addWidget(self.maximizar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.textEdit, self.limpiar_boton)
        QWidget.setTabOrder(self.limpiar_boton, self.maximizar)

        self.retranslateUi(MainWindow)
        self.limpiar_boton.clicked.connect(self.textEdit.clear)
        self.maximizar.clicked.connect(MainWindow.showMaximized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Actividad3", None))
        self.limpiar_boton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.maximizar.setText(QCoreApplication.translate("MainWindow", u"Maximizar", None))
    # retranslateUi

