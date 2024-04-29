'''
Метод split() у Python використовується для розбиття 
рядка на список підрядків на основі вказаного роздільника. 
Якщо роздільник не вказаний, за замовчуванням використовується пробіл.
'''
text = "hello world and Serhii"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

'''
У цьому прикладі рядок "hello world" розділяється 
на список з двох елементів: 'hello' та 'world' за пробілом.

Якщо ми хочемо розділити рядок вказаним роздільником то:
'''
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

result1 = ' '.join(result) #
print(result1)  # Виведе: apple banana cherry

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements) # кома як роздільник
print(result)  # Виведе: 'earth, air, fire, water'
'''
Якщо потрібно видалити зайві пробіли на початку 
і в кінці рядка, є спеціальний метод strip
'''
clean = '   spacious   '.strip()
print(clean) # spacious

'''
У цього метода є два "брати":
"лівий", lstrip, видаляє тільки пробіли на початку рядка;
та "правий", rstrip, видаляє тільки пробіли в кінці рядка.
'''
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) # Hello Python

'''
Метод replace() у Python використовується для заміни 
ідрядка на інший підрядок у рядку. Цей метод повертає 
новий рядок, де кожне входження вказаного підрядка 
замінено на інший підрядок.
Якщо нам треба обмеження кількості замін, то:
'''
text_ = "one fish, two fish, red fish, blue fish"
new_text_ = text_.replace("fish", "bird", 2)
print(new_text_)  # one bird, two bird, red fish, blue fish

text = "Hello, world!"
new_text = text.replace(" world", "") # також можна видалити підрядок
print(new_text) #Hello,!
'''
Для видалення фіксованої послідовності 
на початку рядка є метод removeprefix.
Виведення, в першому випадку 'Test' є 
префіксом рядка та буде видалений, 
в другому 'Hook' це суфікс рядка і видалений не буде:
'''
print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook
# Є парний метод для видалення послідовності в кінці рядка, removesuffix:
print('TestHook'.removesuffix('Test')) # TestHook
print('TestHook'.removesuffix('Hook')) # Test