name = input("Enter Name:")
age = int(input("Enter age:"))
has_driver_licence = input("Have licence(True/False)?")

print(has_driver_licence)

if name and age >= 18 and has_driver_licence == 'True':
    print(f"User {name} can rent a car")
else:
    print(f"User {name} can't rent a car")

'''
AND (і): Операція повертає True, якщо обидва операнди є True. Наприклад, True AND True є True, в той час як True AND False є False.
OR (або): Операція повертає True, якщо хоча б один з операндів є True. Наприклад, True OR False є True.
NOT (ні): Унарна операція, яка інвертує значення; True стає False, а False стає True.
'''