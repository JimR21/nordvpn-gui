import sys
from PyQt5 import QtWidgets, uic

from nordApi import NordApi
from nordVpnGui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.api = NordApi()

        # initialize data
        self.get_data()
        self.populate_country_list()

    def get_data(self):
        self.data = self.api.get_api_data()

    def refresh(self):
        self.get_data()


    def populate_country_list(self):
        self.countries_list.addItems(self.api.get_country_list(self.data))
        self.countries_list.itemClicked.connect(self.populate_server_list())

    def populate_server_list(self):
        current_country = self.countries_list.currentItem()





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
