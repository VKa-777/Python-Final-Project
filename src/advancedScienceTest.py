# Form implementation generated from reading ui file 'advancedScienceTest.ui'
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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_background = QtWidgets.QWidget(parent=self.centralwidget)
        self.heading_background.setGeometry(QtCore.QRect(0, 0, 1337, 78))
        self.heading_background.setStyleSheet("background-color: #AAC4FF\n"
"")
        self.heading_background.setObjectName("heading_background")
        self.return_btn = QtWidgets.QPushButton(parent=self.heading_background)
        self.return_btn.setGeometry(QtCore.QRect(20, 20, 71, 41))
        self.return_btn.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 36px;\n"
"padding-bottom: 9px; \n"
"font-weight: bold;\n"
"text-align: center;")
        self.return_btn.setObjectName("return_btn")
        self.restart_btn = QtWidgets.QPushButton(parent=self.heading_background)
        self.restart_btn.setGeometry(QtCore.QRect(1250, 20, 71, 41))
        self.restart_btn.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 36px;\n"
"padding-bottom: 7px; \n"
"font-weight: bold;\n"
"text-align: center;")
        self.restart_btn.setObjectName("restart_btn")
        self.heading_label = QtWidgets.QLabel(parent=self.heading_background)
        self.heading_label.setGeometry(QtCore.QRect(483, 0, 371, 81))
        self.heading_label.setObjectName("heading_label")
        self.background = QtWidgets.QWidget(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 78, 1337, 642))
        self.background.setStyleSheet("background-color: #B1B2FF;\n"
"")
        self.background.setObjectName("background")
        self.text_area_background = QtWidgets.QWidget(parent=self.background)
        self.text_area_background.setGeometry(QtCore.QRect(40, 69, 1261, 191))
        self.text_area_background.setStyleSheet("font-size: 48pt;\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"")
        self.text_area_background.setObjectName("text_area_background")
        self.text_area = QtWidgets.QTextEdit(parent=self.text_area_background)
        self.text_area.setGeometry(QtCore.QRect(10, 10, 1231, 421))
        self.text_area.setObjectName("text_area")
        self.text_area_background_2 = QtWidgets.QWidget(parent=self.background)
        self.text_area_background_2.setGeometry(QtCore.QRect(40, 310, 1261, 191))
        self.text_area_background_2.setStyleSheet("font-size: 48pt;\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"")
        self.text_area_background_2.setObjectName("text_area_background_2")
        self.text_area_2 = QtWidgets.QTextEdit(parent=self.text_area_background_2)
        self.text_area_2.setGeometry(QtCore.QRect(10, 10, 1231, 461))
        self.text_area_2.setObjectName("text_area_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_btn.setText(_translate("MainWindow", "←"))
        self.restart_btn.setText(_translate("MainWindow", "⟳"))
        self.heading_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Bahnschrift\'; font-size:28pt; font-weight:600; color:#ffffff;\">Advanced Science Test</span></p></body></html>"))
        self.text_area.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo </span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#ea0c0f;\">li</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">gula </span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#ea0c0f;\">ege</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">t dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nas</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#ea0c0f;\">c</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">etur ridiculus mus. Donec quam felis,  ultricies nec, pellentesque eu, pretium q</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#ea0c0f;\">ui</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">s, sem. Nulla consequat massa quis enim. Donec pede justo, fring</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#ea0c0f;\">i</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600; color:#23d83e;\">lla vel, aliquet nec, vulputate  eget,</span><span style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:600;\"> </span></p></body></html>"))
        self.text_area_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
