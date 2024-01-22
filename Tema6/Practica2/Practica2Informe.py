# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Practica2Formulario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6 import QtWidgets
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as sql
import webbrowser




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet("QScrollArea { background-color: white; }")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        
        
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(5000, 5000))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.TabChinook = QWidget()
        self.TabChinook.setObjectName(u"TabChinook")
        self.verticalLayout_6 = QVBoxLayout(self.TabChinook)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.TabChinook)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 715, 481))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        #Creamos la tabla que va a contener la info
        self.tableWidget1 = QtWidgets.QTableWidget(self.TabChinook)
        #Añadimos la info de la tabla al scrollArea
        self.scrollArea.setWidget(self.tableWidget1)
        
        self.verticalLayout.addWidget(self.scrollArea)
        

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ChinookNavegacion = QPushButton(self.TabChinook)
        self.ChinookNavegacion.setObjectName(u"ChinookNavegacion")
        self.ChinookNavegacion.clicked.connect(self.ChinookNavegacionPage)

        self.horizontalLayout.addWidget(self.ChinookNavegacion)

        self.ChinookPDF = QPushButton(self.TabChinook)
        self.ChinookPDF.setObjectName(u"ChinookPDF")
        self.ChinookPDF.clicked.connect(self.chinookToPDF)

        self.horizontalLayout.addWidget(self.ChinookPDF)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.TabChinook, "")
        self.TabColdplay = QWidget()
        self.TabColdplay.setObjectName(u"TabColdplay")
        self.verticalLayout_7 = QVBoxLayout(self.TabColdplay)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_4 = QScrollArea(self.TabColdplay)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 715, 481))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.tableWidget2 = QtWidgets.QTableWidget(self.TabColdplay)
        self.scrollArea_4.setWidget(self.tableWidget2)
        

        self.verticalLayout_4.addWidget(self.scrollArea_4)
        

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ChinookNavegacion_4 = QPushButton(self.TabColdplay)
        self.ChinookNavegacion_4.setObjectName(u"ChinookNavegacion_4")
        self.ChinookNavegacion_4.clicked.connect(self.ColdplayNavegacionPage)   

        self.horizontalLayout_4.addWidget(self.ChinookNavegacion_4)

        self.ChinookPDF_4 = QPushButton(self.TabColdplay)
        self.ChinookPDF_4.setObjectName(u"ChinookPDF_4")
        self.ChinookPDF_4.clicked.connect(self.coldplayToPDF)
    

        self.horizontalLayout_4.addWidget(self.ChinookPDF_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.TabColdplay, "")
        self.TabPoblacion = QWidget()
        self.TabPoblacion.setObjectName(u"TabPoblacion")
        self.horizontalLayout_7 = QHBoxLayout(self.TabPoblacion)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_5 = QScrollArea(self.TabPoblacion)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 715, 481))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)
        self.tableWidget3 = QtWidgets.QTableWidget(self.TabPoblacion)
        self.scrollArea_5.setWidget(self.tableWidget3)

        self.verticalLayout_5.addWidget(self.scrollArea_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ChinookNavegacion_5 = QPushButton(self.TabPoblacion)
        self.ChinookNavegacion_5.setObjectName(u"ChinookNavegacion_5")
        self.ChinookNavegacion_5.clicked.connect(self.PoblacionNavegacionPage)  

        self.horizontalLayout_5.addWidget(self.ChinookNavegacion_5)

        self.ChinookPDF_5 = QPushButton(self.TabPoblacion)
        self.ChinookPDF_5.setObjectName(u"ChinookPDF_5")
        #Damos la funcion al boton de crear PDF
        self.ChinookPDF_5.clicked.connect(self.poblacionToPDF)

        self.horizontalLayout_5.addWidget(self.ChinookPDF_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.TabPoblacion, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ChinookNavegacion.setText(QCoreApplication.translate("MainWindow", u"Abrir en Navegador", None))
        self.ChinookPDF.setText(QCoreApplication.translate("MainWindow", u"Crear PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabChinook), QCoreApplication.translate("MainWindow", u"Chinook SQLITE", None))
        self.ChinookNavegacion_4.setText(QCoreApplication.translate("MainWindow", u"Abrir en Navegador", None))
        self.ChinookPDF_4.setText(QCoreApplication.translate("MainWindow", u"Crear PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabColdplay), QCoreApplication.translate("MainWindow", u"Coldplay JSON", None))
        self.ChinookNavegacion_5.setText(QCoreApplication.translate("MainWindow", u"Abrir en Navegador", None))
        self.ChinookPDF_5.setText(QCoreApplication.translate("MainWindow", u"Crear PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabPoblacion), QCoreApplication.translate("MainWindow", u"Poblacion WIKI", None))
    # retranslateUi
        
    def load_data(self):
        # Cargamos los datos de la base de datos Chinook en tableWidget1
        connection = sql.connect('chinook.db')
        df1 = pd.read_sql_query("SELECT * FROM artists", connection)
        self.tableWidget1.setRowCount(df1.shape[0])
        self.tableWidget1.setColumnCount(df1.shape[1])
        self.tableWidget1.setHorizontalHeaderLabels(df1.columns)
        for i in range(df1.shape[0]):
            for j in range(df1.shape[1]):
                self.tableWidget1.setItem(i, j, QTableWidgetItem(str(df1.iat[i, j])))

        # Cargar los datos del archivo JSON de Coldplay en tableWidget2
        df2 = pd.read_json('coldplay_albums.json')
        self.tableWidget2.setRowCount(df2.shape[0])
        self.tableWidget2.setColumnCount(df2.shape[1])
        self.tableWidget2.setHorizontalHeaderLabels(df2.columns)
        for i in range(df2.shape[0]):
            for j in range(df2.shape[1]):
                self.tableWidget2.setItem(i, j, QTableWidgetItem(str(df2.iat[i, j])))  


        # cargamos los datos directamente de la página web en tableWidget3 que nos proporciona pandas en formato html
        url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
        df3 = pd.read_html(url)[0]  # Asume que la tabla que quieres es la primera en la página
        self.tableWidget3.setRowCount(df3.shape[0])
        self.tableWidget3.setColumnCount(df3.shape[1])
        self.tableWidget3.setHorizontalHeaderLabels(df3.columns)
        for i in range(df3.shape[0]):
            for j in range(df3.shape[1]):
                self.tableWidget3.setItem(i, j, QTableWidgetItem(str(df3.iat[i, j])))     



    def ChinookNavegacionPage(self):
        # Abrir la página web en el navegador
        url = "https://www.sqlitetutorial.net/sqlite-sample-database/"
        webbrowser.open(url)

    def ColdplayNavegacionPage(self):
        url = "https://www.kaggle.com/artimous/every-coldplay-song-ever"
        webbrowser.open(url)
    
    def PoblacionNavegacionPage(self):
        url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
        webbrowser.open(url)



    def chinookToPDF(self):
        # Crear un DataFrame a partir de los datos de la tabla
        data = []
        for i in range(self.tableWidget1.rowCount()):
            row = []
            for j in range(self.tableWidget1.columnCount()):
                item = self.tableWidget1.item(i, j)
                row.append(item.text() if item else "")
            data.append(row)

        df = pd.DataFrame(data, columns=[self.tableWidget1.horizontalHeaderItem(i).text() for i in range(self.tableWidget1.columnCount())])

        # Convertir el DataFrame en una cadena LaTeX
        latex = df.reset_index(drop=True).style.to_latex()

        # Guardar la cadena LaTeX como un archivo PDF
        with PdfPages('ChinookInfo.pdf') as pdf:
            fig, ax = plt.subplots(figsize=(12,4))
            fig.suptitle('CHINOOK.DB INFO', fontsize=20)
            ax.axis('tight')
            ax.axis('off')
            ax.table(cellText=df.values,colLabels=df.columns,cellLoc = 'center', loc='center')

            pdf.savefig(fig, bbox_inches='tight')  

    def coldplayToPDF(self):
        # Crear un DataFrame a partir de los datos de la tabla
        data = []
        for i in range(self.tableWidget2.rowCount()):
            row = []
            for j in range(self.tableWidget2.columnCount()):
                item = self.tableWidget2.item(i, j)
                row.append(item.text() if item else "")
            data.append(row)

        df = pd.DataFrame(data, columns=[self.tableWidget2.horizontalHeaderItem(i).text() for i in range(self.tableWidget2.columnCount())])

        # Convertir el DataFrame en una cadena LaTeX
        latex = df.reset_index(drop=True).style.to_latex()

        # Guardar la cadena LaTeX como un archivo PDF
        with PdfPages('ColdplayInfo.pdf') as pdf:
            fig, ax = plt.subplots(figsize=(12,4))
            fig.suptitle('COLDPLAY MUSIC', fontsize=20)
            ax.axis('tight')
            ax.axis('off')
            ax.table(cellText=df.values,colLabels=df.columns,cellLoc = 'center', loc='center')

            pdf.savefig(fig, bbox_inches='tight')


    def poblacionToPDF(self):
        # Crear un DataFrame a partir de los datos de la tabla
        data = []
        #recorre la tabla y añade la info
        for i in range(self.tableWidget3.rowCount()):
            row = []
            for j in range(self.tableWidget3.columnCount()):
                item = self.tableWidget3.item(i, j)
                row.append(item.text() if item else "")
            data.append(row)

        df = pd.DataFrame(data, columns=[self.tableWidget3.horizontalHeaderItem(i).text() for i in range(self.tableWidget3.columnCount())])

        # Convertir el DataFrame en una cadena LaTeX
        latex = df.reset_index(drop=True).style.to_latex()

        # Guardar la cadena LaTeX como un archivo PDF
        with PdfPages('PoblacionInfo.pdf') as pdf:
            fig, ax = plt.subplots(figsize=(12,4))
            fig.suptitle('COUNTRIES INFO', fontsize=20)
            ax.axis('tight')
            ax.axis('off')
            ax.text(0.5, 0.95, 'Poblacion', ha='center', va='top', fontsize=25)
            ax.table(cellText=df.values,colLabels=df.columns,cellLoc = 'center', loc='center')

            pdf.savefig(fig, bbox_inches='tight')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_data()  # Cargar los datos después de configurar la UI
    MainWindow.show()
    sys.exit(app.exec_())