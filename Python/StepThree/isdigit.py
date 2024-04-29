number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")

for char in "Hello 123h5":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
'''
'H' - не цифра
'e' - не цифра
'l' - не цифра
'l' - не цифра
'o' - не цифра
' ' - не цифра
'1' - це цифра
'2' - це цифра
'3' - це цифра
'h' - не цифра
'5' - це цифра
'''