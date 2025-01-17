# Form implementation generated from reading ui file 'min_1_typingTest.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mainMenu
import min_1_resultPage
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

def get_text_files_directory():
    # Get the directory path of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Join with the relative path to the 'assets/topic_text' directory
    return os.path.join(base_dir, r'assests/topic_text')

directory = get_text_files_directory()
print(directory)
all_texts = read_all_text_files(directory)
# print(all_texts)

class Ui_MainWindow(object):
    
    def back_to_main_menu(self, current_window):
        self.timer.stop()
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        current_window.close()

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.selected_text = None
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
        self.restart_btn.setObjectName("restart_btn")
        self.restart_btn.clicked.connect(self.replay)
        self.heading_label = QtWidgets.QLabel(parent=self.heading_background)
        self.heading_label.setGeometry(QtCore.QRect(514, 0, 321, 75))
        self.heading_label.setObjectName("heading_label")
        self.label = QtWidgets.QLabel(parent=self.heading_background)
        self.label.setGeometry(QtCore.QRect(1156, 0, 61, 78))
        self.label.setStyleSheet("color: white;\n"
"font: 63 24pt \"Bahnschrift SemiBold SemiConden\";\n"
"")
        self.label.setObjectName("label")
        self.background = QtWidgets.QWidget(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 78, 1337, 642))
        self.background.setStyleSheet("background-color: #B1B2FF;\n"
"")
        self.background.setObjectName("background")
        self.text_area_background = QtWidgets.QWidget(parent=self.background)
        self.text_area_background.setGeometry(QtCore.QRect(40, 69, 1261, 181))
        self.text_area_background.setStyleSheet("font-size: 48pt;\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"")
        self.text_area_background.setObjectName("text_area_background")
        self.text_area = QtWidgets.QTextEdit(parent=self.text_area_background)
        self.text_area.setGeometry(QtCore.QRect(10, 10, 1231, 171))
        self.text_area.setStyleSheet("font-size:48pt; font-weight:400; font-style:normal;")
        self.text_area.setObjectName("text_area")
        self.text_area.setReadOnly(True)
        self.text_area.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)  # Disable text selection
        self.text_area.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)  # Disable context menu

        self.typing_area_background_2 = QtWidgets.QWidget(parent=self.background)
        self.typing_area_background_2.setGeometry(QtCore.QRect(40, 310, 1261, 181))
        self.typing_area_background_2.setStyleSheet("font-size: 48pt;\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"")
        self.typing_area_background_2.setObjectName("typing_area_background_2")
        self.typing_area = QtWidgets.QTextEdit(parent=self.typing_area_background_2)
        self.typing_area.setGeometry(QtCore.QRect(10, 10, 1231, 171))
        self.typing_area.setStyleSheet("font-size: 22pt;")
        self.typing_area.setObjectName("typing_area")
        self.typing_area.textChanged.connect(self.check_typing)
        
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


        # Timer setup
        self.time_left = 10  # 1 minute in seconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Update every second

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minute Typing Test"))
        self.return_btn.setText(_translate("MainWindow", "←"))
        self.restart_btn.setText(_translate("MainWindow", "⟳"))
        self.heading_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:'Bahnschrift'; font-size:28pt; font-weight:600; color:#ffffff;\">1 Minute typing test</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "1:00"))
        self.text_area.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bahnschrift\'; font-size:22pt; font-weight:600; color:#000000;\">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis,  ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate  eget, </span></p></body></html>"))
        self.typing_area.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

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

        user_text = self.typing_area.toPlainText()
        
        formatted_text = ""
        for i, char in enumerate(user_text):
            if i < len(expected_text) and char == expected_text[i]:
                formatted_text += f'<span style="color:#23d83e;">{char}</span>'
            else:
                formatted_text += f'<span style="color:#ea0c0f;">{char}</span>'

        cursor = self.typing_area.textCursor()
        cursor_position = cursor.position()

        self.typing_area.blockSignals(True)
        self.typing_area.setHtml(formatted_text)
        cursor.setPosition(cursor_position)
        self.typing_area.setTextCursor(cursor)
        self.typing_area.blockSignals(False)

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
            
    def determine_level(self, wpm):
        if wpm < 20:
            return "Beginner"
        elif 20 <= wpm < 40:
            return "Intermediate"
        elif 40 <= wpm < 60:
            return "Advanced"
        else:
            return "Expert"
    def calculate_accuracy(self, user_text, expected_text):
        if not user_text:  # Avoid division by zero
            return 0.0
        correct_chars = sum(1 for i in range(min(len(user_text), len(expected_text))) 
                            if user_text[i] == expected_text[i])
        return (correct_chars / len(user_text)) * 100
    def count_incorrect_characters(self, user_text, expected_text):
        from collections import Counter
        incorrect_dict = Counter()
        length = min(len(user_text), len(expected_text))
        for i in range(length):
            if user_text[i] != expected_text[i]:
                incorrect_dict[expected_text[i]] += 1
        # Count extra characters if user typed longer than expected
        for i in range(length, len(user_text)):
            incorrect_dict[expected_text[i]] += 1
        return dict(incorrect_dict)
    def calculate_wpm(self):
        user_text = self.typing_area.toPlainText()
        wpm = len(user_text) / 5
        level = self.determine_level(wpm)
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
        accuracy = self.calculate_accuracy(user_text, expected_text)
        incorrect_chars_dict = self.count_incorrect_characters(user_text, expected_text)
        print(f"Calculated WPM: {wpm}, Level: {level}, Accuracy: {accuracy:.2f}%")
        self.open_result_page(wpm * accuracy * 0.01, level, self.selected_text, len(user_text), incorrect_chars_dict)

    def open_result_page(self, wpm, level, current_text, total_chars_entered, incorrect_chars_dict):
        print(f"Opening result page with text: {current_text}")  # Debugging line
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
        self.ui.display_results(wpm, level, suggested_texts, current_text, total_chars_entered, incorrect_chars_dict)
        # Override the "Try Again" button in result page to reset to default text
        self.ui.try_again_btn.clicked.disconnect()
        self.ui.try_again_btn.clicked.connect(lambda: self.ui.try_again(current_text))
        self.window.show()
        self.MainWindow.close()
        QtWidgets.QMessageBox.information(self.window, "Suggestion", suggestion_msg)

    def click_suggested_text(self, new_text):
        # Set the chosen text, then replay test
        print(f"Suggested Text Selected: {new_text}")  # Debugging line
        self.selected_text = new_text
        self.expected_text = new_text
        self.expected_text.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
        self.replay()

    def click_default_text(self):
        # Reset to default text, then replay test
        self.selected_text = None
        self.replay()


    def replay(self):
        # Reset the timer to 1 minute
        self.time_left = 60
        self.label.setText("1:00")  # Reset the label
        self.typing_area.clear()  # Clear the text area
    
        if self.selected_text:
            self.text_area.setPlainText(self.selected_text)
            self.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
            print(f"Set text area to selected_text: {self.selected_text}")  # Debugging line
        else:
            # Default text
            default_text = all_texts.get('book.txt', '')
            self.text_area.setPlainText(default_text)
            self.text_area.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold\"; color: black")
            print(f"Set text area to default text: {default_text}")  # Debugging line
    
        self.text_area.repaint()  # Ensure the text area is updated
        self.timer.start(1000)  # Restart the timer
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())