# Form implementation generated from reading ui file 'resultPage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 720)
        MainWindow.setMaximumSize(QtCore.QSize(1337, 720))
        MainWindow.setStyleSheet("background-color: #B1B2FF;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.heading_container.setGeometry(QtCore.QRect(0, 0, 1337, 56))
        self.heading_container.setMaximumSize(QtCore.QSize(1337, 56))
        self.heading_container.setStyleSheet("background-color: #AAC4FF;")
        self.heading_container.setObjectName("heading_container")
        self.heading_label = QtWidgets.QLabel(parent=self.heading_container)
        self.heading_label.setGeometry(QtCore.QRect(621, 7, 91, 41))
        self.heading_label.setStyleSheet("color: white;\n"
"font: 24pt \"Bahnschrift\";\n"
"font-weight: bold;")
        self.heading_label.setObjectName("heading_label")
        self.result_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.result_container.setGeometry(QtCore.QRect(40, 156, 1261, 421))
        self.result_container.setStyleSheet("background-color: #EEF1FF;\n"
"border-radius: 10px;")
        self.result_container.setObjectName("result_container")
        self.result_heading = QtWidgets.QLabel(parent=self.result_container)
        self.result_heading.setGeometry(QtCore.QRect(476, 14, 321, 46))
        self.result_heading.setStyleSheet("color: black;\n"
"font: 63 28pt \"Bahnschrift SemiBold SemiConden\";\n"
"font-weight: bold;\n"
"")
        self.result_heading.setObjectName("result_heading")
        self.test_complete_label = QtWidgets.QLabel(parent=self.result_container)
        self.test_complete_label.setGeometry(QtCore.QRect(440, 74, 381, 61))
        self.test_complete_label.setStyleSheet("font: 25 20pt \"Bahnschrift\";\n"
"background: none;\n"
"color: black")
        self.test_complete_label.setObjectName("test_complete_label")
        self.wpm_and_accuracy_label = QtWidgets.QLabel(parent=self.result_container)
        self.wpm_and_accuracy_label.setGeometry(QtCore.QRect(363, 110, 531, 61))
        self.wpm_and_accuracy_label.setStyleSheet("font: 25 20pt \"Bahnschrift\";\n"
"background: none;\n"
"color: black")
        self.wpm_and_accuracy_label.setObjectName("wpm_and_accuracy_label")
        self.try_again_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.try_again_btn.setGeometry(QtCore.QRect(300, 269, 171, 41))
        self.try_again_btn.setStyleSheet("background-color: #FFD966;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font: 63 16pt \"Bahnschrift SemiBold\";")
        self.try_again_btn.setObjectName("try_again_btn")
        self.main_menu_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.main_menu_btn.setGeometry(QtCore.QRect(789, 269, 171, 41))
        self.main_menu_btn.setStyleSheet("background-color: #FFD966;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font: 63 16pt \"Bahnschrift SemiBold\";")
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.test_complete_label_2 = QtWidgets.QLabel(parent=self.result_container)
        self.test_complete_label_2.setGeometry(QtCore.QRect(440, 150, 381, 61))
        self.test_complete_label_2.setStyleSheet("font: 25 20pt \"Bahnschrift\";\n"
"background: none;\n"
"color: black")
        self.test_complete_label_2.setObjectName("test_complete_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.heading_label.setText(_translate("MainWindow", "Result"))
        self.result_heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Congratulation!</p></body></html>"))
        self.test_complete_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">You\'ve completed this level</span></p></body></html>"))
        self.wpm_and_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Your speed was </span><span style=\" font-weight:400; color:#23d83e;\">80 WPM </span><span style=\" font-weight:400;\">and </span><span style=\" font-weight:400; color:#23d83e;\">99% </span><span style=\" font-weight:400;\">accuracy.</span></p></body></html>"))
        self.try_again_btn.setText(_translate("MainWindow", "Main Menu"))
        self.main_menu_btn.setText(_translate("MainWindow", "Next Level"))
        self.test_complete_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Let\'s move on to the next stage</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
