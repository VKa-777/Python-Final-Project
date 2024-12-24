from PyQt6 import QtCore, QtGui, QtWidgets
import min_1_typingTest
import mainMenu
import os

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

# Use a raw string to avoid issues with backslashes
directory = '/Users/mac/PythonFinalProject/Python-Final-Project/assests/topic_text'
all_texts = read_all_text_files(directory)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Store the MainWindow instance
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
        self.heading_label.setObjectName("heading_label")
        
        self.result_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.result_container.setGeometry(QtCore.QRect(40, 156, 1261, 421))
        self.result_container.setStyleSheet("background-color: #EEF1FF;\n"
                                            "border-radius: 10px;")
        self.result_container.setObjectName("result_container")
        
        # Define buttons that go in result_container
        self.hard_text_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.hard_text_btn.setGeometry(QtCore.QRect(300, 329, 171, 41))
        self.hard_text_btn.setStyleSheet("background-color: #FFD966;\n"
                                         "border-radius: 5px;\n"
                                         "color: black;\n"
                                         "font: 63 16pt \"Bahnschrift SemiBold\";")
        self.hard_text_btn.setObjectName("hard_text_btn")
        self.hard_text_btn.clicked.connect(self.click_hard_text)
        
        self.very_hard_text_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.very_hard_text_btn.setGeometry(QtCore.QRect(789, 329, 171, 41))
        self.very_hard_text_btn.setStyleSheet("background-color: #FFD966;\n"
                                             "border-radius: 5px;\n"
                                             "color: black;\n"
                                             "font: 63 16pt \"Bahnschrift SemiBold\";")
        self.very_hard_text_btn.setObjectName("very_hard_text_btn")
        self.very_hard_text_btn.clicked.connect(self.click_very_hard_text)
        
        self.result_heading = QtWidgets.QLabel(parent=self.result_container)
        self.result_heading.setGeometry(QtCore.QRect(476, 14, 321, 46))
        self.result_heading.setStyleSheet("color: black;\n"
                                          "font: 63 28pt \"Bahnschrift SemiBold SemiConden\";\n"
                                          "font-weight: bold;")
        self.result_heading.setObjectName("result_heading")
        
        self.test_complete_label = QtWidgets.QLabel(parent=self.result_container)
        self.test_complete_label.setGeometry(QtCore.QRect(375, 74, 500, 61))
        self.test_complete_label.setStyleSheet("font: 25 20pt \"Bahnschrift\";\n"
                                               "background: none;\n"
                                               "color: black")
        self.test_complete_label.setObjectName("test_complete_label")
        
        self.wpm_and_level_label = QtWidgets.QLabel(parent=self.result_container)
        self.wpm_and_level_label.setGeometry(QtCore.QRect(250, 141, 800, 61))
        self.wpm_and_level_label.setStyleSheet("font: 25 20pt \"Bahnschrift\";\n"
                                              "background: none;\n"
                                              "color: black")
        self.wpm_and_level_label.setObjectName("wpm_and_level_label")
        
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
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.try_again_btn.clicked.connect(lambda: self.try_again(self.current_text))
        self.main_menu_btn.clicked.connect(self.go_to_main_menu)

    def display_results(self, wpm, level, suggested_texts, current_text):
        self.suggested_texts = suggested_texts
        self.current_text = current_text
        self.wpm_and_level_label.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Your speed was </span>"
            f"<span style=\" font-weight:400; color:#23d83e;\">{wpm:.2f} WPM</span>"
            f"<span style=\" font-weight:400;\"> and your level is </span>"
            f"<span style=\" font-weight:400; color:#23d83e;\">{level}</span></p></body></html>"
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.heading_label.setText(_translate("MainWindow", "Result"))
        self.result_heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Typing Test Complete!</p></body></html>"))
        self.test_complete_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">You typed the </span><span style=\" font-weight:600;\">1 Minute Typing Test</span></p></body></html>"))
        self.try_again_btn.setText(_translate("MainWindow", "Try Again"))
        self.main_menu_btn.setText(_translate("MainWindow", "Main Menu"))

    def click_hard_text(self):
        if hasattr(self, 'suggested_texts') and len(self.suggested_texts) > 0:
            selected_text = self.suggested_texts[0]
            self.window = QtWidgets.QMainWindow()
            self.ui = min_1_typingTest.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.selected_text = selected_text
            # ▼ Add this to override default Lorem:
            self.ui.text_area.setPlainText(selected_text)
            self.window.show()
            self.MainWindow.close()
        else:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "No Hard Text available.")

    def click_very_hard_text(self):
        if hasattr(self, 'suggested_texts') and len(self.suggested_texts) > 1:
            selected_text = self.suggested_texts[1]
            print(f"Very Hard Text Selected: {selected_text}")  # Debugging line
            self.window = QtWidgets.QMainWindow()
            self.ui = min_1_typingTest.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.selected_text = selected_text
            self.window.show()
            self.MainWindow.close()
        else:
            QtWidgets.QMessageBox.warning(self.MainWindow, "Error", "No Very Hard Text available.")

    def try_again(self, current_text):
        print(f"Trying again with text: {current_text}")  # Debugging line
        self.window = QtWidgets.QMainWindow()
        self.ui = min_1_typingTest.Ui_MainWindow()
        self.ui.setupUi(self.window)
        if current_text:
            # Reuse the same text for the next typing session
            self.ui.selected_text = current_text
            self.ui.text_area.setPlainText(current_text)
        else:
            self.ui.selected_text = None
            self.ui.text_area.setPlainText(all_texts.get('book.txt', ''))
        self.window.show()
        self.MainWindow.close()  # Close the result window

    def go_to_main_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()  # Close the result window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Provide two suggested texts for testing
    ui.display_results(80, "Expert", [
        all_texts.get('what-screams-i-have-depression.txt', 'Default Hard Text'),
        all_texts.get('very_hard_text.txt', 'Default Very Hard Text')
    ], current_text=all_texts.get('book.txt', 'Default Book Text'))
    MainWindow.show()
    sys.exit(app.exec())