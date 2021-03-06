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
        MainWindow.resize(982, 779)
        MainWindow.setMinimumSize(QtCore.QSize(982, 648))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(982, 648))
        self.centralwidget.setObjectName("centralwidget")
        self.countries_list = QtWidgets.QListWidget(self.centralwidget)
        self.countries_list.setGeometry(QtCore.QRect(10, 70, 231, 501))
        self.countries_list.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                          "                     selection-background-color: rgb(70, 135, 255);\n"
                                          "                 \n"
                                          "font: 57 14pt \"Ubuntu\";")
        self.countries_list.setObjectName("countries_list")
        self.server_list = QtWidgets.QListWidget(self.centralwidget)
        self.server_list.setGeometry(QtCore.QRect(240, 70, 731, 501))
        self.server_list.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                       "font: 57 14pt \"Ubuntu\";\n"
                                       "                     selection-background-color: rgb(70, 135, 255);\n"
                                       "                 ")
        self.server_list.setObjectName("server_list")
        self.refresh_button = QtWidgets.QToolButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(920, 630, 41, 41))
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_button.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                          "      font: 57 15pt \"Ubuntu\";\n"
                                          "     ")
        self.refresh_button.setObjectName("refresh_button")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(810, 630, 91, 41))
        self.connect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connect_button.setMouseTracking(False)
        self.connect_button.setStyleSheet("background-color: rgb(70, 135, 255);\n"
                                          "      font: 57 14pt \"Ubuntu\";\n"
                                          "      color: rgb(255, 255, 255);\n"
                                          "     ")
        self.connect_button.setObjectName("connect_button")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 961, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setStyleSheet("border-image: url(ui/nord-icon-152x152.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.email_label = QtWidgets.QLabel(self.frame)
        self.email_label.setGeometry(QtCore.QRect(740, 16, 161, 20))
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.expires_label = QtWidgets.QLabel(self.frame)
        self.expires_label.setGeometry(QtCore.QRect(740, 36, 161, 16))
        self.expires_label.setStyleSheet("font: 10pt \"Ubuntu\";\n"
                                         "       color: rgb(136, 138, 133);\n"
                                         "      ")
        self.expires_label.setObjectName("expires_label")
        self.connection_label = QtWidgets.QLabel(self.frame)
        self.connection_label.setGeometry(QtCore.QRect(110, 20, 171, 31))
        self.connection_label.setStyleSheet("font: 57 14pt \"Ubuntu\";")
        self.connection_label.setText("")
        self.connection_label.setObjectName("connection_label")
        self.connection_color_status = QtWidgets.QFrame(self.frame)
        self.connection_color_status.setGeometry(QtCore.QRect(0, 0, 16, 71))
        self.connection_color_status.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.connection_color_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connection_color_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connection_color_status.setObjectName("connection_color_status")
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
        self.connected_server.setGeometry(QtCore.QRect(360, 10, 271, 51))
        self.connected_server.setStyleSheet("font: 75 15pt \"Samanata\";")
        self.connected_server.setText("")
        self.connected_server.setObjectName("connected_server")
        self.disconnect_button = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_button.setGeometry(QtCore.QRect(680, 630, 111, 41))
        self.disconnect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.disconnect_button.setStyleSheet("background-color: rgb(237, 239, 241);\n"
                                             "               font: 57 14pt \"Ubuntu\";\n"
                                             "               color: rgb(191, 64, 64);\n"
                                             "           ")
        self.disconnect_button.setObjectName("disconnect_button")
        self.checkBox_auto_connect = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_auto_connect.setGeometry(QtCore.QRect(20, 590, 151, 23))
        self.checkBox_auto_connect.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.checkBox_auto_connect.setTristate(False)
        self.checkBox_auto_connect.setObjectName("checkBox_auto_connect")
        self.checkBox_kill_switch = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_kill_switch.setGeometry(QtCore.QRect(20, 620, 151, 23))
        self.checkBox_kill_switch.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.checkBox_kill_switch.setTristate(False)
        self.checkBox_kill_switch.setObjectName("checkBox_kill_switch")
        self.checkBox_cybersec = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_cybersec.setGeometry(QtCore.QRect(20, 650, 151, 23))
        self.checkBox_cybersec.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.checkBox_cybersec.setTristate(False)
        self.checkBox_cybersec.setObjectName("checkBox_cybersec")
        self.checkBox_obfuscate = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_obfuscate.setGeometry(QtCore.QRect(20, 680, 151, 23))
        self.checkBox_obfuscate.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.checkBox_obfuscate.setTristate(False)
        self.checkBox_obfuscate.setObjectName("checkBox_obfuscate")
        self.checkBox_notify = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_notify.setGeometry(QtCore.QRect(20, 710, 151, 23))
        self.checkBox_notify.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.checkBox_notify.setTristate(False)
        self.checkBox_notify.setObjectName("checkBox_notify")
        self.radioButton_udp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_udp.setGeometry(QtCore.QRect(310, 590, 61, 23))
        self.radioButton_udp.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.radioButton_udp.setAutoExclusive(False)
        self.radioButton_udp.setObjectName("radioButton_udp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 590, 81, 21))
        self.label_3.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.radioButton_open_vpn = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_open_vpn.setGeometry(QtCore.QRect(310, 620, 101, 23))
        self.radioButton_open_vpn.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.radioButton_open_vpn.setAutoExclusive(False)
        self.radioButton_open_vpn.setObjectName("radioButton_open_vpn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 620, 91, 21))
        self.label_4.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.radioButton_nord_lynx = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_nord_lynx.setGeometry(QtCore.QRect(420, 620, 101, 23))
        self.radioButton_nord_lynx.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.radioButton_nord_lynx.setAutoExclusive(False)
        self.radioButton_nord_lynx.setObjectName("radioButton_nord_lynx")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 580, 521, 161))
        self.frame_2.setStyleSheet("\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(153, 10, 20, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radioButton_tcp = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_tcp.setGeometry(QtCore.QRect(410, 10, 61, 23))
        self.radioButton_tcp.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.radioButton_tcp.setAutoExclusive(False)
        self.radioButton_tcp.setObjectName("radioButton_tcp")
        self.frame_2.raise_()
        self.frame.raise_()
        self.countries_list.raise_()
        self.server_list.raise_()
        self.refresh_button.raise_()
        self.connect_button.raise_()
        self.disconnect_button.raise_()
        self.checkBox_auto_connect.raise_()
        self.checkBox_kill_switch.raise_()
        self.checkBox_cybersec.raise_()
        self.checkBox_obfuscate.raise_()
        self.checkBox_notify.raise_()
        self.radioButton_udp.raise_()
        self.label_3.raise_()
        self.radioButton_open_vpn.raise_()
        self.label_4.raise_()
        self.radioButton_nord_lynx.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.setBuddy(self.radioButton_udp)
        self.label_4.setBuddy(self.radioButton_open_vpn)

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
            self.expires_label.setText(_translate("MainWindow", "Expires on"))
            self.disconnect_button.setText(_translate("MainWindow", "Disconnect"))
            self.checkBox_auto_connect.setToolTip(_translate("MainWindow",
                                                             "Enables or disables auto-connect. When enabled, this feature will automatically try to connect\n"
                                                             "                     to VPN on operating system startup.\n"
                                                             "                 "))
            self.checkBox_auto_connect.setText(_translate("MainWindow", "Auto-connect"))
            self.checkBox_kill_switch.setToolTip(_translate("MainWindow",
                                                            "Enables or disables Kill Switch. This security feature blocks your device from accessing the\n"
                                                            "                     Internet outside the secure VPN tunnel, in case connection with a VPN server is lost.\n"
                                                            "                 "))
            self.checkBox_kill_switch.setText(_translate("MainWindow", "Kill Switch"))
            self.checkBox_cybersec.setToolTip(_translate("MainWindow",
                                                         "Enables or disables CyberSec. When enabled, the CyberSec feature will automatically block\n"
                                                         "                     suspicious websites so that no malware or other cyber threats can infect your device. Additionally,\n"
                                                         "                     no flashy ads will come into your sight. More information on how it works:\n"
                                                         "                     https://nordvpn.com/features/cybersec/.\n"
                                                         "                 "))
            self.checkBox_cybersec.setText(_translate("MainWindow", "CyberSec"))
            self.checkBox_obfuscate.setToolTip(_translate("MainWindow",
                                                          "Enables or disables obfuscation. When enabled, this feature allows to bypass network traffic\n"
                                                          "                     sensors which aim to detect usage of the protocol and log, throttle or block it.\n"
                                                          "                 "))
            self.checkBox_obfuscate.setText(_translate("MainWindow", "Obfuscate"))
            self.checkBox_notify.setToolTip(_translate("MainWindow", "Enables or disables notifications"))
            self.checkBox_notify.setText(_translate("MainWindow", "Notify"))
            self.radioButton_udp.setText(_translate("MainWindow", "UDP"))
            self.label_3.setText(_translate("MainWindow", "Protocol"))
            self.radioButton_open_vpn.setText(_translate("MainWindow", "OpenVPN"))
            self.label_4.setText(_translate("MainWindow", "Technology"))
            self.radioButton_nord_lynx.setText(_translate("MainWindow", "NordLynx"))
            self.radioButton_tcp.setText(_translate("MainWindow", "TCP"))
