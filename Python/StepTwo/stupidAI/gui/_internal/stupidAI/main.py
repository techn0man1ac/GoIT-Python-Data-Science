# Основний файл
import random
from datetime import datetime
import ai_module as ai_module #include ai_module.py

responses_list = []

while True:
    user_question = input("Задайте своє питання: ") + " " + str(datetime.now())
    random.seed(user_question)
    category, response = ai_module.get_response(user_question)
    #print("Категорія:", category)
    print("Відповідь:", response)
    responses_list.append((user_question, category, response))

    continue_query = input("Продовжити? (так/ні): ")
    if continue_query.lower() != "т":
        break

print("Список питань та відповідей:")
for question, category, response in responses_list:
    print("Питання:", question)
    print("Категорія:", category)
    print("Відповідь:", response)
    print("-" * 20)