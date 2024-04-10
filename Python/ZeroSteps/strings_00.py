name = "Serhii"
age = 32
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")


game_string = 'My favorite "Game"'
print(game_string)

s = "Hello world!1"
print(s[0])# H
print(s[-1])# !

s = "Hello" 
print(s.upper()) # Виведе 'HELLO'

s = "Some Text"
print(s.lower())  # Виведе 'some text'

s = "Start000.jpg"
print(s.startswith("Start"))  # Виведе True
print(s.endswith(".jpg"))  # Виведе True

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))