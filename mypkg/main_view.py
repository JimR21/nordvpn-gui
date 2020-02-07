# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nordVpnGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MainUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 648)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countries_list = QtWidgets.QListWidget(self.centralwidget)
        self.countries_list.setGeometry(QtCore.QRect(10, 70, 231, 501))
        self.countries_list.setStyleSheet("background-color: rgb(237, 239, 241);")
        self.countries_list.setObjectName("countries_list")
        self.server_list = QtWidgets.QListWidget(self.centralwidget)
        self.server_list.setGeometry(QtCore.QRect(240, 70, 731, 501))
        self.server_list.setStyleSheet("background-color: rgb(237, 239, 241);")
        self.server_list.setObjectName("server_list")
        self.refresh_button = QtWidgets.QToolButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(930, 590, 41, 41))
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_button.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                          "font: 57 15pt \"Ubuntu\";")
        self.refresh_button.setObjectName("refresh_button")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(820, 590, 91, 41))
        self.connect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connect_button.setMouseTracking(False)
        self.connect_button.setStyleSheet("background-color: rgb(70, 135, 255);\n"
                                          "font: 57 14pt \"Ubuntu\";\n"
                                          "color: rgb(255, 255, 255);")
        self.connect_button.setObjectName("connect_button")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 961, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setStyleSheet("border-image: url(ui/nordvpnicon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.email_label = QtWidgets.QLabel(self.frame)
        self.email_label.setGeometry(QtCore.QRect(740, 16, 161, 20))
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.expires_label = QtWidgets.QLabel(self.frame)
        self.expires_label.setGeometry(QtCore.QRect(740, 36, 101, 16))
        self.expires_label.setStyleSheet("font: 10pt \"Ubuntu\";\n"
                                         "color: rgb(136, 138, 133);")
        self.expires_label.setObjectName("expires_label")
        self.connection_label = QtWidgets.QLabel(self.frame)
        self.connection_label.setGeometry(QtCore.QRect(110, 20, 111, 31))
        self.connection_label.setStyleSheet("font: 57 14pt \"Ubuntu\";")
        self.connection_label.setText("")
        self.connection_label.setObjectName("connection_label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 16, 71))
        self.frame_2.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(700, 20, 31, 31))
        self.label_2.setStyleSheet("border-image: url(ui/icons8-user-24.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.logout_button = QtWidgets.QToolButton(self.frame)
        self.logout_button.setGeometry(QtCore.QRect(920, 20, 31, 31))
        self.logout_button.setStyleSheet("border-image: url(ui/icons8-logout-rounded-up-50.png);")
        self.logout_button.setText("")
        self.logout_button.setObjectName("logout_button")
        self.connected_server = QtWidgets.QLabel(self.frame)
        self.connected_server.setGeometry(QtCore.QRect(380, 10, 161, 41))
        self.connected_server.setStyleSheet("font: 75 15pt \"Samanata\";")
        self.connected_server.setText("")
        self.connected_server.setObjectName("connected_server")
        self.disconnect_button = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_button.setGeometry(QtCore.QRect(690, 590, 111, 41))
        self.disconnect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.disconnect_button.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                             "font: 57 14pt \"Ubuntu\";\n"
                                             "color: rgb(191, 64, 64);")
        self.disconnect_button.setObjectName("disconnect_button")
        self.frame.raise_()
        self.countries_list.raise_()
        self.server_list.raise_()
        self.refresh_button.raise_()
        self.connect_button.raise_()
        self.disconnect_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.countries_list, self.server_list)
        MainWindow.setTabOrder(self.server_list, self.connect_button)
        MainWindow.setTabOrder(self.connect_button, self.disconnect_button)
        MainWindow.setTabOrder(self.disconnect_button, self.refresh_button)
        MainWindow.setTabOrder(self.refresh_button, self.logout_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh_button.setText(_translate("MainWindow", "↺"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.expires_label.setText(_translate("MainWindow", "Expires on "))
        self.disconnect_button.setText(_translate("MainWindow", "Disconnect"))
