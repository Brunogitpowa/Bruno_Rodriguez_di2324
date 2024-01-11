# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecursosTecladoNumerico.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import Iconos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 744)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(self.centralwidget)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(300, 250))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")

        self.verticalLayout.addWidget(self.textEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.button1 = QPushButton(self.centralwidget)
        self.button1.setObjectName(u"button1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy1)
        self.button1.setMinimumSize(QSize(100, 50))
        self.button1.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon = QIcon()
        icon.addFile(u":/NumerosPython/uno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button1, 0, 0, 1, 1)

        self.button2 = QPushButton(self.centralwidget)
        self.button2.setObjectName(u"button2")
        sizePolicy1.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy1)
        self.button2.setMinimumSize(QSize(100, 50))
        self.button2.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon1 = QIcon()
        icon1.addFile(u":/NumerosPython/dos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button2.setIcon(icon1)
        self.button2.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button2, 0, 1, 1, 1)

        self.button3 = QPushButton(self.centralwidget)
        self.button3.setObjectName(u"button3")
        sizePolicy1.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy1)
        self.button3.setMinimumSize(QSize(100, 50))
        self.button3.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon2 = QIcon()
        icon2.addFile(u":/NumerosPython/tres.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button3.setIcon(icon2)
        self.button3.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button3, 0, 2, 1, 1)

        self.button4 = QPushButton(self.centralwidget)
        self.button4.setObjectName(u"button4")
        sizePolicy1.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy1)
        self.button4.setMinimumSize(QSize(100, 50))
        self.button4.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon3 = QIcon()
        icon3.addFile(u":/NumerosPython/cuatro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button4.setIcon(icon3)
        self.button4.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button4, 1, 0, 1, 1)

        self.button5 = QPushButton(self.centralwidget)
        self.button5.setObjectName(u"button5")
        sizePolicy1.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy1)
        self.button5.setMinimumSize(QSize(100, 50))
        self.button5.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon4 = QIcon()
        icon4.addFile(u":/NumerosPython/cinco.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button5.setIcon(icon4)
        self.button5.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button5, 1, 1, 1, 1)

        self.button6 = QPushButton(self.centralwidget)
        self.button6.setObjectName(u"button6")
        sizePolicy1.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy1)
        self.button6.setMinimumSize(QSize(100, 50))
        self.button6.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon5 = QIcon()
        icon5.addFile(u":/NumerosPython/seis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button6.setIcon(icon5)
        self.button6.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button6, 1, 2, 1, 1)

        self.button8 = QPushButton(self.centralwidget)
        self.button8.setObjectName(u"button8")
        self.button8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy1)
        self.button8.setMinimumSize(QSize(100, 50))
        self.button8.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon6 = QIcon()
        icon6.addFile(u":/NumerosPython/ocho.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button8.setIcon(icon6)
        self.button8.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button8, 2, 1, 1, 1)

        self.button9 = QPushButton(self.centralwidget)
        self.button9.setObjectName(u"button9")
        sizePolicy1.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy1)
        self.button9.setMinimumSize(QSize(100, 50))
        self.button9.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon7 = QIcon()
        icon7.addFile(u":/NumerosPython/nueve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button9.setIcon(icon7)
        self.button9.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button9, 2, 2, 1, 1)

        self.button0 = QPushButton(self.centralwidget)
        self.button0.setObjectName(u"button0")
        sizePolicy1.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy1)
        self.button0.setMinimumSize(QSize(100, 50))
        self.button0.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon8 = QIcon()
        icon8.addFile(u":/NumerosPython/cero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button0.setIcon(icon8)
        self.button0.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button0, 3, 1, 1, 1)

        self.button7 = QPushButton(self.centralwidget)
        self.button7.setObjectName(u"button7")
        sizePolicy1.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy1)
        self.button7.setMinimumSize(QSize(100, 50))
        self.button7.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        icon9 = QIcon()
        icon9.addFile(u":/NumerosPython/siete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button7.setIcon(icon9)
        self.button7.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button7, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitulo.setText(QCoreApplication.translate("MainWindow", u"Teclado Numerico", None))
        self.button1.setText("")
        self.button2.setText("")
        self.button3.setText("")
        self.button4.setText("")
        self.button5.setText("")
        self.button6.setText("")
        self.button8.setText("")
        self.button9.setText("")
        self.button0.setText("")
        self.button7.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

