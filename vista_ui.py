# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\enman\OneDrive\Escritorio\metodos cuantitativos\simlacion\programacion de objetos\vista.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 619)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 160, 961, 411))
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 221, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 121, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 231, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 60, 141, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setGeometry(QtCore.QRect(490, 40, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 221, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(270, 20, 161, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(450, 20, 241, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 171, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(250, 120, 181, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 50, 221, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_5.setGeometry(QtCore.QRect(270, 50, 161, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_6.setGeometry(QtCore.QRect(460, 50, 221, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_7.setGeometry(QtCore.QRect(30, 150, 171, 31))
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_8.setGeometry(QtCore.QRect(240, 150, 221, 31))
        self.textEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 130, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 51, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(160, 30, 111, 16))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(330, 30, 121, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(510, 30, 131, 16))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(690, 30, 71, 16))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(800, 30, 101, 16))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_9.setGeometry(QtCore.QRect(20, 60, 81, 31))
        self.textEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_10.setGeometry(QtCore.QRect(130, 60, 161, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_11.setGeometry(QtCore.QRect(310, 60, 161, 31))
        self.textEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_12.setGeometry(QtCore.QRect(490, 60, 161, 31))
        self.textEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_13.setGeometry(QtCore.QRect(670, 60, 101, 31))
        self.textEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_14.setGeometry(QtCore.QRect(790, 60, 101, 31))
        self.textEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_14.setObjectName("textEdit_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 140, 161, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(190, 60, 55, 16))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(280, 60, 55, 16))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(390, 60, 55, 16))
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.textEdit_16 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_16.setGeometry(QtCore.QRect(170, 90, 71, 31))
        self.textEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_17.setGeometry(QtCore.QRect(270, 90, 71, 31))
        self.textEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_18.setGeometry(QtCore.QRect(380, 90, 61, 31))
        self.textEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_18.setObjectName("textEdit_18")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 90, 141, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.label_31.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_31.setObjectName("label_31")
        self.textEdit_34 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_34.setGeometry(QtCore.QRect(70, 90, 71, 31))
        self.textEdit_34.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_34.setObjectName("textEdit_34")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(140, 30, 81, 16))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(260, 30, 131, 16))
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(420, 30, 131, 16))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(570, 30, 121, 16))
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(710, 30, 121, 16))
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.textEdit_19 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_19.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.textEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_20.setGeometry(QtCore.QRect(120, 50, 111, 31))
        self.textEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_20.setObjectName("textEdit_20")
        self.textEdit_21 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_21.setGeometry(QtCore.QRect(260, 50, 121, 31))
        self.textEdit_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_21.setObjectName("textEdit_21")
        self.textEdit_22 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_22.setGeometry(QtCore.QRect(420, 50, 121, 31))
        self.textEdit_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_22.setObjectName("textEdit_22")
        self.textEdit_23 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_23.setGeometry(QtCore.QRect(560, 50, 121, 31))
        self.textEdit_23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_23.setObjectName("textEdit_23")
        self.textEdit_24 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_24.setGeometry(QtCore.QRect(700, 50, 121, 31))
        self.textEdit_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_24.setObjectName("textEdit_24")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 140, 181, 61))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_24 = QtWidgets.QLabel(self.tab_6)
        self.label_24.setGeometry(QtCore.QRect(40, 20, 51, 16))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_6)
        self.label_25.setGeometry(QtCore.QRect(120, 20, 111, 16))
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_6)
        self.label_26.setGeometry(QtCore.QRect(250, 20, 91, 16))
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_6)
        self.label_27.setGeometry(QtCore.QRect(360, 20, 161, 20))
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_6)
        self.label_28.setGeometry(QtCore.QRect(530, 20, 171, 16))
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_6)
        self.label_29.setGeometry(QtCore.QRect(710, 20, 101, 16))
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setGeometry(QtCore.QRect(840, 20, 91, 16))
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.textEdit_26 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_26.setGeometry(QtCore.QRect(30, 40, 61, 31))
        self.textEdit_26.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_26.setObjectName("textEdit_26")
        self.textEdit_27 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_27.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.textEdit_27.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_27.setObjectName("textEdit_27")
        self.textEdit_28 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_28.setGeometry(QtCore.QRect(243, 40, 111, 31))
        self.textEdit_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_29.setGeometry(QtCore.QRect(360, 40, 161, 31))
        self.textEdit_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_30 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_30.setGeometry(QtCore.QRect(540, 40, 151, 31))
        self.textEdit_30.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_30.setObjectName("textEdit_30")
        self.textEdit_31 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_31.setGeometry(QtCore.QRect(710, 40, 101, 31))
        self.textEdit_31.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_32 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_32.setGeometry(QtCore.QRect(830, 40, 111, 31))
        self.textEdit_32.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_32.setObjectName("textEdit_32")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 110, 141, 61))
        self.pushButton_6.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 60, 431, 51))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Constante de velocidad de la reacción"))
        self.label_3.setText(_translate("MainWindow", "Concentracion inicial"))
        self.pushButton.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Continuo reaccion Quimica"))
        self.label_4.setText(_translate("MainWindow", "Tasa de generación de calor en vatios"))
        self.label_5.setText(_translate("MainWindow", "Coeficiente de enfriamiento"))
        self.label_6.setText(_translate("MainWindow", "Temperatura del sistema de enfriamiento"))
        self.label_7.setText(_translate("MainWindow", "Capacidad térmica del reactor"))
        self.label_8.setText(_translate("MainWindow", "Temperatura inicial del reactor"))
        self.pushButton_2.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Continuo Reactor"))
        self.label_9.setText(_translate("MainWindow", "Semilla"))
        self.label_10.setText(_translate("MainWindow", "Num de peluqueros"))
        self.label_11.setText(_translate("MainWindow", "Tiempo corte en Min"))
        self.label_12.setText(_translate("MainWindow", "Tiempo corte Maximo"))
        self.label_13.setText(_translate("MainWindow", "T llegadas"))
        self.label_14.setText(_translate("MainWindow", "Tot Clientes"))
        self.pushButton_3.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Discreta peluqueria"))
        self.label_15.setText(_translate("MainWindow", "Rango A"))
        self.label_16.setText(_translate("MainWindow", "Rango B"))
        self.label_17.setText(_translate("MainWindow", "Tiempo"))
        self.pushButton_4.setText(_translate("MainWindow", "Ejecutar"))
        self.label_31.setText(_translate("MainWindow", "Mostradores"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Discreta Restaurante"))
        self.label_18.setText(_translate("MainWindow", "SEMILLA"))
        self.label_19.setText(_translate("MainWindow", "NUM_MESAS"))
        self.label_20.setText(_translate("MainWindow", "TIEMPO_COMER_MIN"))
        self.label_21.setText(_translate("MainWindow", "TIEMPO_COMER_MAX"))
        self.label_22.setText(_translate("MainWindow", "TIEMPO_LLEGADAS"))
        self.label_23.setText(_translate("MainWindow", "TOTAL_CLIENTES"))
        self.pushButton_5.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Discreta restaurante 2"))
        self.label_24.setText(_translate("MainWindow", "semilla"))
        self.label_25.setText(_translate("MainWindow", "capacidad_servidor"))
        self.label_26.setText(_translate("MainWindow", "capacidad_cola"))
        self.label_27.setText(_translate("MainWindow", "tiempo_procesamiento_min"))
        self.label_28.setText(_translate("MainWindow", "tiempo_procesamiento_max"))
        self.label_29.setText(_translate("MainWindow", "tiempo_llegadas"))
        self.label_30.setText(_translate("MainWindow", "total_paquetes"))
        self.pushButton_6.setText(_translate("MainWindow", "Ejecutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Discreta Redes"))
        self.label.setText(_translate("MainWindow", "Metodos cuantitativos Simulación "))
