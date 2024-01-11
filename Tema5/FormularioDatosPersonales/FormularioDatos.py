# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormularioDatos.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(753, 160)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelNombre = QLabel(self.centralwidget)
        self.labelNombre.setObjectName(u"labelNombre")

        self.horizontalLayout.addWidget(self.labelNombre)

        self.editNombre = QLineEdit(self.centralwidget)
        self.editNombre.setObjectName(u"editNombre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNombre.sizePolicy().hasHeightForWidth())
        self.editNombre.setSizePolicy(sizePolicy)
        self.editNombre.setMaximumSize(QSize(280, 16777215))
        self.editNombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.editNombre)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelApellidos = QLabel(self.centralwidget)
        self.labelApellidos.setObjectName(u"labelApellidos")

        self.horizontalLayout_2.addWidget(self.labelApellidos)

        self.editApellidos = QLineEdit(self.centralwidget)
        self.editApellidos.setObjectName(u"editApellidos")
        sizePolicy.setHeightForWidth(self.editApellidos.sizePolicy().hasHeightForWidth())
        self.editApellidos.setSizePolicy(sizePolicy)
        self.editApellidos.setMaximumSize(QSize(280, 16777215))
        self.editApellidos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.editApellidos)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelDireccion = QLabel(self.centralwidget)
        self.labelDireccion.setObjectName(u"labelDireccion")

        self.horizontalLayout_3.addWidget(self.labelDireccion)

        self.editDireccion = QLineEdit(self.centralwidget)
        self.editDireccion.setObjectName(u"editDireccion")
        sizePolicy.setHeightForWidth(self.editDireccion.sizePolicy().hasHeightForWidth())
        self.editDireccion.setSizePolicy(sizePolicy)
        self.editDireccion.setMaximumSize(QSize(280, 16777215))
        self.editDireccion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.editDireccion)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelDNI = QLabel(self.centralwidget)
        self.labelDNI.setObjectName(u"labelDNI")

        self.horizontalLayout_4.addWidget(self.labelDNI)

        self.editDNI = QLineEdit(self.centralwidget)
        self.editDNI.setObjectName(u"editDNI")
        self.editDNI.setMaximumSize(QSize(280, 16777215))
        self.editDNI.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.editDNI)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelTelefono = QLabel(self.centralwidget)
        self.labelTelefono.setObjectName(u"labelTelefono")

        self.horizontalLayout_5.addWidget(self.labelTelefono)

        self.editTelefono = QLineEdit(self.centralwidget)
        self.editTelefono.setObjectName(u"editTelefono")
        self.editTelefono.setMaximumSize(QSize(280, 16777215))
        self.editTelefono.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.editTelefono)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelCorreo = QLabel(self.centralwidget)
        self.labelCorreo.setObjectName(u"labelCorreo")

        self.horizontalLayout_6.addWidget(self.labelCorreo)

        self.editCorreo = QLineEdit(self.centralwidget)
        self.editCorreo.setObjectName(u"editCorreo")
        self.editCorreo.setMaximumSize(QSize(280, 16777215))
        self.editCorreo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.editCorreo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonAceptar = QPushButton(self.centralwidget)
        self.buttonAceptar.setObjectName(u"buttonAceptar")

        self.horizontalLayout_7.addWidget(self.buttonAceptar)

        self.buttonCancelar = QPushButton(self.centralwidget)
        self.buttonCancelar.setObjectName(u"buttonCancelar")

        self.horizontalLayout_7.addWidget(self.buttonCancelar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_3.setStretch(0, 4)

        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.labelNombre.setBuddy(self.editNombre)
        self.labelApellidos.setBuddy(self.editApellidos)
        self.labelDireccion.setBuddy(self.editDireccion)
        self.labelDNI.setBuddy(self.editDNI)
        self.labelTelefono.setBuddy(self.editTelefono)
        self.labelCorreo.setBuddy(self.editCorreo)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.editNombre, self.editDNI)
        QWidget.setTabOrder(self.editDNI, self.editApellidos)
        QWidget.setTabOrder(self.editApellidos, self.editTelefono)
        QWidget.setTabOrder(self.editTelefono, self.editDireccion)
        QWidget.setTabOrder(self.editDireccion, self.editCorreo)
        QWidget.setTabOrder(self.editCorreo, self.buttonAceptar)
        QWidget.setTabOrder(self.buttonAceptar, self.buttonCancelar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.labelApellidos.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.labelDireccion.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.labelDNI.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.labelTelefono.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.labelCorreo.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.buttonAceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.buttonCancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

