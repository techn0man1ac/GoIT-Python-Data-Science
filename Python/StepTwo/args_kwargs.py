'''
Спочатку розглянемо приклад *args. 
Параметр *args використовується 
у визначенні функції для вказівки на те, 
що функція може приймати довільну 
кількість позиційних аргументів. 
Це означає, що ви можете передавати 
в функцію стільки аргументів, 
скільки потрібно, без необхідності 
їх попереднього визначення.
'''

def print_all_args(*args):
    for argym in args:
        print(argym)

print_all_args(1, 'Serhii', True, 1024 , "HELLO!")

'''
У цьому прикладі, функція print_all_args 
може приймати будь-яку кількість аргументів. 
Аргументи 1, 'hello', та True передаються 
у функцію як кортеж і в середині функції 
змінна args зберігає кортеж (1, 'hello', True).
'''