import sys
import time

from PyQt5 import QtWidgets

from mypkg.linux_cli import LinuxCli
from mypkg.login_view import LoginUi
from mypkg.main_view import MainUi
from mypkg.nord_api import NordApi


class LoginWindow(QtWidgets.QMainWindow, LoginUi):
    def __init__(self, *args, obj=None, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.cli = LinuxCli()
        if self.cli.isUserLoggedIn():
            self.repaint()
            time.sleep(0.5)
            self.hide()
            MainWindow().show()

        self.login_button.clicked.connect(lambda: self.login())

    def login(self):
        if self.cli.login('r21jim@gmail.com', 'dvN9P2k52MmB'):
            self.repaint()
            time.sleep(0.5)
            self.hide()
            MainWindow().show()



class MainWindow(QtWidgets.QMainWindow, MainUi):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.api = NordApi()
        self.data = None

        # initialize data
        self.get_data()
        self.populate_country_list()

    def get_data(self):
        self.data = self.api.get_api_data()

    def refresh(self):
        self.get_data()

    def populate_country_list(self):
        self.countries_list.addItems(self.api.get_country_list(self.data))
        self.countries_list.itemClicked.connect(lambda: self.populate_server_list())

    def populate_server_list(self):
        self.server_list.clear()
        current_country = self.countries_list.currentItem().text()
        server_list = []
        if current_country is not None:
            server_list = self.api.get_servers_by_country(self.data, current_country)
        formatted_server_list = []
        for server in server_list:
            formatted_server_list.append(self.format_server_list_item(server))
        self.server_list.addItems(formatted_server_list)

    def format_server_list_item(self, server):
        name = server['name']
        domain = server['domain']
        load = server['load']

        return name + '\n' + 'Load: ' + str(load) + '%\n' + 'Domain: ' + domain


app = QtWidgets.QApplication(sys.argv)

window = LoginWindow()
window.show()
app.exec()
