'''
У цьому прикладі, функція concatenate може 
приймати будь-яку кількість рядкових аргументів, 
які потім конкатенуються в один рядок. 
Під час виклику функції, всі позиційні аргументи, 
передані після останнього визначеного аргументу, 
будуть упаковані в кортеж під ім'ям, 
що йде після символу * і зазвичай це ім'я tpls, 
але може бути будь-яке інше ім'я.
'''
def concatenate(*tpls) -> str:
    result = ""
    for arg in tpls:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

def concatenateStr(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result

print(concatenateStr("Sweet", " ", "nice", "!"))

'''
Ми замінили назву параметру args на 
strings і в нас все продовжує працювати.
'''