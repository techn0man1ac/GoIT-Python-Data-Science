def get_cats_info(path):
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []  # Створюємо пустий список для зберігання інформації про котів
            
            # Проходимося по кожному рядку файлу
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_data = line.strip().split(',')
                
                # Формуємо словник для кожного кота
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                
                # Додаємо словник про кота до списку
                cats_info.append(cat_info)
            
            return cats_info  # Повертаємо список інформації про котів
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

# Приклад використання функції
cats_info = get_cats_info("HomeWork/4/Cats/cats.db")
if cats_info is not None:
    print(cats_info)