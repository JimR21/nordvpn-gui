# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginUi(object):
    def setupUi(self, LoginUi):
        LoginUi.setObjectName("LoginUi")
        LoginUi.resize(1082, 822)
        LoginUi.setMinimumSize(QtCore.QSize(1082, 822))
        LoginUi.setMaximumSize(QtCore.QSize(1082, 822))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("nordvpnicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginUi.setWindowIcon(icon)
        LoginUi.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginUi)
        self.centralwidget.setObjectName("centralwidget")
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setGeometry(QtCore.QRect(310, 610, 211, 31))
        self.username_line.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.username_line.setText("")
        self.username_line.setObjectName("username_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(560, 610, 211, 31))
        self.password_line.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.password_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.password_line.setText("")
        self.password_line.setObjectName("password_line")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(310, 580, 191, 17))
        self.username_label.setStyleSheet("background-color: rgba(81, 76, 76, 0);\n"
                                          "      color: rgb(243, 243, 243);\n"
                                          "      font: 57 15pt \"Ubuntu\";\n"
                                          "     ")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(560, 580, 141, 17))
        self.password_label.setStyleSheet("color: rgb(243, 243, 243);\n"
                                          "      font: 57 15pt \"Ubuntu\";\n"
                                          "     ")
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(480, 670, 121, 41))
        self.login_button.setStyleSheet("background-color: rgb(70, 135, 255);\n"
                                        " color: rgb(243, 243, 243);\n"
                                        "    \n"
                                        "font: 75 14pt \"Ubuntu\";")
        self.login_button.setDefault(True)
        self.login_button.setObjectName("login_button")
        self.background_label_image = QtWidgets.QLabel(self.centralwidget)
        self.background_label_image.setGeometry(QtCore.QRect(0, -250, 1081, 1071))
        self.background_label_image.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.background_label_image.setObjectName("background_label_image")
        self.wrong_credentials_msg = QtWidgets.QLabel(self.centralwidget)
        self.wrong_credentials_msg.setGeometry(QtCore.QRect(330, 730, 431, 16))
        self.wrong_credentials_msg.setStyleSheet("font: 57 13pt \"Ubuntu\";\n"
                                                 "      color: rgb(204, 0, 0);\n"
                                                 "     ")
        self.wrong_credentials_msg.setObjectName("wrong_credentials_msg")
        self.background_label_image.raise_()
        self.username_line.raise_()
        self.password_line.raise_()
        self.username_label.raise_()
        self.password_label.raise_()
        self.login_button.raise_()
        self.wrong_credentials_msg.raise_()
        LoginUi.setCentralWidget(self.centralwidget)
        self.username_label.setBuddy(self.username_line)
        self.password_label.setBuddy(self.password_line)

        self.retranslateUi(LoginUi)
        self.username_line.returnPressed.connect(self.login_button.click)
        self.password_line.returnPressed.connect(self.login_button.click)
        QtCore.QMetaObject.connectSlotsByName(LoginUi)

    def retranslateUi(self, LoginUi):
        _translate = QtCore.QCoreApplication.translate
        LoginUi.setWindowTitle(_translate("LoginUi", "NordVPN Login"))
        self.username_label.setText(_translate("LoginUi", "Email"))
        self.password_label.setText(_translate("LoginUi", "Password"))
        self.login_button.setText(_translate("LoginUi", "Login"))
        self.background_label_image.setText(_translate("LoginUi",
                                                       "<html><head/><body><p align=\"center\"><img src=\"ui/nordvpn_login_background.png\"/></p></body></html>"))
        self.wrong_credentials_msg.setText(
            _translate("LoginUi", "Username or password is not correct. Please try again."))
