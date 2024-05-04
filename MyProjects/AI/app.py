import os
from flask import Flask, render_template, request
import sqlite3
from flask import g
import ollama

app = Flask(__name__)

# Database connection setup
db_path = 'MyProjects/AI/dialog_history.db'

def get_db():
    if not hasattr(g, 'db'):
        g.db = sqlite3.connect(db_path)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Create dialog history table (if not exists)
with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS dialog_history (
        user_input TEXT,
        bot_response TEXT
    )""")
    db.commit()

# Load dialog history from database
def load_dialog():
    dialog_history = []
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM dialog_history')
    for row in cursor.fetchall():
        dialog_history.append((row[0], row[1]))
    return dialog_history

# Save dialog to database
def save_dialog(user_input, bot_response):
    cursor = get_db().cursor()
    cursor.execute('INSERT INTO dialog_history (user_input, bot_response) VALUES (?, ?)', (user_input, bot_response))
    get_db().commit()

# Routes
@app.route('/')
def index():
    dialog_history = load_dialog()
    return render_template('index.html', dialog_history=dialog_history)

@app.route('/chat', methods=['POST'])
def chat():
    # Перевірка, чи містить запит поле 'user_input'
    if 'user_input' not in request.form:
        return "Поле 'user_input' не знайдено у вашому запиті."

    user_input = request.form['user_input']
    if len(user_input) < 3:
        return "Введіть повідомлення довжиною щонайменше 3 символи."

    # Перевірка, чи є в базі даних кешована відповідь для введеного повідомлення
    cached_response = get_cached_response(user_input)
    if cached_response:
        return cached_response

    # Якщо відповідь не знайдено в кеші, отримати відповідь з зовнішнього сервісу
    try:
        response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': user_input}])
        bot_response = response['message']['content']
    except Exception as e:
        bot_response = f"Виникла помилка: {str(e)}"

    # Збереження відповіді в кеш бази даних
    save_dialog(user_input, bot_response)

    return bot_response

# Функція для отримання кешованої відповіді з бази даних
def get_cached_response(user_input):
    cursor = get_db().cursor()
    cursor.execute('SELECT bot_response FROM dialog_history WHERE user_input = ?', (user_input,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Повертаємо знайдену відповідь
    return None  # Повертаємо None, якщо відповідь не знайдено

if __name__ == '__main__':
    app.run(debug=True, port="80", host="192.168.0.101")
