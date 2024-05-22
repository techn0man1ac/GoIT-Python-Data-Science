from pathlib import Path

# Початковий шлях до файлу
original_path = Path("Python/StepFive/examplePl.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path) # Python\StepFive\report.txt

# Початковий шлях до файлу 
original_path = Path("Python/StepFive/examplePl.txt")

# Зміна імені файлу
new_path = original_path.with_suffix(".md") 
print(new_path) # Python\StepFive\examplePl.md

original_path = Path("Python/StepFive/examplePl.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")

print(original_path) # Python\StepFive\examplePl.txt
print(new_path) # Python\StepFive\report.txt

'''
У цьому прикладі, original_path залишається незмінним, а new_path 
є новим об'єктом Path, який відображає шлях з новим іменем файлу.
'''

original_path = Path("Python/StepFive/test.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)

'''
Щоб фізично змінити ім'я файлу на диску, потрібно використовувати 
методи для роботи з файловою системою, наприклад, rename. 
Цей виклик змінить ім'я файлу example.txt на report.txt у директорії documents на диску.
'''
