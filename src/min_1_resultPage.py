from PyQt6 import QtCore, QtGui, QtWidgets
import min_1_typingTest
import mainMenu
import os
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

# Use a raw string to avoid issues with backslashes
directory = '/Users/mac/PythonFinalProject/Python-Final-Project/assests/topic_text'
all_texts = read_all_text_files(directory)
# print(all_texts)

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
        self.main_menu_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.main_menu_btn.setGeometry(QtCore.QRect(789, 269, 171, 41))
        self.main_menu_btn.setStyleSheet("background-color: #FFD966;\n"
                                         "border-radius: 5px;\n"
                                         "color: black;\n"
                                         "font: 63 16pt \"Bahnschrift SemiBold\";")
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.other_topic_btn = QtWidgets.QPushButton(parent=self.result_container)
        self.other_topic_btn.setGeometry(QtCore.QRect(545, 269, 171, 41))
        self.other_topic_btn.setStyleSheet("background-color: #FFD966;\n"
                                         "border-radius: 5px;\n"
                                         "color: black;\n"
                                         "font: 63 16pt \"Bahnschrift SemiBold\";")
        self.other_topic_btn.setObjectName("other_topic_btn")
        self.other_topic_btn.setText("Other Topic")

        self.try_again_btn.clicked.connect(self.on_try_again_clicked)
        self.main_menu_btn.clicked.connect(lambda: self.go_to_main_menu(MainWindow))
        self.other_topic_btn.clicked.connect(self.go_to_topic_select)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.try_again_btn.clicked.connect(self.on_try_again_clicked)
        self.main_menu_btn.clicked.connect(lambda: self.go_to_main_menu(MainWindow))
        
    def go_to_topic_select(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = topicSelectMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()
    def display_results(self, wpm, level, suggested_texts, current_text, total_chars, incorrect_chars_dict):
        self.suggested_texts = suggested_texts
        self.current_text = current_text
        self.wpm_and_level_label.setText(
            f"<html><head/><body><p align=\"center\">"
            f"Your speed was <span style=\"color:#23d83e;\">{wpm:.2f} WPM</span>, "
            f"level: <span style=\"color:#23d83e;\">{level}</span></p></body></html>"
        )

        # Add a label for incorrect character stats
        self.incorrect_chars_label = QtWidgets.QLabel(parent=self.result_container)
        self.incorrect_chars_label.setGeometry(QtCore.QRect(250, 210, 800, 61))
        self.incorrect_chars_label.setStyleSheet("""
            QLabel {
                font: 25 14pt "Bahnschrift";
                background: none;
                color: black;
                padding: 10px;
            }
        """)
        self.incorrect_chars_label.setObjectName("incorrect_chars_label")
    
        stats_str = ", ".join([f"'{char}': {count}" for char, count in incorrect_chars_dict.items()])
        self.incorrect_chars_label.setText(
            f"""<html><head/><body>
                <p align="center" style="margin-right: 70px; margin-bottom: 90px;">
                    <span style="font-size:14pt; font-weight:400;">You entered </span>
                    <span style="font-size:14pt; font-weight:600; color:#23d83e;">{total_chars} characters.</span><br>
                    <span style="font-size:14pt; font-weight:400;">Incorrect characters: </span>
                    <span style="font-size:14pt; font-weight:600; color:#ea0c0f;">{stats_str}</span>
                </p>
            </body></html>"""
        )


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.heading_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\" style=\"font-size:24pt;\">Result</p></body></html>"))
        self.result_heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Typing Test Complete!</p></body></html>"))
        self.test_complete_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">You typed the </span><span style=\" font-weight:600;\">1 Minute Typing Test</span></p></body></html>"))
        self.try_again_btn.setText(_translate("MainWindow", "Try Again"))
        self.main_menu_btn.setText(_translate("MainWindow", "Main Menu"))


    def on_try_again_clicked(self):
        self.try_again(self.current_text)
        
    def try_again(self, current_text):
        print(f"Trying again with text: {current_text}")  # Debugging line
        self.window = QtWidgets.QMainWindow()
        self.ui = min_1_typingTest.Ui_MainWindow()
        self.ui.setupUi(self.window)
        if current_text:
            # Reuse the same text for the next typing session
            self.ui.selected_text = current_text
            self.ui.text_area.setPlainText(current_text)
            self.ui.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
        else:
            self.ui.selected_text = None
            self.ui.text_area.setPlainText(all_texts.get('book.txt', ''))
        self.window.show()
        self.MainWindow.hide()

    def go_to_main_menu(self, current_window):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        current_window.hide()  # Close the result window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Provide two suggested texts for testing
    MainWindow.show()
    sys.exit(app.exec())