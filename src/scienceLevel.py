# Form implementation generated from reading ui file 'scienceLevel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os
import min_1_typingTest
import topicSelectMenu
def read_all_text_files(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return {}

    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    text_contents = {}

    for file_name in text_files:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            text_contents[file_name] = file.read()

    return text_contents

def get_text_files_directory():
    # Get the directory path of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Join with the relative path to the 'assets/topic_text' directory
    return os.path.join(base_dir, r'assests/topic_text')

directory = get_text_files_directory()
all_texts = read_all_text_files(directory)
class Ui_MainWindow(object):
    def go_to_topic_select(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = topicSelectMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.MainWindow = MainWindow
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
        self.heading_label = QtWidgets.QLabel(parent=self.heading_background)
        self.heading_label.setGeometry(QtCore.QRect(514, 0, 321, 75))
        self.heading_label.setObjectName("heading_label")
        self.background = QtWidgets.QWidget(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 78, 1337, 642))
        self.background.setStyleSheet("background-color: #B1B2FF;\n"
"")
        self.background.setObjectName("background")
        self.main_container = QtWidgets.QWidget(parent=self.background)
        self.main_container.setGeometry(QtCore.QRect(10, 30, 1314, 551))
        self.main_container.setStyleSheet("background-color: white;\n"
"\n"
"border-radius: 5px;")
        self.main_container.setObjectName("main_container")
        self.widget_2 = QtWidgets.QWidget(parent=self.main_container)
        self.widget_2.setGeometry(QtCore.QRect(10, 13, 1291, 101))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 1271, 71))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.frame_2 = QtWidgets.QFrame(parent=self.main_container)
        self.frame_2.setGeometry(QtCore.QRect(20, 130, 1281, 381))
        self.frame_2.setStyleSheet("background-color: #AAC4FF;\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(140, 120, 231, 101))
        self.widget_3.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.min_1_btn = QtWidgets.QPushButton(parent=self.widget_3)
        self.min_1_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_1_btn.setStyleSheet("background-color: #FFD966;\n"
"font: 11pt \"Bahnschrift\";")
        self.min_1_btn.setObjectName("min_1_btn")
        self.min_1_label = QtWidgets.QLabel(parent=self.widget_3)
        self.min_1_label.setGeometry(QtCore.QRect(17, 23, 201, 31))
        self.min_1_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_1_label.setObjectName("min_1_label")
        self.widget_4 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_4.setGeometry(QtCore.QRect(530, 120, 231, 101))
        self.widget_4.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.line_2 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_2.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.min_3_btn = QtWidgets.QPushButton(parent=self.widget_4)
        self.min_3_btn.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_3_btn.setStyleSheet("background-color: #FFD966;\n"
"font: 11pt \"Bahnschrift\";")
        self.min_3_btn.setObjectName("min_3_btn")
        self.min_3_label = QtWidgets.QLabel(parent=self.widget_4)
        self.min_3_label.setGeometry(QtCore.QRect(17, 24, 201, 31))
        self.min_3_label.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_3_label.setObjectName("min_3_label")
        self.widget_5 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_5.setGeometry(QtCore.QRect(920, 120, 231, 101))
        self.widget_5.setStyleSheet("background-color:white;\n"
"border-radius: 5px;\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.line_3 = QtWidgets.QFrame(parent=self.widget_5)
        self.line_3.setGeometry(QtCore.QRect(0, 0, 231, 16))
        self.line_3.setStyleSheet("background-color: #94B3FD;\n"
"border-radius: 0px;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.min_1_btn_2 = QtWidgets.QPushButton(parent=self.widget_5)
        self.min_1_btn_2.setGeometry(QtCore.QRect(10, 69, 211, 25))
        self.min_1_btn_2.setStyleSheet("background-color: #FFD966;\n"
"font: 11pt \"Bahnschrift\";")
        self.min_1_btn_2.setObjectName("min_1_btn_2")
        self.min_1_label_2 = QtWidgets.QLabel(parent=self.widget_5)
        self.min_1_label_2.setGeometry(QtCore.QRect(17, 23, 201, 31))
        self.min_1_label_2.setStyleSheet("font: 18pt \"OCR A Extended\";\n"
"color: black;")
        self.min_1_label_2.setObjectName("min_1_label_2")
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
    def go_to_beginnerSci(self):
        self.window = QtWidgets.QMainWindow()
        selected_text = all_texts.get('beginnerSci.txt', '')
        self.ui = min_1_typingTest.Ui_MainWindow()
        self.ui.setupUi(self.window)
        # Use selected_text so check_typing won't fall back to the default
        self.ui.selected_text = selected_text
        self.ui.text_area.setText(selected_text)
        self.ui.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
        self.window.show()
        self.MainWindow.close()
    def go_to_mediumSci(self):
        self.window = QtWidgets.QMainWindow()
        selected_text = all_texts.get('medSci.txt', '')
        self.ui = min_1_typingTest.Ui_MainWindow()
        self.ui.setupUi(self.window)
        # Use selected_text so check_typing won't fall back to the default
        self.ui.selected_text = selected_text
        self.ui.text_area.setText(selected_text)
        self.ui.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
        self.window.show()
        self.MainWindow.close()
    def go_to_advancedSci(self):
        self.window = QtWidgets.QMainWindow()
        selected_text = all_texts.get('advancedSci.txt', '')
        self.ui = min_1_typingTest.Ui_MainWindow()
        self.ui.setupUi(self.window)
        # Use selected_text so check_typing won't fall back to the default
        self.ui.selected_text = selected_text
        self.ui.text_area.setText(selected_text)
        self.ui.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
        self.window.show()
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minute Typing Test"))
        self.return_btn.setText(_translate("MainWindow", "←"))
        self.return_btn.clicked.connect(self.go_to_topic_select)
        self.heading_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Bahnschrift\'; font-size:28pt; font-weight:600; color:#ffffff;\">Science level</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">Please choose your desired level</span></p></body></html>"))
        self.min_1_btn.setText(_translate("MainWindow", "Let\'s go"))
        self.min_1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Beginner</p></body></html>"))
        self.min_3_btn.setText(_translate("MainWindow", "Let\'s go"))
        self.min_3_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Medium</p></body></html>"))
        self.min_1_btn_2.setText(_translate("MainWindow", "Let\'s go"))
        self.min_1_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Advanced</p></body></html>"))
        self.min_1_btn.clicked.connect(self.go_to_beginnerSci)
        self.min_3_btn.clicked.connect(self.go_to_mediumSci)
        self.min_1_btn_2.clicked.connect(self.go_to_advancedSci)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
