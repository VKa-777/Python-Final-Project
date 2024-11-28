import mainMenu
from PyQt6 import QtCore, QtGui, QtWidgets

class Utils:
    def back_to_main_menu(self, current_window):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        current_window.hide()