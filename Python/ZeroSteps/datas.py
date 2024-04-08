my_list = [1, "Hello", 3.14]
my_list.append(4) # метод, який додає ще один елемент "4" в список
my_list.remove(3.14) # метод для видаленя
print(f"Datas: {my_list} ")

some_iterable = ["a", "b", "c"]
some_iterable[1] = "-1" # Перезаписую "b" на "-1"
first_letter = some_iterable[2]
middle_one = some_iterable[1]
last_letter = some_iterable[0]

print(f"1: {first_letter}, 2: {middle_one}, 3: {last_letter} ")

chars = ['a', 'b', 'c']
last = chars.pop(1) # Забирає вміст списку з першої комірки
print(f"last: {last}  chars: {chars}")

# Конкатинація

chars = ['x', 'y', 'z']
numbers = [9, 8]
chars.extend(numbers)
print(f"numbers: {numbers}  chars: {chars}")
chars.insert(1, "b") # ['x', 'y', 'z', 9, 8] -> ['x', 'b', 'y', 'z', 9, 8]
print(f"chars: {chars}")
chars.clear() # Очистка списку
print(f"clear: {chars}")
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') # 2 — це індекс елемента 'c' у списку chars.
print(f"c_ind: {c_ind}") 
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази
my_list12345 = [1, 2, 3, 4, 5]
print(len(my_list12345)) # 5 елементів у списку
