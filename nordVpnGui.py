# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nordVpnGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 559)
        MainWindow.setStyleSheet("background-color: rgb(32, 74, 135);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countries_list = QtWidgets.QListWidget(self.centralwidget)
        self.countries_list.setGeometry(QtCore.QRect(20, 90, 361, 401))
        self.countries_list.setStyleSheet("background-color: rgb(94, 114, 137);")
        self.countries_list.setObjectName("countries_list")
        self.server_list = QtWidgets.QListWidget(self.centralwidget)
        self.server_list.setGeometry(QtCore.QRect(410, 90, 521, 401))
        self.server_list.setStyleSheet("background-color: rgb(94, 114, 137);")
        self.server_list.setObjectName("server_list")
        self.countries_label = QtWidgets.QLabel(self.centralwidget)
        self.countries_label.setGeometry(QtCore.QRect(40, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Heros")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.countries_label.setFont(font)
        self.countries_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.countries_label.setObjectName("countries_label")
        self.refresh_button = QtWidgets.QToolButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(900, 10, 31, 31))
        self.refresh_button.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.refresh_button.setObjectName("refresh_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.countries_label.setText(_translate("MainWindow", "Countries"))
        self.refresh_button.setText(_translate("MainWindow", "↺"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
