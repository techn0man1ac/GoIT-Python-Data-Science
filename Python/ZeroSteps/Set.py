lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
print(lst)
d_lst = set(lst)
lst=list(d_lst)
print(f"numbers: {lst}, d_lst: {d_lst}")

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b)) # Всі елементи з двох множин, окрім загальних
print(a - b) #{1, 2} Різниця між двома множинами
print(a & b) #{3} Перетин двох множин
print(a | b) #{1, 2, 3, 4, 5} об'єднання

my_set = {4, 6, 'test', 'Python', 100}
print(my_set)
my_set.add('Test')
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard('Test')
print(my_set)

my_set.discard(111) # м'яке видалення
print(my_set)
