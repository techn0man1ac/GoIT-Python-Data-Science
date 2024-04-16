'''
Важливо пам'ятати, що не можна робити, поки ітеруєтеся за словником: 
не можна видаляти елементи із словника, не можна додавати елементи у словник. 
Але можна перезаписувати значення, якщо ви ітеруєтеся за ключами. 
Теж саме стосуються і списку - не можна видаляти елементи списку та не можна 
додавати елементи у список під час ітерацій в циклі.
'''
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

for key in numbers:
    print(key)

'''
1
2
3
4
'''

for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

'''
one
two
three
four
'''

for key, value in numbers.items():
    print(key, value)
'''
1 one
2 two
3 three
4 four
'''