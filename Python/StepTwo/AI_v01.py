import random
from datetime import datetime

responses = {
    "positive": ["Можливо", "Так буде,", "Так", "Однозначно", "Має бути так", 
                 "Однозначно так", "Хороші шанси", "Здійсниться,"],
    "neutral": ["Питайте пізніше", "Зараз я не можу відповісти", 
                "Задайте запитання точніше", "Багато сумнівів", "Повторіть питання,"],
    "negative": ["Без сумнівів, багато сумнівів,", "Поганий прогноз", "Зірки кажуть ні", 
                 "Зараз невідомо"]
}


def get_user_input():
    while True:
        question = input("Задайте своє питання: ").strip()
        if question:
            return question
        print("Неправильний ввід, буль ласка повторіть.")

def generate_response(question):
    random.seed(question + str(datetime.now()))
    response_category = random.choice(["positive", "neutral", "negative"])
    return random.choice(responses[response_category])

def main():
    question = get_user_input()
    response = generate_response(question)
    print(response)

if __name__ == "__main__":
    main()