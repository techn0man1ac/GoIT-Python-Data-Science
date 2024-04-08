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