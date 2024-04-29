import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result) # 4 3 3

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

print(0.1 + 0.2 == 0.3)  # Це повертає False
print(0.1 + 0.2) # 0.30000000000000004

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

'''
Функція math.isclose використовується для порівняння 
двох чисел з певною допустимою похибкою. 
Це корисно для порівняння дійсних чисел, 
де пряме порівняння може бути ненадійним.
'''
r = math.isclose(0.1, 0.10000000009)
print(r)  # Це поверне True

'''
У цьому прикладі math.isclose знову використовується 
для порівняння двох чисел, де друге число 
відрізняється від першого на дуже малу величину.
'''