import sys
from collections import namedtuple

from PyQt5 import QtWidgets

from nordApi import NordApi
from nordVpnGui import Ui_MainWindow

ServerInfo = namedtuple('ServerInfo', 'name, country, domain, load, categories')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
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
        country = server['country']
        domain = server['domain']
        load = server['load']

        return name + '\n' + 'Load: ' + str(load) + '%\n' + 'Domain: ' + domain


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
