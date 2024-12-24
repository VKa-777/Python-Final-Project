from PyQt6 import QtCore, QtGui, QtWidgets
import min_1_resultPage
import mainMenu
import os

def read_all_text_files(directory):
    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    text_contents = {}

    for file_name in text_files:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            text_contents[file_name] = file.read()

    return text_contents

directory = '/Users/mac/PythonFinalProject/Python-Final-Project/assests/topic_text'
all_texts = read_all_text_files(directory)

class Ui_MainWindow(object):
    def back_to_main_menu(self, current_window):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        current_window.hide()
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 720)
        self.selected_text = None
        MainWindow.setMaximumSize(QtCore.QSize(1337, 720))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.heading_background = QtWidgets.QWidget(parent=self.centralwidget)
        self.heading_background.setGeometry(QtCore.QRect(0, 0, 1337, 78))
        self.heading_background.setStyleSheet("background-color: #AAC4FF;")
        self.heading_background.setObjectName("heading_background")
        
        self.return_btn = QtWidgets.QPushButton(parent=self.heading_background)
        self.return_btn.setGeometry(QtCore.QRect(20, 20, 71, 41))
        self.return_btn.clicked.connect(lambda: self.back_to_main_menu(MainWindow))
        self.return_btn.setStyleSheet("""
            QPushButton {
                border: 2px solid white;
                border-radius: 5px;
                color: white;
                font-size: 36px;
                padding-bottom: 9px;
                font-weight: bold;
                text-align: center;
            } QPushButton:hover {
                color: #eeeeee;
                border: 2px solid #eeeeee;
            }
            
            QPushButton:pressed {
                color: #ABABAB;
                border: 2px solid #ABABAB;
            }
        """)
        self.return_btn.setObjectName("return_btn")
        
        self.restart_btn = QtWidgets.QPushButton(parent=self.heading_background)
        self.restart_btn.setGeometry(QtCore.QRect(1250, 20, 71, 41))
        self.restart_btn.setStyleSheet("""
            QPushButton {
                border: 2px solid white;
                border-radius: 5px;
                color: white;
                font-size: 36px;
                padding-bottom: 7px;
                font-weight: bold;
                text-align: center;
            } QPushButton:hover {
                color: #eeeeee;
                border: 2px solid #eeeeee;
            }
            
            QPushButton:pressed {
                color: #ABABAB;
                border: 2px solid #ABABAB;
            }
        """)
        self.restart_btn.setObjectName("restart_btn")
        self.restart_btn.clicked.connect(self.replay)
        
        self.heading_label = QtWidgets.QLabel(parent=self.heading_background)
        self.heading_label.setGeometry(QtCore.QRect(514, 0, 321, 75))
        self.heading_label.setObjectName("heading_label")
        
        self.label = QtWidgets.QLabel(parent=self.heading_background)
        self.label.setGeometry(QtCore.QRect(1156, 0, 61, 78))
        self.label.setStyleSheet("color: white;\n"
                                 "font: 63 24pt \"Bahnschrift SemiBold SemiConden\";")
        self.label.setObjectName("label")
        
        self.background = QtWidgets.QWidget(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 78, 1337, 642))
        self.background.setStyleSheet("background-color: #B1B2FF;")
        self.background.setObjectName("background")
        
        self.text_area_background = QtWidgets.QWidget(parent=self.background)
        self.text_area_background.setGeometry(QtCore.QRect(40, 69, 1261, 481))
        self.text_area_background.setStyleSheet("font-size: 48pt;\n"
                                               "background-color: #fff;\n"
                                               "border-radius: 5px;")
        self.text_area_background.setObjectName("text_area_background")
        
        self.text_area = QtWidgets.QTextEdit(parent=self.text_area_background)
        self.text_area.setGeometry(QtCore.QRect(10, 10, 1231, 461))
        self.text_area.setStyleSheet("font-size: 48pt;")
        self.text_area.setObjectName("text_area")
        self.text_area.textChanged.connect(self.check_typing)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Timer setup
        self.time_left = 60  # 1 minute in seconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Update every second

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minute Typing Test"))
        self.return_btn.setText(_translate("MainWindow", "←"))
        self.restart_btn.setText(_translate("MainWindow", "⟳"))
        self.heading_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:'Bahnschrift'; font-size:28pt; font-weight:600; color:#ffffff;\">1 Minute typing test</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "1:00"))
        self.text_area.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                   "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo </span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#ea0c0f;\">li</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">gula </span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#ea0c0f;\">ege</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">t dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nas</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#ea0c0f;\">c</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">etur ridiculus mus. Donec quam felis,  ultricies nec, pellentesque eu, pretium q</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#ea0c0f;\">ui</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">s, sem. Nulla consequat massa quis enim. Donec pede justo, fring</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#ea0c0f;\">i</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600; color:#23d83e;\">lla vel, aliquet nec, vulputate  eget,</span>"
                                                   "<span style=\" font-family:'Bahnschrift'; font-size:24pt; font-weight:600;\"> </span></p></body></html>"))

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label.setText(f"{minutes}:{seconds:02d}")
        else:
            self.timer.stop()
            self.text_area.setReadOnly(True)
            self.calculate_wpm()

    def check_typing(self):
        # Use selected_text if available, otherwise use the default text
        if self.selected_text:
            expected_text = self.selected_text
        else:
            expected_text = (
                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "
                "Aenean commodo ligula eget dolor. Aenean massa. "
                "Cum sociis natoque penatibus et magnis dis parturient montes, "
                "nascetur ridiculus mus. Donec quam felis, ultricies nec, "
                "pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. "
                "Donec pede justo, fringilla vel, aliquet nec, vulputate eget,"
            )

        user_text = self.text_area.toPlainText()
        formatted_text = ""
        for i, char in enumerate(user_text):
            if i < len(expected_text) and char == expected_text[i]:
                formatted_text += f'<span style="color:#23d83e;">{char}</span>'
            else:
                formatted_text += f'<span style="color:#ea0c0f;">{char}</span>'

        cursor = self.text_area.textCursor()
        cursor_position = cursor.position()
        self.text_area.blockSignals(True)
        self.text_area.setHtml(formatted_text)
        cursor.setPosition(cursor_position)
        self.text_area.setTextCursor(cursor)
        self.text_area.blockSignals(False)

    def calculate_wpm(self):
        user_text = self.text_area.toPlainText()
        num_chars = len(user_text)
        wpm = num_chars / 5  # Since the test is 1 minute, we don't need to divide by time
        level = self.determine_level(wpm)
        self.open_result_page(wpm, level)

    def determine_level(self, wpm):
        if wpm < 20:
            return "Beginner"
        elif 20 <= wpm < 40:
            return "Intermediate"
        elif 40 <= wpm < 60:
            return "Advanced"
        else:
            return "Expert"

    def open_result_page(self, wpm, level):
        self.window = QtWidgets.QMainWindow()
        self.ui = min_1_resultPage.Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Decide suggested texts
        suggested_texts = []
        if level in ["Advanced", "Expert"]:
            suggestion_msg = "You did great! Try a harder text next time."
            suggested_texts = [
                all_texts.get('what-screams-i-have-depression.txt', 'Default Hard Text'),
                all_texts.get('very_hard_text.txt', 'Default Very Hard Text')
            ]
        else:
            suggestion_msg = "Keep practicing! Try an easier text to improve your skills."
            suggested_texts = [
                all_texts.get('book.txt', 'Default Book Text'),
                all_texts.get('cats.txt', 'Default Cats Text')
            ]
        self.ui.display_results(wpm, level, suggested_texts)
        # Override the "Try Again" button in result page to reset to default text
        self.ui.try_again_btn.clicked.disconnect()
        self.ui.try_again_btn.clicked.connect(self.click_default_text)

        self.window.show()
        self.MainWindow.close()
        QtWidgets.QMessageBox.information(self.window, "Suggestion", suggestion_msg)
        self.suggested_texts = suggested_texts

    def click_suggested_text(self, new_text):
        # Set the chosen text, then replay test
        print(f"Suggested Text Selected: {new_text}")  # Debugging line
        self.selected_text = new_text
        self.replay()

    def click_default_text(self):
        # Reset to default text, then replay test
        self.selected_text = None
        self.replay()

    def replay(self):
        self.time_left = 60  # Reset the timer to 1 minute
        self.label.setText("1:00")  # Reset the label
        self.text_area.setReadOnly(False)  # Make the text area editable
        self.text_area.clear()  # Clear the text area

        # Set the text area to one of the suggested texts
        if self.selected_text:
            self.text_area.setPlainText(self.selected_text)
        else:
            # Default text
            self.text_area.setPlainText(all_texts.get('book.txt', ''))
        self.timer.start(1000)  # Restart the timer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())