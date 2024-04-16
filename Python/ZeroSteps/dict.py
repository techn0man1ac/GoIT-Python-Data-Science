# Словники
my_dict = {"name": "Serhii", "age": 32, "city": "Lutsk"}
print(f"my_dict: {my_dict}") 

my_dict["age"] = 33  # Змінює вік на 32->33
my_dict["email"] = "qwertyyyy@example.com"  # Додає нову пару ключ-значення
print(f"my_dict(new): {my_dict}") 

del my_dict["age"]
print(my_dict)
print(f"name" in my_dict, "age" in my_dict)

city = my_dict.pop("city") # зберігає у мінну та видаляє з списку
print(f"city: {city}, my_dict={my_dict}") 

my_dict.clear()
print(my_dict)
my_dict.update({"email": "qwerty@example.com", "age": 33}) # Оновлення даних у списку
print(my_dict)

age = my_dict.get("age")  # Поверне 33
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

print(f"my_dict: {my_dict}, gender: {gender}")

# Unite several dict into new one
dict_a = {'Alex':12, 'Olga':10}
dict_b = {'Alex': 12, 'Olga': 10, 'Boris': 9, 'Kostya': 10}
dict_c = {'Ira': 11, 'Vova': 6, 'Alex': 12, 'Olga': 10, 'Boris': 9, 'Kostya': 10}}

print(dict_a) #'Alex': 12, 'Olga': 10}
dict_a.update(dict_b)
print(dict_a) #{'Alex': 12, 'Olga': 10, 'Boris': 9, 'Kostya': 10}
dict_c.update(dict_a)
print(dict_c) #{'Ira': 11, 'Vova': 6, 'Alex': 12, 'Olga': 10, 'Boris': 9, 'Kostya': 10}