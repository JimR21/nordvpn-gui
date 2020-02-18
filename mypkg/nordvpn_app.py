import enum
import sys

from PyQt5 import QtWidgets, QtCore

from mypkg.linux_cli import LinuxCli
from mypkg.login_view import LoginUi
from mypkg.main_view import MainUi
from mypkg.nord_api import NordApi

cli = LinuxCli()
api = NordApi()


class Status(enum.auto):
    status = 'Status'
    current_server = 'Current server'
    country = 'Country'
    city = 'City'
    ip = 'Your new IP'
    technology = 'Current technology'
    protocol = 'Current protocol'
    transfer = 'Transfer'
    uptime = 'Uptime'


class Account(enum.auto):
    email = 'Email Address'
    expiration = 'VPN Service'


class Settings(enum.auto):
    technology = 'Technology'
    protocol = 'Protocol'
    kill_switch = 'Kill Switch'
    cybersec = 'CyberSec'
    obfuscate = 'Obfuscate'
    notify = 'Notify'
    auto_connect = 'Auto-connect'


def get_specific_info_from_output(output, info):
    lines = output.split('\n')
    for line in lines:
        if info in line:
            return line.split(': ')[1]


def format_server_list_item(server):
    name = server['name']
    domain = server['domain']
    load = server['load']

    return name + '\n' + 'Load: ' + str(
        load) + '%\n' + 'Domain: ' + domain + '\n-------------------------------------------------------------------' \
                                              '---------------------------------------------------------------------' \
                                              '--------------------- '


class MainWindow(QtWidgets.QMainWindow, MainUi):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.data = None

        # initialize data
        self.get_data()
        self.populate_account_info()
        self.populate_server_status()
        self.populate_country_list()
        self.populate_server_list()
        self.populate_settings()

        # buttons
        self.logout_button.clicked.connect(self.logout)
        self.connect_button.clicked.connect(self.connect)
        self.disconnect_button.clicked.connect(self.disconnect_from_server)
        self.refresh_button.clicked.connect(self.refresh)
        self.server_list.doubleClicked.connect(self.connect)

    def populate_account_info(self):
        account_output = cli.get_account()
        self.email_label.setText(get_specific_info_from_output(account_output, Account.email))
        self.expires_label.setText(
            get_specific_info_from_output(account_output, Account.expiration).split('(')[1].split(')')[0])

    def get_data(self):
        self.data = api.get_api_data()

    def refresh(self):
        self.get_data()
        self.populate_country_list()
        self.populate_server_list()

    def populate_country_list(self):
        self.countries_list.clear()
        self.countries_list.addItems(api.get_country_list(self.data))
        self.countries_list.itemClicked.connect(self.populate_server_list)

    def populate_server_list(self):
        self.server_list.clear()
        current_country = self.countries_list.currentItem()
        server_list = []
        if current_country is not None:
            server_list = api.get_servers_by_country(self.data, current_country.text())
        server_list.sort(key=lambda server: server['load'])
        formatted_server_list = []
        for server in server_list:
            formatted_server_list.append(format_server_list_item(server))
        self.server_list.addItems(formatted_server_list)

    def populate_server_status(self):
        status_output = cli.get_status()
        if 'Disconnected' in status_output:
            self.connection_label.setText('Disconnected')
            self.connected_server.setText('')
            self.connection_color_status.setStyleSheet('background-color: rgb(204, 0, 0);')
        else:
            self.connection_label.setText('Connected')
            self.connected_server.setText(get_specific_info_from_output(status_output, Status.current_server))
            self.connection_color_status.setStyleSheet('background-color: rgb(78, 154, 6);')
        self.update_button_status()

    def populate_settings(self):
        settings_output = cli.get_settings()
        self.checkBox_auto_connect.setChecked(
            get_specific_info_from_output(settings_output, Settings.auto_connect) == 'Enabled')
        self.checkBox_kill_switch.setChecked(
            get_specific_info_from_output(settings_output, Settings.kill_switch) == 'Enabled')
        self.checkBox_cybersec.setChecked(
            get_specific_info_from_output(settings_output, Settings.cybersec) == 'Enabled')
        self.checkBox_obfuscate.setChecked(
            get_specific_info_from_output(settings_output, Settings.obfuscate) == 'Enabled')
        self.checkBox_notify.setChecked(
            get_specific_info_from_output(settings_output, Settings.notify) == 'Enabled')

        if get_specific_info_from_output(settings_output, Settings.protocol) == 'UDP':
            self.radioButton_udp.setChecked(True)
            self.radioButton_tcp.setChecked(False)
        else:
            self.radioButton_udp.setChecked(False)
            self.radioButton_tcp.setChecked(True)

        if get_specific_info_from_output(settings_output, Settings.technology) == 'OpenVPN':
            self.radioButton_open_vpn.setChecked(True)
            self.radioButton_nord_lynx.setChecked(False)
        else:
            self.radioButton_open_vpn.setChecked(False)
            self.radioButton_nord_lynx.setChecked(True)

    def logout(self):
        cli.logout()
        self.switch_window.emit()

    def connect(self):
        if self.server_list.currentItem():
            selected_server = get_specific_info_from_output(self.server_list.currentItem().
                                                            text(), "Domain").split('.')[0]
            if cli.connect(selected_server):
                self.populate_server_status()

    def disconnect_from_server(self):
        cli.disconnect()
        self.populate_server_status()

    def update_button_status(self):
        if self.connection_label.text() == 'Connected':
            self.disconnect_button.setHidden(False)
            self.disconnect_button.setEnabled(True)
        else:
            self.disconnect_button.setHidden(True)
            self.disconnect_button.setDisabled(True)


class LoginWindow(QtWidgets.QMainWindow, LoginUi):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.username_line.textChanged.connect(self.check_login_button)
        self.password_line.textChanged.connect(self.check_login_button)
        self.password_line.setEchoMode(2)
        self.login_button.setDisabled(True)
        self.login_button.clicked.connect(self.login)
        self.wrong_credentials_msg.setHidden(True)

    def login(self):
        if self.username_line.text() and self.password_line.text():
            self.login_button.setDisabled(True)
            self.wrong_credentials_msg.setHidden(True)
            self.repaint()
            if cli.login(self.username_line.text(), self.password_line.text()):
                self.switch_window.emit()
                return
        self.login_button.setEnabled(True)
        self.wrong_credentials_msg.setHidden(False)

    def check_login_button(self):
        if self.username_line.text() and self.password_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setDisabled(True)


class Controller:

    def __init__(self):
        self.login = None
        self.window = None

    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_window.connect(self.show_main)
        if self.window:
            self.window.close()
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_login)
        if self.login:
            self.login.close()
        self.window.show()

    def show_starting_window(self):
        if cli.is_user_logged_in():
            self.show_main()
        else:
            self.show_login()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_starting_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
