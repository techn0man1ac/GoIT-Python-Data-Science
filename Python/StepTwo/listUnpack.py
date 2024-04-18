'''
Тут a отримає перший елемент списку 1, а rest стане 
списком, що містить всі інші елементи та дорівнюватиме [2, 3].
'''

my_list = [1, 2, 3]
a, _, c = my_list
a, *rest = my_list
print('rest = ', rest, 'my_list = ', my_list) # rest =  [2, 3] my_list =  [1, 2, 3]

'''
Розпакування списків корисне, коли вам потрібно швидко 
присвоїти значення зі списку змінним або коли вам 
потрібно ігнорувати деякі з цих значень.
Розпакування словників працює трохи інакше і зазвичай 
використовується під час передачі аргументів у функцію.
'''
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Serhii", "age": 33}
greet(**person_info)

'''
У цьому прикладі **person_info розпаковує словник person_info, 
і його ключі та значення передаються як ключові аргументи в функцію greet.
'''