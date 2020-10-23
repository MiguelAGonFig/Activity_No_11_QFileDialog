# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAbrir_Archivo = QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName(u"actionAbrir_Archivo")
        self.actionGuardar_Archivo = QAction(MainWindow)
        self.actionGuardar_Archivo.setObjectName(u"actionGuardar_Archivo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(200, 110, 211, 348))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")
        self.ID_spinBox.setMaximum(100000000)

        self.gridLayout.addWidget(self.ID_spinBox, 0, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Origen_X_spinBox = QSpinBox(self.groupBox)
        self.Origen_X_spinBox.setObjectName(u"Origen_X_spinBox")
        self.Origen_X_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_X_spinBox, 1, 1, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Origen_Y_spinBox = QSpinBox(self.groupBox)
        self.Origen_Y_spinBox.setObjectName(u"Origen_Y_spinBox")
        self.Origen_Y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_Y_spinBox, 2, 1, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.Destino_X_spinBox = QSpinBox(self.groupBox)
        self.Destino_X_spinBox.setObjectName(u"Destino_X_spinBox")
        self.Destino_X_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_X_spinBox, 3, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.Destino_Y_spinBox = QSpinBox(self.groupBox)
        self.Destino_Y_spinBox.setObjectName(u"Destino_Y_spinBox")
        self.Destino_Y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_Y_spinBox, 4, 1, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(100000000)

        self.gridLayout.addWidget(self.Velocidad_spinBox, 5, 1, 1, 2)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Red_spinBox, 6, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 1, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Green_spinBox, 7, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 1, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Blue_spinBox, 8, 2, 1, 1)

        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")

        self.gridLayout.addWidget(self.Agregar_Inicio_pushButton, 9, 0, 1, 3)

        self.Agregar_Final_pushButton = QPushButton(self.groupBox)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")

        self.gridLayout.addWidget(self.Agregar_Final_pushButton, 10, 0, 1, 3)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout.addWidget(self.Mostrar_pushButton, 11, 0, 1, 3)

        self.Salida = QPlainTextEdit(self.centralwidget)
        self.Salida.setObjectName(u"Salida")
        self.Salida.setGeometry(QRect(420, 120, 191, 331))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_Archivo)
        self.menuArchivo.addAction(self.actionGuardar_Archivo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir_Archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_Archivo.setText(QCoreApplication.translate("MainWindow", u"Guardar Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino en X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COLOR - RGB", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

