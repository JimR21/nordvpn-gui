import sys

from PyQt5 import QtWidgets, QtCore

from mypkg.linux_cli import LinuxCli
from mypkg.login_view import LoginUi
from mypkg.main_view import MainUi
from mypkg.nord_api import NordApi

cli = LinuxCli()
api = NordApi()


def format_server_list_item(server):
    name = server['name']
    domain = server['domain']
    load = server['load']

    return name + '\n' + 'Load: ' + str(load) + '%\n' + 'Domain: ' + domain


class MainWindow(QtWidgets.QMainWindow, MainUi):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.data = None

        # initialize data
        self.get_data()
        self.populate_country_list()

    def get_data(self):
        self.data = api.get_api_data()

    def refresh(self):
        self.get_data()

    def populate_country_list(self):
        self.countries_list.addItems(api.get_country_list(self.data))
        self.countries_list.itemClicked.connect(lambda: self.populate_server_list())

    def populate_server_list(self):
        self.server_list.clear()
        current_country = self.countries_list.currentItem().text()
        server_list = []
        if current_country is not None:
            server_list = api.get_servers_by_country(self.data, current_country)
        formatted_server_list = []
        for server in server_list:
            formatted_server_list.append(format_server_list_item(server))
        self.server_list.addItems(formatted_server_list)


class LoginWindow(QtWidgets.QMainWindow, LoginUi):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.username_line.textChanged.connect(lambda: self.check_login_button())
        self.password_line.textChanged.connect(lambda: self.check_login_button())
        self.password_line.setEchoMode(2)
        self.login_button.setDisabled(True)
        self.login_button.clicked.connect(lambda: self.login())
        self.wrong_credentials_msg.setHidden(True)

    def login(self):
        if self.username_line.text() and self.password_line.text():
            if cli.login(self.username_line.text(), self.password_line.text()):
                self.switch_window.emit()
                return

        self.wrong_credentials_msg.setHidden(False)

    def check_login_button(self):
        if self.username_line.text() and self.password_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setDisabled(True)


class Controller:

    def __init__(self):
        self.window = MainWindow()
        self.login = LoginWindow()

    def show_login(self):
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
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
