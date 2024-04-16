condition = True
start = 1

while condition:
    if start == 7:
        condition = False
    print(start)
    start += 1

print('Out of the loop')

while start <= 7:
    print(start)
    start += 1

for i in range(0, 10, 2):
    print(i)

some_list = ["apple", "banana", "cherry", "raspberry", "strawsberry"]
for index, value in enumerate(some_list):
    print(index, value)

'''
0 apple
1 banana
2 cherry
3 raspberry
4 strawsberry
'''

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат", "груша"]
for number, letter in zip(list1, list2):
    print(number, letter)
'''
зелене яблуко
стигла вишня
червоний томат
'''