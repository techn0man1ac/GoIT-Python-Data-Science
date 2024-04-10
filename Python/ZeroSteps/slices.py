s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2] # від 0 значеня і так 10 разів, з кроком в 2
odd_numbers_pair = even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
print(odd_numbers) # [1, 3, 5, 7, 9] непарні
print(odd_numbers_pair) # [2, 4, 6, 8, 10] парні
print(three_numbers) # [3, 6, 9] кратні 3-м
copy_numbers = numbers[:] # Замість copy
print(copy_numbers)