import time
# Час епохи Unix
current_time = time.time()
print(f"Поточний час: {current_time}") # Поточний час: 1714117829.7142134
time.sleep(5)
current_time = time.time()
print(f"Поточний час: {current_time}") # Поточний час: 1714117834.715658

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}") # Читабельний час: Fri Apr 26 10:52:19 2024

gmtime = time.gmtime(current_time)
print(f"time.gmtime: {gmtime}")      # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=26, tm_hour=8, tm_min=0, tm_sec=6, tm_wday=4, tm_yday=117, tm_isdst=0)
'''
Метод time.gmtime([seconds]) схожий на localtime, але повертає struct_time у UTC.
'''

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}") # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=26, tm_hour=10, tm_min=55, tm_sec=42, tm_wday=4, tm_yday=117, tm_isdst=1)

'''
Об'єкт time.struct_time в Python є іменованим кортежем,
 який використовується для представлення часу. 
 Кожен елемент кортежу має особливе значення, 
 що представляє певний компонент дати та часу:

tm_year - рік
tm_mon - місяць від 1 до 12
tm_mday - день місяця від 1 до 31
tm_hour - години від 0 до 23
tm_min - хвилини від 0 до 59
tm_sec - секунди від 0 до 59
tm_wday - день тижня від 0 до 6
tm_yday - день року від 1 до 366
tm_isdst - прапорець літнього часу. 0 означає, що літній час не діє, -1 - інформація відсутня, 1 - літній час діє
'''