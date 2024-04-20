import sys
import random
from datetime import datetime
import ai_module as ai_module #include ai_module.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel

responses_list = []

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stupid AI")
        self.setGeometry(100, 100, 480, 250)
        self.setStyleSheet("background-color: #333; color: white;")

        self.text_field = QLineEdit(self)
        self.text_field.setGeometry(50, 50, 200, 30)
        self.text_field.setStyleSheet("background-color: #444; color: white; border: 1px solid gray; padding: 5px;")
        self.text_field.setPlaceholderText("Задайте Ваше питання")
        self.text_field.textChanged.connect(self.on_text_changed)

        self.button = QPushButton("Отримати відповідь", self)
        self.button.setGeometry(270, 50, 150, 30)
        self.button.setStyleSheet("background-color: #00bcd4; color: white; border: 1px solid gray; padding: 5px;")
        self.button.clicked.connect(self.button_clicked)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 100, 370, 100)
        self.result_label.setStyleSheet("background-color: #444; color: white; border: 1px solid gray; padding: 5px;")
        self.result_label.setWordWrap(True)

    def button_clicked(self):
        text = self.text_field.text()

        user_question = text + " " + str(datetime.now())
        random.seed(user_question)
        category, response = ai_module.get_response(user_question)
        print("Категорія:", category)
        print("Відповідь:", response)
        responses_list.append((user_question, category, response))

        self.result_label.setText("Всесвіт каже: " + response)

    def on_text_changed(self, text):
        if text == "":
            self.result_label.setText("")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
