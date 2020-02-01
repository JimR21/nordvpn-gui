# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 1048)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setGeometry(QtCore.QRect(440, 860, 211, 21))
        self.username_line.setObjectName("username_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(440, 940, 211, 21))
        self.password_line.setObjectName("password_line")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(440, 830, 141, 17))
        self.username_label.setStyleSheet("background-color: rgba(81, 76, 76, 0);\n"
"color: rgb(243, 243, 243);")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(440, 910, 141, 17))
        self.password_label.setStyleSheet("color: rgb(243, 243, 243);")
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(480, 990, 121, 41))
        self.login_button.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(243, 243, 243);")
        self.login_button.setObjectName("login_button")
        self.background_label_image = QtWidgets.QLabel(self.centralwidget)
        self.background_label_image.setGeometry(QtCore.QRect(0, 0, 1071, 1051))
        self.background_label_image.setObjectName("background_label_image")
        self.background_label_image.raise_()
        self.username_line.raise_()
        self.password_line.raise_()
        self.username_label.raise_()
        self.password_label.raise_()
        self.login_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username / Email"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.background_label_image.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\"ui/nordvpn_login_background.png\"/></p></body></html>"))
