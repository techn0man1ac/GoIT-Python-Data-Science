import sys
import random
from datetime import datetime
import ai_module as ai_module #include ai_module.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTextEdit

responses_list = []

class ChatBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Простий чат-бот")
        self.setGeometry(100, 100, 400, 400)

        # Віджет для відображення чату
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        # Віджет для введення тексту
        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.send_message)

        # Розміщення віджетів на головному вікні
        layout = QVBoxLayout()
        layout.addWidget(self.chat_display)
        layout.addWidget(self.input_field)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def send_message(self):
        message = self.input_field.text()
        self.input_field.clear()

        # Додати повідомлення до відображення чату
        self.add_message_to_chat("Ви:", message)

        # Отримати відповідь від чат-бота
        response = self.get_chatbot_response(message)
        self.add_message_to_chat("Чат-бот:", response)

    def add_message_to_chat(self, sender, message):
        self.chat_display.append(f"<b>{sender}</b>: {message}")

    def get_chatbot_response(self, message):
        user_question = message + " " + str(datetime.now())
        category, response = ai_module.get_response(user_question)
        print("Категорія:", category)
        print("Відповідь:", response)
        responses_list.append((user_question, category, response))
        return response

def main():
    app = QApplication(sys.argv)
    window = ChatBot()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
