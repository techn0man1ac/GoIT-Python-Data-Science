import random

dice_roll = random.randint(1, 6) # 1..6
print(f"Ви кинули {dice_roll}")

num = random.random() # 0.0..0.9999999999999999
print(num)

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

print(random.randrange(10))  # Верхня межа є 10, але не включається 0..9

'''
Наприклад симуляція пострілу по мішені, але необхідно 
вибрати випадковий номер від 1 до 10, та лише непарні числа
'''
target = random.randrange(1, 11, 2) # 1, 3, 5, 7, 9, 11
print(f"Ціль: {target}") 