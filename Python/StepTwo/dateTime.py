from datetime import datetime, date, time


current_date = datetime.now()
date_today = datetime.today()

print(f"current_date {current_date}, date_today {date_today}")

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

# Створення об'єктів date та time
date_part = date(2023, 1, 14)
time_part = time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя) + 1
print(f"Сьогодні: {day_of_week+1} день")  

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

'''
datetime.now(): Метод повертає об'єкт datetime, який містить поточну дату та час.
datetime.date(): Цей метод повертає об'єкт date, який представляє лише дату (без часу).
datetime.time(): Метод повертає об'єкт time, який містить лише час (без дати).
datetime.combine(date, time): Цей метод використовується для об'єднання об'єктів date та time і створення нового об'єкта datetime.
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Конструктор класу datetime дозволяє створити об'єкт datetime з конкретною датою та часом.
weekday(): Метод визначає номер дня тижня для вказаної дати, де понеділок має номер 0, а неділя - 6.
'''

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023-03-14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу