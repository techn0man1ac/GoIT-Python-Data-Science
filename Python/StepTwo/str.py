string = '   Hello, world! !111     \n!'
print(string)

stripped_string = string.strip()
print(stripped_string)

string = '   apple,   banana, orange  '
fruits = string.split(',') # Якщо не вказується роздільник, то рахується пробіл " "
print(f'Fruits: {fruits}') # Fruits: ['apple,', 'banana,', 'orange']
for fruit in fruits:
    print(fruit.strip(), end=',') # apple,,banana,,orange,['apple', 'banana', 'orange']

string = 'apple,banana,orange'
fruits = string.split(',')
print(fruits)
new_string = '\t'.join(fruits) # *.join об'єднує всі елементи ітерабельних об'єктів
print(new_string)
new_string = '-'.join(fruits)
print(new_string)
new_string = '\n'.join(fruits)
print(new_string)
def custom_join(iterable_object, separator):
    return f'{separator}'.join(iterable_object)

new_string = '-'.join(fruits)

print(f'custom_join:{custom_join(fruits, '-')}') # custom_join:apple-banana-orange

string = 'Hello world! Hello everyone!'
print(string)
print(string.find('!'))        # 11
print(string.find('@'))        # -1
print(string.find('!', 5, 8))  # -1
print(string.find('!', 12))    # 27
print(string.find('!', 0, 8))  # -1
print(string.index('!'))       # 11
# print(string.index('@')) #ValueError: substring not found
print(string.find('!'))        # 11 - мінімальний індекс
print(string.rfind('!'))       # 27 - максимальний індекс який я хочу знайти

string = 'Hello world! Hello everyone!'
print(test:=string.replace('world', 'Python'))

string = '123'
print(string.isdigit()) # Це цифри

string = 'abc'
print(string.isalpha()) # Це строка

string = 'abc'
print(string.islower())

string = 'ABC'
print(string.isupper())

print(test)


string = "Ми вчимо Java? "

print(string.replace('Java', 'Python').removesuffix('? '))