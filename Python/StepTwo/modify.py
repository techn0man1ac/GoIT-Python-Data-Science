def modify_string(original: str) -> str:
    original = "Changed"
    return original

str_var = "Original"
print(id(modify_string(str_var)))  # Changed
print(id(str_var))                # Original

'''
У цьому прикладі, навіть після зміни рядка 
в функції modify_string, оригінальна змінна 
str_var залишається незмінною.
'''

def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # output [1, 2, 3, 4]

'''
Змінні типи, як списки list, словники dict, множини set, 
можуть змінюватися. Коли змінний об'єкт передається у функцію, 
передається посилання на цей об'єкт, і зміни, 
зроблені всередині функції, відображаються на оригінальному об'єкті.
'''

def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # output: [1, 2, 3]

'''
Використовуйте метод copy() для створення копій 
змінних об'єктів, якщо не хочете змінювати оригінал.
'''