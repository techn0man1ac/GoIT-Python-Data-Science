def total_salary(path):
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо всі рядки з файлу
            lines = file.readlines()
            # Ініціалізуємо змінні для обчислення загальної суми та кількості розробників
            total_salary = 0
            num_developers = 0

            # Проходимося по кожному рядку файлу
            for line in lines:
                # Розділяємо рядок на прізвище та заробітну плату
                data = line.strip().split(',')
                # Перетворюємо заробітну плату на ціле число
                salary = int(data[1])
                # Додаємо заробітну плату до загальної суми
                total_salary += salary
                # Збільшуємо лічильник розробників
                num_developers += 1

            # Обчислюємо середню заробітну плату
            average_salary = total_salary / num_developers

            # Повертаємо загальну суму та середню заробітну плату у вигляді кортежу
            return total_salary, average_salary

    except FileNotFoundError:
        # Обробляємо випадок, коли файл не знайдено
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        # Обробляємо інші можливі помилки
        print(f"Сталася помилка: {e}")
        return None, None

# Приклад використання функції
total, average = total_salary("HomeWork/4/Salarys/salary.db")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
